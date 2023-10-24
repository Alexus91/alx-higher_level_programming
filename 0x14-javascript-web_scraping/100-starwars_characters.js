#!/usr/bin/node
/* script that prints all characters of a Star Wars movie */
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, function (error, response, body) {
  if (error) console.log(error);
  for (const URLCH of JSON.parse(body).characters) {
    request(URLCH, (error, response, body) =>
      !error && console.log(JSON.parse(body).name));
  }
});
