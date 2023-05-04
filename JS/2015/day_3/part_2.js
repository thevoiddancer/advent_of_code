
const fs = require('fs');
const path = require('path');
const filePath = path.join(__dirname, 'data.txt');

let d = fs.readFile(filePath, 'utf8', apply_logic)

function apply_logic(err, data) {
    loc = [0, 0]
    loc_rs = [0, 0]
    visited = new Set();
    visited.add(JSON.stringify(loc));
    for (idx = 0; idx < data.length; idx += 2) {
        chr = data[idx]
        loc = move(loc, chr);
        loc_str = JSON.stringify(loc);
        if (!visited.has(loc_str)) {
            visited.add(loc_str);
        }

        chr_rs = data[idx + 1]
        loc_rs = move(loc_rs, chr_rs);
        loc_str_rs = JSON.stringify(loc_rs);
        if (!visited.has(loc_str_rs)) {
            visited.add(loc_str_rs);
        }
    }
    console.log(visited.size);
}

const dir = {
    ">": [1, 0], 
    "<": [-1, 0], 
    "^": [0, 1], 
    "v": [0, -1],
};


function move(loc, char) {
    step = dir[char];
    result = loc.map((num, index) => num + step[index]);
    return result;
}
