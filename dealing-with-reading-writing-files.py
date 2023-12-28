#script below read a txt file from a directory/folder and search for ftd and replace it with dev1 and put results in a new file
#also the script search for proflowers ,change shopId with customerId and put it in a diferent file within a directory
import re


path="/mnt/c/Users/salian/Documents/python/text"

with open('path/messages-old.txt') as f:
    items = [item.rstrip() for item in f]
   
with open('/mnt/c/Users/salian/Documents/python/text/orderid.txt', 'w') as orderid_f, open('/mnt/c/Users/salian/Documents/python/text/listid.txt', 'w') as listid_f:
    for item in items:
        if re.search ("ftd",item):
            item=re.sub('dev1','prod1',item)
            orderid_f.write(item + '\n')
            #print (item) 

        if re.search ("proflowers",item):
            item=re.sub('customer','shop',item)
            listid_f.write(item + '\n') 