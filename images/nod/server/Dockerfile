# Context: images/nod. BASE is upstream's deployment/self-host/Dockerfile build.
ARG BASE
FROM ${BASE}
USER root
COPY common/ /usr/local/lib/nod/
COPY server/nod-healthcheck /usr/local/bin/nod-healthcheck
RUN chmod 0755 /usr/local/lib/nod && chmod 0555 /usr/local/lib/nod/entrypoint.sh /usr/local/bin/nod-healthcheck \
    && chmod 0444 /usr/local/lib/nod/load-secrets.sh
ENV NOD_OWNED_DIRS="/var/lib/nod /var/lib/nod/workspaces" \
    NOD_SECRETS_FILE=/var/lib/nod/secrets.env
HEALTHCHECK --interval=15s --timeout=6s --retries=10 --start-period=60s CMD ["nod-healthcheck"]
ENTRYPOINT ["/usr/local/lib/nod/entrypoint.sh"]
CMD ["node", "--import", "tsx", "src/server/index.ts"]
