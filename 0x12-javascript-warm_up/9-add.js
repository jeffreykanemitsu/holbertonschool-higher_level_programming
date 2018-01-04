#!/usr/bin/node
// prints the addition of two integers
let first = parseInt(process.argv[2]);
let second = parseInt(process.argv[3]);
function add (a, b) {
  return a + b;
}
console.log(add(first, second));
