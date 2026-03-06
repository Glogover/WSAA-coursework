# This program converts a web page to a PDF file
# This is to demonstrate API keys
# Author: Marcin Kaminski

import requests # for making HTTP requests
import urllib.parse # for URL encoding
from config import apikeys as cfg # we import the API keys from a separate config file for better security and organization

#targetUrl = "https://en.wikipedia.org" # this is the web page we want to convert to PDF
targetUrl = "https://example.com/" # you can change this to any web page you want, but make sure it is a valid URL and that the API can access it (some websites may block requests from certain sources)

apikey = cfg["htmltopdfkey"] # we get the API key from the config file
# you can get a free API key from https://html2pdf.app/ (limited to 100 conversions per month and 1 MB file size, but you can upgrade to a paid plan for more conversions and larger file sizes)

apiurl = "https://api.html2pdf.app/v1/generate"  # this is the API endpoint for generating PDF files from web pages

params = {"html": targetUrl, "apiKey": apikey} # these are the parameters we need to send to the API: the URL of the web page and our API key
parsedparams = urllib.parse.urlencode(params) # we need to URL-encode the parameters to make sure they are properly formatted for the HTTP request

requestUrl = apiurl + "?" + parsedparams # this is the full URL we will use to make the HTTP request to the API, including the parameters
print(requestUrl) #print the request URL to the console for debugging purposes

response = requests.get(requestUrl) # make the HTTP GET request to the API and store the response in a variable

print(response.status_code) # print the HTTP status code of the response to the console for debugging purposes

result = response.content # the content of the response is the PDF file in binary format, so we store it in a variable

with open ("document.pdf", "wb") as handler: # we open a new file called "document.pdf" in binary write mode
    handler.write(result) # we write the content of the response (the PDF file) to the new file

