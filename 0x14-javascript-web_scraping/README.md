# JavaScript Web Scraping

This repository contains JavaScript scripts for various web scraping tasks. Each script solves a specific problem using Node.js along with the `request` module for making HTTP requests.

## Requirements

- Ubuntu 20.04 LTS
- Node.js version 14.x
- npm packages: `request` and `semistandard`

## Installation

To install Node.js version 14.x:

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

1. To install the required npm packages:

$ sudo npm install request --global
$ sudo npm install semistandard --global
$ export NODE_PATH=/usr/lib/node_modules

Scripts
0-readme.js
Reads and prints the content of a file.

Usage:

$ ./0-readme.js <file_path>

1-writeme.js
Writes a string to a file.

Usage:

$ ./1-writeme.js <file_path> <string_to_write>

2-statuscode.js
Displays the status code of a GET request.

Usage:

$ ./2-statuscode.js <URL>

3-starwars_title.js
Prints the title of a Star Wars movie with a given movie ID.

Usage:

$ ./3-starwars_title.js <movie_id>

4-starwars_count.js
Prints the number of movies where the character “Wedge Antilles” is present.

Usage:

$ ./4-starwars_count.js <API_URL>

5-request_store.js
Gets the contents of a webpage and stores it in a file.

Usage:

5-request_store.js
Gets the contents of a webpage and stores it in a file.

Usage:

$ ./5-request_store.js <URL> <file_path>

6-completed_tasks.js
Computes the number of tasks completed by user id.

Usage:6-completed_tasks.js
Computes the number of tasks completed by user id.

Usage:

$ ./6-completed_tasks.js <API_URL>



This README.md file provides an overview of the project, instructions for installation, and usage examples for each script. Feel free to modify and expand it according to your needs.
