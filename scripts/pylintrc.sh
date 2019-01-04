#!/bin/bash

pipenv run pylint \
  --disable=all \
  --enable=F,E,unreachable,duplicate-key,unnecessary-semicolon\
    ,global-variable-not-assigned,unused-variable,binary-op-exception\
    ,bad-format-string,anomalous-backslash-in-string,bad-open-mode \
  --load-plugins pylint_django \
  --generate-rcfile \
  > .pylintrc
