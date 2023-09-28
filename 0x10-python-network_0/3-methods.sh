#!/bin/bash
# Checks server options
curl -sX OPTIONS -i "$1" | grep "Allow" | cut -d' ' -f2-
