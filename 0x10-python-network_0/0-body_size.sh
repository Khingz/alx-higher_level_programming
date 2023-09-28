#!/bin/bash
# Gets the size in byte of a url
curl -sI "$1" | grep "Content-Length" | awk -F " " '{print $2}'
