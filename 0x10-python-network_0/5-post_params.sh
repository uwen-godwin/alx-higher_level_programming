#!/bin/bash
#sends a POST request to the passed URL,displays the body of the response
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
