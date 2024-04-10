#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [...list]; // Create a copy of the original list
  
  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    // Swap elements at index i and j
    const temp = reversedList[i];
    reversedList[i] = reversedList[j];
    reversedList[j] = temp;
  }
  
  return reversedList;
};
