#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let ir = '';
    for (let ic = 0; ic < size; ic++) ir += 'X';
    console.log(ir);
  }
}
