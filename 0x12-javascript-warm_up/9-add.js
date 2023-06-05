#!/usr/bin/node
// Muideen27
// 9-add.js
// write a script that prints the addition of 2 interger

function add (a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
