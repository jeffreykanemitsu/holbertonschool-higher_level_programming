#!/usr/bin/node
// searches the second biggest int in the list of arguments
if (process.argv.length < 4) {
  console.log('0');
} else {
  process.argv.sort();
  console.log(process.argv.slice(-2)[0]);
}
