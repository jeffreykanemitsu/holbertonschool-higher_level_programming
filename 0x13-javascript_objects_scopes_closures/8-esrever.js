#!/usr/bin/node
// Write a function that returns the reversed version of a list
exports.esrever = function (list) {
  let rev = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
