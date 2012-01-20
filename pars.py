import urllib2
import re
import json
#import BeautifulSoup
        
site = urllib2.urlopen('http://www.zara.com/webapp/wcs/stores/servlet/category/uk/en/zara-W2011-r/178003/Collection')

#site = BeautifulSoup.BeautifulSoup(site)

#scripts = site.findAll('script')

items = re.search('categoryData: {"items":(.*\]),',site.read()).groups()

items = json.loads(items[0])

for item in items:
    print json.dumps(item, sort_keys=True, indent=4)
    print "---------"

#for script in scripts:
 #   script = str(script)
  #  if script.find('categoryData') != (-1):
   #     index = script.find('"items"')
    #    end = script.find('productImageAnimationStepTime')
     #   print script[index:end]
        
        
    
