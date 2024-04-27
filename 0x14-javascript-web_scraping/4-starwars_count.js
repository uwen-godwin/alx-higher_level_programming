#!/usr/bin/node

const http = require('http');
const request = require('request');

const PORT = 8080;

# Function to start the local server
const startServer = () => {
  const server = http.createServer((req, res) => {
    request('https://swapi-api.alx-tools.com/api/films', (error, response, body) => {
      if (error) {
        res.statusCode = 500;
        res.end('Internal Server Error');
        return;
      }
      const films = JSON.parse(body).results;
      const count = films.reduce((total, film) => {
        if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          return total + 1;
        }
        return total;
      }, 0);
      res.end(count.toString());
    });
  });

  server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
  });
};

startServer();
