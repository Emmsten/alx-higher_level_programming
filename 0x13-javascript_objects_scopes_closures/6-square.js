#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint(c = 'X') {
    // Check if the character is undefined and set it to 'X' if so
    const char = c === undefined ? 'X' : c;
    
    // Printing the square using the specified character
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
