#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    }
  }
}

module.exports = Square;
