#!/bin/bash
if [[ -d "$HOME/.docker/images" ]]; then
  find "$HOME/.docker/images" -name "*.tar.gz" | xargs -I {file} sh -c "zcat < {file} | docker load"
fi
