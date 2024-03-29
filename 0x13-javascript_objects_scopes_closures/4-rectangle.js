#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.hight] = [w, h]; }
  }

  print () {
    for (let i = 0; i < this.hight; i++) console.log('X'.repeat(this.width));
  }

  rotate () {
    [this.width, this.hight] = [this.hight, this.width];
  }

  double () {
    [this.width, this.hight] = [this.width * 2, this.hight * 2];
  }
};
