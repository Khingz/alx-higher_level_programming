#!/usr/bin/node

const argc = process.argv.length - 2;
if (argc < 1) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
