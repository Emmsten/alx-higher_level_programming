#!/usr/bin/node

function secondBiggest(args) {
    if (args.length <= 2) {
        return 0;
    }

    let max = -Infinity;
    let secondMax = -Infinity;

    for (let i = 2; i < args.length; i++) {
        const num = parseInt(args[i]);
        if (num > max) {
            secondMax = max;
            max = num;
        } else if (num > secondMax && num < max) {
            secondMax = num;
        }
    }

    return secondMax;
}

console.log(secondBiggest(process.argv));
