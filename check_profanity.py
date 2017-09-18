import urllib
'''
Output file content to console.
Check whehter there is bad world by using some web service
'''
file_path = "movie_quotes.txt"

def read_text():
    quotes = open(file_path)
    contents = quotes.read()
    print type(contents) # this is a string
    print contents
    quotes.close()
    return contents

def check_profanity(text):
    conn = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    response = conn.read()
    print(response) #false
    conn.close
    return response

content = read_text()
response = check_profanity(content)

if "true" in response:
    print "There are some bad words!"
else:
    print "There are no bad words"
