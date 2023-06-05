#!/usr/bin/node

// Muideen27
// 2-arguments.js
// Write a script that prints a message
// depending of the number of arguments passed

const count = process.argv.length;

if (count === 2) {
console.log('No argument');
} else if (count === 3) {
console.log('Argument found');
} else {
console.log('Arguments found');
};
