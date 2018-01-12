#!/usr/bin/node
// Write a script that prints the number of movies where the character
//  “Wedge Antilles” is present
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    for (let i = 0; i < JSON.parse(body).results.length; i++) {
      if (JSON.parse(body).results[i].characters.includes('https://swapi.co/api/people/18/')) {
        count++;
      }
    }
    return console.log(count);
  }
});
