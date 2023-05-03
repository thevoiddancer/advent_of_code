const fs = require('fs');
const path = require('path');
const { mainModule } = require('process');
const filePath = path.join(__dirname, 'data.txt');

let d = fs.readFile(filePath, 'utf8', apply_logic)

function apply_logic(err, data) {
    data = data.split('\n');
    paper = 0;
    for (key in data) {
        box = data[key].split('x');
        area1 = box[0]*box[1];
        area2 = box[1]*box[2];
        area3 = box[2]*box[0];
        area = 2*(area1 + area2 + area3) + Math.min(area1, area2, area3);
        paper += area;
    }
    console.log(paper);
}

