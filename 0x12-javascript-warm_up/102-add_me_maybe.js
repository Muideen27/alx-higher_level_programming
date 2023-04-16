#!/usr/bin/node
// Muideen27
// 102-add_me_maybe.js
// Write a function that increments and calls a function.

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
