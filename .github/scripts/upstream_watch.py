#!/usr/bin/env python3
"""Watch the upstream files our templates depend on.

`check` compares each watched file (at the upstream's latest release, or its
default branch) with the fingerprint in .github/upstream-watch.json, plus the
major version of templates that pin one, and writes a Markdown report per app
that changed to $REPORT_DIR. `update` records the current state as the new
baseline after the templates have been reviewed.

Usage: upstream_watch.py check|update
"""
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASELINE = ROOT / '.github' / 'upstream-watch.json'
API = 'https://api.github.com'


def get(url, raw=False):
    headers = {'Accept': 'application/vnd.github.raw' if raw else 'application/vnd.github+json',
               'User-Agent': 'repires-upstream-watch'}
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
    if token:
        headers['Authorization'] = f'Bearer {token}'
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
        body = response.read()
    return body if raw else json.loads(body)


def current_ref(repo, mode):
    if mode == 'release':
        return get(f'{API}/repos/{repo}/releases/latest')['tag_name']
    return get(f'{API}/repos/{repo}')['default_branch']


def fingerprint(repo, ref, path):
    try:
        return hashlib.sha256(get(f'{API}/repos/{repo}/contents/{path}?ref={ref}', raw=True)).hexdigest()
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return 'missing'
        raise


def snapshot(app):
    repo, mode = app['repo'], app['ref']
    ref = current_ref(repo, mode)
    commit = get(f'{API}/repos/{repo}/commits/{ref}')['sha']
    state = {'ref': ref, 'commit': commit,
             'files': {path: fingerprint(repo, ref, path) for path in app['files']}}
    if 'major' in app:
        state['latest_major'] = ref.lstrip('v').split('.')[0]
    return state


def report(name, app, old, new):
    lines = []
    for path, digest in new['files'].items():
        before = old.get('files', {}).get(path)
        if before != digest:
            what = 'removed' if digest == 'missing' else 'added' if before in (None, 'missing') else 'changed'
            lines.append(f'- `{path}` {what}')
    if 'major' in app and new.get('latest_major') != app['major']:
        lines.append(f"- New major version **{new['ref']}**: the template still uses "
                     f"`:{app['major']}`, so users stay on {app['major']}.x until the template changes.")
    if not lines:
        return None
    compare = f"https://github.com/{app['repo']}/compare/{old.get('commit', '')[:12]}...{new['commit'][:12]}"
    return '\n'.join([
        f"Upstream [{app['repo']}](https://github.com/{app['repo']}) moved from `{old.get('ref', '?')}` "
        f"to `{new['ref']}`, and files that `{', '.join(app['templates'])}` depend on changed:",
        '', *lines, '', f'Diff: {compare}', '',
        'Check the template still matches (settings, ports, paths, user, healthcheck). Then run the '
        '**Upstream watch** workflow with **accept** enabled to record this version as reviewed.',
    ])


def main(mode):
    data = json.loads(BASELINE.read_text())
    out = Path(os.environ.get('REPORT_DIR', 'upstream-reports'))
    out.mkdir(exist_ok=True)
    changed = 0
    for name, app in data['apps'].items():
        new = snapshot(app)
        if mode == 'update':
            app['baseline'] = new
            continue
        text = report(name, app, app.get('baseline', {}), new)
        if text:
            (out / f'{name}.md').write_text(text)
            changed += 1
            print(f'{name}: changes to review')
        else:
            print(f'{name}: unchanged ({new["ref"]})')
    if mode == 'update':
        BASELINE.write_text(json.dumps(data, indent=2) + '\n')
        print('baseline updated')
    return changed


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'check')
