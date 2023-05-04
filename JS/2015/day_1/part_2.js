const fs = require('fs');
const path = require('path');
const filePath = path.join(__dirname, 'data.txt');

let d = fs.readFile(filePath, 'utf8', apply_logic)

function apply_logic(err, data) {
    if (err) throw err;
    console.log(to_basement(data));
}

const dir = { 
    "(": 1, 
    ")": -1, 
};

function to_basement(str) {
    let level = 0;
    let i;
    for (i = 0; i < str.length; i++) {
        level += dir[str[i]];
        if (level == -1) {
            break;
        };
    };
    return i + 1;
};



// let data = "()())";
// console.log(to_basement(data));