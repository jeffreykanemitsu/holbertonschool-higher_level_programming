#!/usr/bin/node
// Write a script that imports an array and computes a new array
const list = require('./100-data').list;
const list2 = list.map((element, index) => element * index);
console.log(list);
console.log(list2);
