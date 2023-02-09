#!/usr/bin/node
const request = require('request');

const fetchData = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(error);
      }
    });
  });
};

const baseUrl = 'https://swapi-api.alx-tools.com/api/';
const endpoint = 'films/';

const url = baseUrl + endpoint + process.argv[2];

const fetchDataFromUrls = async () => {
  try {
    const data = await fetchData(url);
    // console.log(data.characters);
    const charactersUrl = data.characters;
    for (const url of charactersUrl) {
      try {
        const data = await fetchData(url);
        const characterName = data.name;
        console.log(characterName);
      } catch (error) {

      }
    }
  } catch (error) {

    // console.error(error);
  }
};

fetchDataFromUrls();
