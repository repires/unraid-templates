# Context: images/nod. BASE is upstream's Dockerfile.workspace build.
# The same image also runs as nod-workspace-network (entrypoint overridden there),
# so it carries no HEALTHCHECK of its own.
ARG BASE
FROM ${BASE}
USER root
COPY common/ /usr/local/lib/nod/
RUN chmod 0755 /usr/local/lib/nod && chmod 0555 /usr/local/lib/nod/entrypoint.sh \
    && chmod 0444 /usr/local/lib/nod/load-secrets.sh
ENV NOD_OWNED_DIRS="/workspace /home/node"
ENTRYPOINT ["/usr/local/lib/nod/entrypoint.sh"]
CMD ["sleep", "infinity"]
