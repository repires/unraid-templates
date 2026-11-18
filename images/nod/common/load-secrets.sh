# Sourced by the entrypoint and healthcheck (as node).
# Exports generated secrets unless the container already sets them, and builds
# DATABASE_URL from NOD_POSTGRES_PASSWORD when no URL is given.
if [ -n "${NOD_SECRETS_FILE:-}" ] && [ -r "$NOD_SECRETS_FILE" ]; then
  # Read whole lines: base64 values end in "=", which IFS splitting would drop.
  while IFS= read -r line; do
    case $line in
      NOD_AUTH_TOKEN=*) [ -n "${NOD_AUTH_TOKEN:-}" ] || export NOD_AUTH_TOKEN="${line#*=}" ;;
      NOD_VAULT_KEY=*) [ -n "${NOD_VAULT_KEY:-}" ] || export NOD_VAULT_KEY="${line#*=}" ;;
    esac
  done < "$NOD_SECRETS_FILE"
fi

if [ -z "${DATABASE_URL:-}" ] && [ -n "${NOD_POSTGRES_PASSWORD:-}" ]; then
  export DATABASE_URL="postgresql://nod:${NOD_POSTGRES_PASSWORD}@${NOD_POSTGRES_HOST:-nod-postgres}:5432/nod"
fi
