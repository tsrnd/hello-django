#!/bin/bash
docker-compose run app sh ./scripts/pylint.sh
pip install -U lintly
cat ./reports/pylint.json | lintly --format=pylint-json --api-key=$GITHUB_ACCESS_TOKEN
