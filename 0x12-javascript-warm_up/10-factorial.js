#!/usr/bin/node

const arg = parseInt(process.argv[2]);
function factorial (num) {
  if (isNaN(arg)) {
    console.log(1);
    return;
  }
  if (num === 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}
console.log(factorial(arg));
