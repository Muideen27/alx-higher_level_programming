#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given integer.
const argv = require('process').argv;
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

// Request module is async and for us to have the list in order we need to
// make our requests in a synchronous manner
// Recursive functions to make synchronous requests
function makeRequests (urls) {
  const url = urls.shift();
  request(url, (error, response, body) => {
    // If the list is not empty do some recursion
    if (urls.length) {
      makeRequests(urls);
    }
    if (error) {
      console.log(error);
    }

    console.log(JSON.parse(body).name);
  });
}

// Request the film data
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const characters = JSON.parse(body).characters;
  // Make a request for each character
  makeRequests(characters);
});
