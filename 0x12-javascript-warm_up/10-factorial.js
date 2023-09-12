#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 1) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(Math.floor(Number(process.argv[2]))));
