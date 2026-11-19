#!/bin/sh
set -eu
if [ "$#" -ne 2 ]; then
  echo 'Usage: ./builder.sh <github-repo> <docker-image>' >&2
  exit 1
fi
tmp_dir=$(mktemp -d)
trap 'rm -rf "$tmp_dir"' EXIT HUP INT TERM
git clone "https://github.com/$1" "$tmp_dir/repo"
docker build -t "$2" "$tmp_dir/repo"
docker push "$2"