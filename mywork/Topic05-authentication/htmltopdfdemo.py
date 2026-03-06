# This program converts a web page to a PDF file
# This is to demonstrate API keys
# Author: Marcin Kaminski

import requests # for making HTTP requests
import urllib.parse # for URL encoding

targetUrl = "https://en.wikipedia.org" # this is the web page we want to convert to PDF

apikiey = "LXVsRthF6WocSPJXxUytgrkpM0x8kONlsdm5lnPry5fsdUfF8WFWI0Y9OG3kLASJ" # you can get a free API key from https://html2pdf.app/ (limited to 100 conversions per month)
apiurl = "https://api.html2pdf.app/v1/generate" # this is the API endpoint for generating PDF files from web pages

params = {"html": targetUrl, "apiKey": apikiey} # these are the parameters we need to send to the API: the URL of the web page and our API key
parsedParams = urllib.parse.urlencode(params) # we need to URL-encode the parameters to make sure they are properly formatted for the HTTP request

requestUrl = apiurl + "?" + parsedParams # this is the full URL we will use to make the HTTP request to the API, including the parameters
print(requestUrl) #print the request URL to the console for debugging purposes
