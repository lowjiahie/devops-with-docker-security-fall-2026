#!/bin/sh
set -eu
if [ "$#" -ne 2 ]; then
  echo 'Usage: builder <github-repo> <docker-image>' >&2
  exit 1
fi
: "${DOCKER_USER:?DOCKER_USER is required}"
: "${DOCKER_PWD:?DOCKER_PWD is required}"
export DOCKER_CONFIG="$(mktemp -d)"
tmp_dir=$(mktemp -d)
trap 'rm -rf "$tmp_dir" "$DOCKER_CONFIG"' EXIT HUP INT TERM
printf '%s' "$DOCKER_PWD" | docker login --username "$DOCKER_USER" --password-stdin
git clone "https://github.com/$1" "$tmp_dir/repo"
docker build -t "$2" "$tmp_dir/repo"
docker push "$2"