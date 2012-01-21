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


siteMango = urllib2.urlopen('http://shop.mango.com/GB/page/mango/clothing/dresses/?n=1')
        
siteMango = BeautifulSoup.BeautifulSoup(siteMango)

print "Mango Dresses \n"

pageNum = 1
while True:
    itemsMango = siteMango.find(id='iteradorPrendas')
    
    for row in itemsMango:
        for box in row:
            if box.table: 
                box = box.table
                oldPrice = None
                title = box.findAll('span', {'id':re.compile('.*iteradorPrendas:\d+:.*'),'class':'txt7'})[0].text
                if (box.findAll('span', {'class':re.compile('txt7'), 'id':None})):
                    oldPrice = box.findAll('span', {'class':re.compile('txt7'), 'id':None})[0].text
                newPrice = box.findAll('span', {'class':re.compile('txt8B'), 'id':None})[0].text
                image = box.findAll('img')[0]
                print "Product: \n"
                print "Title " + title
                print "Image " + image['src']
                if (oldPrice):
                    print "Old Price " + oldPrice + "*****" + "New Price " + newPrice + "\n"
                else:
                    print "New Price " + newPrice + '\n'
                print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ \n"
                
    pageNum += 1
    page = siteMango.findAll('a', {'href':re.compile('GB/page/mango/clothing/dresses/\?n=%d' % pageNum)})
    if page:
        page = page[0]
        newPage = 'http://shop.mango.com/' + page['href']
        print "Getting a new page:", newPage
        siteMango = urllib2.urlopen(newPage)
        siteMango = BeautifulSoup.BeautifulSoup(siteMango)
        print "Processing page"
    else:
        break

print "Everything done"
