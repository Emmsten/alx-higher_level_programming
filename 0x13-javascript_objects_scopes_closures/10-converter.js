#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBase(num) {
    if (num === 0) {
      return '';
    }
    return convertToBase(Math.floor(num / base)) + (num % base);
  };
};
