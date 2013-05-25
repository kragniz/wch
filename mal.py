import urllib2, base64
def search():
    url = 'http://myanimelist.net/api/anime/search.xml?q=gosick'

    request = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (username,
                                                  password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)   
    result = urllib2.urlopen(request)
    return result.read()

import xml.etree.ElementTree as ET
p = search().replace('&', '')
root = ET.fromstring(p)
for child in root:
    for s in child:
        print s.tag, ':', s.text
    print '-'*100
