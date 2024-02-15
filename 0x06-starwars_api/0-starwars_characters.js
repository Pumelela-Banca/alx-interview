#!/usr/bin/node
// Prints all  characters of a star-wars movie

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const pross = require('process');

if (pross.argv.length > 2) {
  request(url + pross.argv[2], function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        })
    );

    Promise.all(charactersName)
      .then((names) => console.log(names.join('\n')))
      .catch((allErr) => console.log(allErr));
  });
}
