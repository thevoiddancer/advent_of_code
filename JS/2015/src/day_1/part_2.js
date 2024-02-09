'use strict';

const fs = require('fs');
const path = require('path');
const filePath = path.join(__dirname, 'data.txt');

const dir = {
    "(": 1,
    ")": -1,
};

function applyLogic(err, data) {
    if (err) {
        throw err;
    }
    console.log(toBasement(data));
}

function toBasement(str) {
    let level = 0;
    let i;

    for (i = 0; i < str.length; i++) {
        level += dir[str[i]];
        if (level == -1) {
            break;
        }
    }

    return i + 1;
};

fs.readFile(filePath, 'utf8', applyLogic)
