#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}; // Create an empty object if w or h is 0 or not a positive integer
    }
    this.width = w;
    this.height = h;
  }

  print() {
    if (Object.keys(this).length === 0) {
      return; // If the object is empty, return without printing
    }
    const row = 'X'.repeat(this.width); // Create a row of X characters with the width of the rectangle
    for (let i = 0; i < this.height; i++) {
      console.log(row); // Print the row for each row in the rectangle
    }
  }

  rotate() {
    if (Object.keys(this).length === 0) {
      return; // If the object is empty, return without rotating
    }
    // Exchange the width and height of the rectangle
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double() {
    if (Object.keys(this).length === 0) {
      return; // If the object is empty, return without doubling
    }
    // Multiply the width and height of the rectangle by 2
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
