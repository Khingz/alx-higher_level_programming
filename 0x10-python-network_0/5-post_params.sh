#!/bin/bash
# post request with curl
curl -d "email=test@gmail.com&subject=I will always be here for PLD" -sX POST "$1"