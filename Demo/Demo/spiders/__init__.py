# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import unicodedata

file =open('itcast_pipeline.json',"r")
str = file.read().encode("utf-8").decode('unicode_escape')


file1 =open('itcast_pipeline.json1','w',encoding='utf-8')
print(str)

file1.write(str)


