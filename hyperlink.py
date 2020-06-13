import urllib.request, urllib.error

print("Welcome to Hyperlink Checker, please provide the hyperlink below.")
url = input()
try:
    conn = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    # Returns the particular error in the code (e.g. 404, 501, ...)
    print('There seems to be an error with the page: HTTPError: {}'.format(e.code))
except urllib.error.URLError as e:
    # Not an HTTP-specific error (e.g. connection refused)
    print('There seems to be an error with the page: URLError: {}'.format(e.reason))
else:
    # 200
    print('Hyperlink looks good! ')


 
