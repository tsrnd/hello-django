#!/bin/bash
mkdir -p reports
pylint myproject myapp --output-format=json > ./reports/pylint.json
