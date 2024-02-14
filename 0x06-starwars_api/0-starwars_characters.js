#!/usr/bin/node
// Prints all  characters of a star-wars movie

const request = require('request');
const util = require('util');
let id = Number(process.argv[2]);

request('https://swapi-api.alx-tools.com/api/films', async (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }
  let jsonObject = JSON.parse(body);
  let char_names;
  for (let names of jsonObject.results) {
    if (names.episode_id === id) {
      char_names = names.characters;
      break;
    }
  }
  const requestPromise = util.promisify(request);
  async function makeRequestsInOrder(urls) {
    for (let url of urls) {
      try {
        const response = await requestPromise(url);
        console.log(JSON.parse(response.body).name);
      } catch (error) {
        console.error(`An error occurred while making a request to ${url}:`, error);
      }
    }
  }
  await makeRequestsInOrder(char_names);
});
