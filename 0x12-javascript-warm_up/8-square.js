#!/usr/bin/node

const argsSquare = process.argv;
const number = parseInt(argsSquare[2], 10);

if (argsSquare[2]) {
  if (number) {
    for (let i = 0; i < number; i++) {
      let square = '';
      for (let j = 0; j < number; j++) {
        square += 'X';
      }
      console.log(square);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
