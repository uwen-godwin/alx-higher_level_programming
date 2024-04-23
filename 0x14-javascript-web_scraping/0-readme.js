#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(`\x1b[32m{ Error: ${err.message}\n  \x1b[32merrno: ${err.errno},\n  \x1b[32mcode: '${err.code}',\n  \x1b[32msyscall: '${err.syscall}',\n  \x1b[32mpath: '${err.path}' }\x1b[0m`);
    return;
  }
  console.log(data);
});
