#!/usr/bin/env bash
# Return request status code
curl -s -o /dev/null -w "%{http_code}" "$1"
