#!/usr/bin/node
// Muideen27
// 9-add.js
// write a script that prints the addition of 2 interger

fuction addNumber (a, b) {
	return a + b
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);
	if (isNaN(arg1) || isNaN(arg2)) {
		console.log("Missing or invalid argument(s)");
	} else {
		const result = addNumber(arg1, arg2);
		console.log(result);
	}
