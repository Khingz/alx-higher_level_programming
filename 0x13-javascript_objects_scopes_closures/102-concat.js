#!/usr/bin/node

if (process.argv.length === 5) {
  const fs = require('fs');
  fs.readFile(process.argv[2], 'utf8', (err, data1) => {
    if (err) {
      return;
    }
    fs.readFile(process.argv[3], 'utf8', (err, data2) => {
      if (err) {
        return;
      }
      const data = data1 + data2;
      fs.writeFile(process.argv[4], data, 'utf8', (err) => {
        if (err) {
          console.log('');
        }
      });
    });
  });
}
