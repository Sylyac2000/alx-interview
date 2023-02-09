#!/usr/bin/node
const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/';
const endpoint = 'films/';

const url = baseUrl + endpoint + process.argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const datas = JSON.parse(body);
    // console.log(datas);
    const characters = datas.characters;
    // console.log(typeof characters);
    characters.forEach((anUrl) => {
      request(anUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
