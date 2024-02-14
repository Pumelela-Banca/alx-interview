#!/usr/bin/node
// Prints all  characters of a star-wars movie

const request = require('request');
let id = Number(process.argv[2]);

request('https://swapi-api.alx-tools.com/api/films', (error, body) => {
  if (error) {
    console.error('An error occurred:', error);
  }
  let jsonObject = JSON.parse(body.body);
  for (let names of jsonObject.results) {
    if (names.episode_id === id) {
      break;
    }}
  for (let specific_url of names.characters) {
    request(specific_url, (error, data) => {
      if (error) {
        console.error('An error occurred:', error);
      }
      let actor = JSON.parse(data.body);
      console.log(actor.name);
    });
  }
});
