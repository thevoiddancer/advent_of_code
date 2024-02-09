'use strict';

const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'data.txt');

fs.readFile(filePath, 'utf8', applyLogic);

function applyLogic(err, data) {
    if (err) {
        console.error(err);
    }

    const opening = count(data, '(');
    const closing = count(data, ')');
    console.log(opening - closing);
};

function count(str, char) {
    let c = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === char) {
            c++;
        }
    }
    return c;
};
