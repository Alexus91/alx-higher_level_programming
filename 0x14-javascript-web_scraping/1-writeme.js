#!/usr/bin/node
/* script that writes a string to a file */

const fs = require('fs');
const name = process.argv[2];
const text = process.argv[3];
fs.writeFile(name, text, 'utf8', (err) => {
  if (err) console.log(err);
});
