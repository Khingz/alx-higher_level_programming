#!/usr/bin/node

exports.esrever = function (list) {
  revList = [];
  for (let i in list) {
   revList.unshift(list[i]);
  }
  return (revList);
}
