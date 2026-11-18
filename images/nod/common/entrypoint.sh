#!/bin/sh
# Unraid wrapper entrypoint for the Nod images.
#
# Starts as root only long enough to:
#   1. hand freshly created appdata folders to uid/gid 1000 (Unraid creates
#      missing host paths as root, while Nod runs as the image's node user);
#   2. (as node) generate NOD_AUTH_TOKEN / NOD_VAULT_KEY once, when NOD_SECRETS_FILE is set
#      and the template does not provide them.
# Then it re-executes itself as node and runs the image command.
#
# NOD_OWNED_DIRS: space-separated "path" or "path:mode" entries.
set -eu

if [ "$(id -u)" = 0 ]; then
  for entry in ${NOD_OWNED_DIRS:-}; do
    dir=${entry%%:*}
    [ -d "$dir" ] || continue
    if [ "$(stat -c %u:%g "$dir")" != 1000:1000 ]; then
      # chmod while root still owns the folder: with all capabilities dropped,
      # root cannot change the mode of a folder it no longer owns.
      [ "$entry" = "$dir" ] || chmod "${entry#*:}" "$dir"
      chown -R 1000:1000 "$dir"
    fi
  done
  export HOME=/home/node USER=node
  exec setpriv --reuid=1000 --regid=1000 --init-groups -- "$0" "$@"
fi

if [ -n "${NOD_SECRETS_FILE:-}" ] && [ ! -e "$NOD_SECRETS_FILE" ]; then
  (
    umask 077
    {
      echo '# Generated on first start. Template values for these keys take precedence.'
      echo '# Back up NOD_VAULT_KEY: without it, saved credentials cannot be decrypted.'
      echo "NOD_AUTH_TOKEN=$(od -An -tx1 -N32 /dev/urandom | tr -d ' \n')"
      echo "NOD_VAULT_KEY=$(head -c 32 /dev/urandom | base64)"
    } > "$NOD_SECRETS_FILE"
  )
  echo "Generated Nod secrets in $NOD_SECRETS_FILE (sign in with NOD_AUTH_TOKEN from that file)."
fi

. /usr/local/lib/nod/load-secrets.sh
exec "$@"
