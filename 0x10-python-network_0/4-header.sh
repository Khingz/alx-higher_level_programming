#!/bin/bash
# sends request and sets a header variable
curl -sH "X-School-User-Id: 98" "$1"
