#!/bin/sh
for PY_DIR in $(find ./myapp -type f -name '*.py' -print0 | xargs -0 -n1 dirname | sort -u); do
  touch "$PY_DIR/__init__.py"
done
