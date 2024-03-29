#!/usr/bin/python3
""" script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    """encode email as a parameter"""
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
