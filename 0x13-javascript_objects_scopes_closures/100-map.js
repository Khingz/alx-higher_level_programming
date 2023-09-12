#!/usr/bin/node
const { list } = require('./100-data.js');

const newArr = [];
list.map((item, index) => {
  return newArr.push(item * index);
});
console.log(list);
console.log(newArr);
