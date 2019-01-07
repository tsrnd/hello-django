#!/bin/bash
until psql "$DATABASE_URL" -c '\l'; do
  echo "Postgres is unavailable - sleeping";
  sleep 1;
done
echo "Postgres is up - continuing"
