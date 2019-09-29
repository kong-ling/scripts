from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #if 'td' in tag or 'tr' in tag:
        if 'table' in tag:
            print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        if 'table' in tag:
            print "Encountered an end tag :", tag

    def handle_data(self, data):
        if data is '\n\r':
            pass
        elif data is ' ':
            pass
        else:
            print "Encountered some data  :>%s<" % data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

htm = open('cps_cu_s.html', 'r')

parser.feed(htm.read())
