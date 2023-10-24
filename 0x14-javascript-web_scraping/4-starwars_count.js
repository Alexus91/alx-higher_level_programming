#!/usr/bin/node
const request = require('request');
const fd = '/18/';
request(process.argv[2], function (error, response, body) {
  if (error) console.error(error);
  let number = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      number += (character.endsWith(fd) ? 1 : 0);
    }
  }
  console.log(number);
});
