# Project Title

## Description
This repository contains Bash scripts and Python scripts for performing various tasks related to network communication using cURL and Python requests library.

## Requirements
- All scripts were tested on Ubuntu 20.04 LTS.
- All Bash scripts are exactly 3 lines long.
- All files end with a new line.
- All files are executable.
- The first line of all Bash files is `#!/bin/bash`.
- The second line of all Bash scripts is a comment explaining what the script does.
- All curl commands have the option `-s` (silent mode).
- Python3 (version 3.8.5) is used for interpretation.
- Python modules, classes, and functions are documented.
- Pycodestyle (version 2.8.*) is used.
- A README.md file is provided at the root of the folder.

## List of Scripts
1. `0-body_size.sh`: Retrieves the size of the body of a response from a URL.
2. `1-body.sh`: Retrieves the body of a response from a URL.
3. `2-delete.sh`: Sends a DELETE request to a URL and displays the body of the response.
4. `3-methods.sh`: Displays all HTTP methods accepted by a server for a given URL.
5. `4-header.sh`: Sends a GET request to a URL with a custom header and displays the body of the response.
6. `5-post_params.sh`: Sends a POST request with parameters to a URL and displays the body of the response.
7. `7-status_code.sh`: Sends a request to a URL and displays only the status code of the response.
8. `8-post_json.sh`: Sends a JSON POST request to a URL with the contents of a file and displays the body of the response.
9. `9-catch_me.sh`: Makes a request to a specific URL to trigger a server response.

## Usage
Each script can be run from the command line, passing the necessary arguments as described in the task descriptions.
