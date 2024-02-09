const fs = require('fs');
const path = require('path');
const { mainModule } = require('process');
const filePath = path.join(__dirname, 'data.txt');

let d = fs.readFile(filePath, 'utf8', apply_logic)

function apply_logic(err, data) {
    data = data.split('\n');
    ribbon = 0;
    for (key in data) {
        box = data[key].split('x').map((val) => parseInt(val));
        length = 2 * (box.reduce((sum, val) => sum + parseInt(val), 0) - Math.max(...box)) + box.reduce((prod, val) => prod * parseInt(val), 1)
        ribbon += length;
    }
    console.log(ribbon);

}

