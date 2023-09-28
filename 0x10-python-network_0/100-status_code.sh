#!/usr/bin/env bash
# Return request status code
curl -s -o /dev/null "$1" -w "%{http_code}"
