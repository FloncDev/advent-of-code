import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
})

let p1total = 0;
let p2total = 0;
let enabled = true;

rl.on('line', (line) => {
  line.matchAll(/(?:mul\((\d{1,3}),(\d{1,3})\))|don\'t\(\)|do\(\)/gm).forEach(match => {
    switch (match[0]) {
      case "do()":
        enabled = true;
        break;

      case "don't()":
        enabled = false;
        break;

      default:
        p1total += match[1] * match[2];

        if (enabled) {
          p2total += match[1] * match[2];
        }
    }
  });
})

rl.on('close', () => {
  console.log(p1total, p2total);
})
