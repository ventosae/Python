import urllib.request

def read_text():
    quotes = open("C:\study_files\quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    query = urllib.parse.urlencode({'q': text_to_check})
    url = "http://www.wdylike.appspot.com/?"+query
    connection = urllib.request.urlopen(url)
    output= str(connection.read())
##    print(output)
    if "true" in output:
        print("All good man")
    elif "false" in output:
        print("Something worng")
    else:
        print("Error")
    connection.close()
    
read_text()
