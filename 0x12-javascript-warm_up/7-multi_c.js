#!/usr/bin/node
// Muideen27
// 7-multi_c.js
// Write a script that prints x times “C is fun

const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  };
};
