const data = require('./dev.json')[0].trends;

console.log("All trending topics are:");
for(let i = 0; i < data.length; i++) {
    console.log(data[i].name);
}