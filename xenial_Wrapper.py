__name__= "xenial_wrapper"

import sys, os, glob

try:
	folder = sys.argv[1]
except:
	print "need a clear directory like:\n/usr/share/background/"

intro="""<background>
  <starttime>
    <year>2009</year>
    <month>08</month>
    <day>04</day>
    <hour>00</hour>
    <minute>00</minute>
    <second>00</second>
  </starttime>
<!-- This animation will start at midnight. -->\n"""

picture1 = ""
glob_Arr =[]
picture_list = glob.glob(folder+"*")

for picture2 in picture_list:
	if picture1 != "":
		pawns="""<static>
    <duration>1795.0</duration>
    <file>"""+picture1+"""</file>
  </static>
  <transition>
    <duration>5.0</duration>
    <from>"""+picture1+"""</from>
    <to>"""+picture2+"""</to>
  </transition>\n"""
  		glob_Arr.append(pawns)
  	else:
  		picture1 = picture2

xml= intro + "".join(glob_Arr) +"</background>"

print xml

f = open("xenial.xml","w")
f.write(xml)
f.close()
