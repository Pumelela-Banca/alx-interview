#!/usr/bin/node
// Prints all  characters of a star-wars movie

const request = require('request');
let id = Number(process.argv[2]);


request('https://swapi-api.alx-tools.com/api/filims', (error, body) => {
  if (error) {
    console.error('An error occurred:', error);
  }
  for (let names of body.results) {
    if (names.episode_id == id) {
      break;
    }}
  for (let chars of names.characters) {
    request(chars, (data) => {
      console.log(data.name);
    });
  }
});
