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
    if (names.episode_id == id) {
      var char_names = names.characters;
      break;
    }}
  for (let specific_url of char_names) {
    request(specific_url, (error, data) => {
      let actor = JSON.parse(data.body);
      console.log(actor.name);
    });
  }
});
