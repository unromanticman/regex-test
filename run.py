#!/usr/bin/python
# -*- coding: UTF-8 -*- 
 
import re
import os.path

path = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(path, "./page.html")

file = open(file_path, "r") 

content = file.read() 

match = re.findall(r'<tr class=[^>]*>([\s\S]*?)</tr>', content)

for item in match:
	o = re.findall(r'<td[^>]*>(.*?)</td>', item)
	print str(o).decode('string_escape')