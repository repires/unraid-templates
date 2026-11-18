# PostgreSQL for Nod: official postgres:17-alpine with Nod's database defaults
# and a healthcheck, so the Unraid template needs no extra parameters.
FROM postgres:17-alpine
ENV POSTGRES_USER=nod \
    POSTGRES_DB=nod
HEALTHCHECK --interval=5s --timeout=3s --retries=30 CMD ["pg_isready", "-U", "nod", "-d", "nod"]
