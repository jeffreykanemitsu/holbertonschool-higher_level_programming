#!/usr/bin/node
// prints a message depending on the number of arguments passed
if ((process.argv).length < 3) {
  console.log('No argument');
} else if (process.argv[3]) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
