FROM docker:28-cli
RUN apk add --no-cache git
COPY builder.sh /usr/local/bin/builder
RUN chmod +x /usr/local/bin/builder
ENTRYPOINT ["/usr/local/bin/builder"]