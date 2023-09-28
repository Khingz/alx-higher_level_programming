#!/bin/bash
# Return request status code
curl -sI "$1" | grep "HTTP" | awk -F " " '{print $2}'
