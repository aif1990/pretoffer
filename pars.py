import urllib2
import re
import json
import BeautifulSoup
        
siteZara = urllib2.urlopen('http://www.zara.com/webapp/wcs/stores/servlet/category/uk/en/zara-W2011-r/178003/Collection')

itemsZara = re.search('categoryData: {"items":(.*\]),',siteZara.read()).groups()

itemsZara = json.loads(itemsZara[0])

for item in itemsZara:
    print json.dumps(item, sort_keys=True, indent=4)
    print "---------"


siteMango = urllib2.urlopen('http://shop.mango.com/GB/mango/clothing/dresses')
        
siteMango = BeautifulSoup.BeautifulSoup(siteMango)

itemsMango = siteMango.find(id='iteradorPrendas')

#print itemsMango.prettify()

for row in itemsMango:
    for box in row:
        if box.table: 
            box = box.table
            title = box.findAll('span', {'id':re.compile('.*iteradorPrendas:\d+:.*'),'class':'txt7'})[0].text
            price = box.findAll('span', {'class':re.compile('txt8B|txt7'), 'id':None})
            print price
            print "$$$$$$"
            
