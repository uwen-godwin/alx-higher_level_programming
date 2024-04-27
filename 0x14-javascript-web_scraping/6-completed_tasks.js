#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const tasks = JSON.parse(body);
  const completedTasksByUser = tasks.reduce((result, task) => {
    if (task.completed) {
      result[task.userId] = (result[task.userId] || 0) + 1;
    }
    return result;
  }, {});
  console.log(completedTasksByUser);
});
