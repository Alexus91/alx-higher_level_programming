#!/usr/bin/node
const { dict } = require('./101-data');

const sortedDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (sortedDict[occurrences]) {
    sortedDict[occurrences].push(userId);
  } else {
    sortedDict[occurrences] = [userId];
  }
}

console.log(sortedDict);
