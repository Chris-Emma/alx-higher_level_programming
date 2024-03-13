#!/usr/bin/node

const firstArgument = parseInt(process.argv[2]);
const secondArgument = parseInt(process.argv[3]);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return a + b;
}
console.log(add(firstArgument, secondArgument));
