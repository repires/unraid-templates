# Context: images/nod. docker-proxy.mjs is copied from the matching upstream
# release (deployment/self-host/docker-proxy.mjs) by the build workflow.
FROM node:24.21.0-bookworm-slim
COPY runtime/docker-proxy.mjs /app/docker-proxy.mjs
RUN chmod 0755 /app && chmod 0444 /app/docker-proxy.mjs
CMD ["node", "/app/docker-proxy.mjs"]
