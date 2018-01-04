#!/usr/bin/node
// incrememnts and calls a function
module.exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
