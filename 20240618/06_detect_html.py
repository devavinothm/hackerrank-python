

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print("->", ele[0], ">", ele[1])

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print("->", ele[0], ">", ele[1])

parser = MyHTMLParser()

n = int(input())

for i in range(n):
    parser.feed(input())
parser.close()