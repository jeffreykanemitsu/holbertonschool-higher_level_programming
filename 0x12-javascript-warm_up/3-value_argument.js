#!/usr/bin/node
// prints first argument passed
if ((process.argv).length < 3) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
