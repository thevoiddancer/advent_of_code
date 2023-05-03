const fs = require('fs');
const path = require('path');
const filePath = path.join(__dirname, 'data.txt');

let d = fs.readFile(filePath, 'utf8', apply_logic)

function apply_logic(err, data) {
    opening = count(data, "(");
    closing = count(data, ")");
    console.log(opening-closing);
}

function count(str, char) {
    c = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] == char) {
            c++;
        }
    }
    return c
}

