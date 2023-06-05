#!/usr/bin/node
// Muideen27
// 5-to_integer.js
// Write a script that prints My number: <first argument converted in integer
// if the first argument can be converted to an integer

const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
