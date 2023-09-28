#!/bin/bash
# post request with curl
curl -sX POST -H "Content-Type: application/json" -d @$2 "$1"
