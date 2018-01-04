#!/usr/bin/node
// prints "My number" if the first argument can be converted to an int
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + process.argv[2]);
}
