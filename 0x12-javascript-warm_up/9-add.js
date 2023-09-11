#!/usr/bin/node

num1 = parseInt(process.argv[2]);
num2 = parseInt(process.argv[3]);

function add(a, b) {
  console.log(a + b);
}
add(num1, num2);
