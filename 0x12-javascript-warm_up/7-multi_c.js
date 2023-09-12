#!/usr/bin/node
const numOccurrences = parseInt(process.argv[2]);

if (!isNaN(numOccurrences) && numOccurrences > 0) {
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
