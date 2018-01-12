#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let dict = {};
    const id = JSON.parse(body);
    for (let todo in id) {
      let task = id[todo];
      if (task.completed === true) {
        if (task.userId in dict) {
          dict[task.userId]++;
        } else {
          dict[task.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
