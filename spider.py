#Fetch Web page's a element,and print
import HTMLParser, urllib

class linkParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag=='a':
            self.links.append(dict(attrs)['href'])

htmlSource = urllib.urlopen("http://www.baidu.com/index.html").read(200000)
p = linkParser()
p.feed(htmlSource)
for link in p.links:
    print link