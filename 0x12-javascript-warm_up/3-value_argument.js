#!/usr/bin/node
// Muideen27
// Write a script that prints the first argument passed to it

const arg = process.argv[2];
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
