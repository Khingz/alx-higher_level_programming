#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  for (const i in list) {
    revList.unshift(list[i]);
  }
  return (revList);
};
