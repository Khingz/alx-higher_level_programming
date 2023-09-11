#!/usr/bin/node

const arr = [];
const len = process.argv.length;
if (len === 2) {
  console.log(0);
} else if (len === 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    arr.push(Number(process.argv[i]));
  }
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
