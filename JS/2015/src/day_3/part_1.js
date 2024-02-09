
const fs = require('fs');
const path = require('path');
const filePath = path.join(__dirname, 'data.txt');

let d = fs.readFile(filePath, 'utf8', apply_logic)

function apply_logic(err, data) {
    loc = [0, 0]
    visited = new Set();
    visited.add(JSON.stringify(loc));
    for (char of data) {
        loc = move(loc, char);
        loc_str = JSON.stringify(loc);
        if (!visited.has(loc_str)) {
            visited.add(loc_str);
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
