# Context: images/nod. BASE is upstream's Dockerfile.browser build.
ARG BASE
FROM ${BASE}
USER root
COPY common/ /usr/local/lib/nod/
RUN chmod 0755 /usr/local/lib/nod && chmod 0555 /usr/local/lib/nod/entrypoint.sh \
    && chmod 0444 /usr/local/lib/nod/load-secrets.sh
ENV NOD_OWNED_DIRS="/data:700"
# Healthchecks run as root without capabilities, so check /data (mode 700) as node.
HEALTHCHECK --interval=5s --timeout=3s --retries=30 \
  CMD ["setpriv", "--reuid=1000", "--regid=1000", "--init-groups", "test", "-S", "/data/control.sock"]
ENTRYPOINT ["/usr/local/lib/nod/entrypoint.sh"]
CMD ["node", "/app/worker.mjs"]
