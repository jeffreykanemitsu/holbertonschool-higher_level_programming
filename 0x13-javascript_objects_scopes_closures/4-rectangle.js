#!/usr/bin/node
// Write a class Rectangle that defines a rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
  rotate () {
	  let newWidth = this.width;
	  this.width = this.height;
	  this.height = newWidth;
  }
  double () {
	  this.width *= 2;
	  this.height *= 2;
  }
};
