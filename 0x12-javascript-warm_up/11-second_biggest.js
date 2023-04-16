#!/usr/bin/node
// Muideen27
// 11-second_biggest.js
// write a scrip thar searches the second biggest integer in the list or arguments

const args = process.argv.slice(2).map(Number); 
// Get arguments and convert them to numbers

if (args.length === 0) {
	console.log(0); // If no argument passed, print 0
} else if (args.length === 1) {
	console.log(0); // If the number of arguments is 1, print 0
} else {
	const sortedArgs = args.sort((a, b) => b - a); // Sort arguments in descending order
	console.log(sortedArgs[1]); // Print the second biggest integer
}

