#!/usr/bin/node

const numOccurence = parseInt(process.argv[2]);
if (isNaN(numOccurence)) {
  console.log('Missing number of occurences');
} else {
  let i;
  for (i = 0; i < numOccurence; i++) {
    console.log('C is fun');
  }
}
