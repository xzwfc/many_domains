import pandas 
import os
import time
from urllib.request import urlopen, Request
from tld import get_tld, get_fld #remove sub domain

if not os.path.exists ("domain_html"):
	os.mkdir("domain_html")
df = pandas.read_csv("domains.csv")


for link in df["domain_name"]:
	f=open("domain_html/" + link, "wb")
	try:


	    print ("downloading:", link)
	    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'} #google url header to fake it like a human
	    request_link="http://www." + link
	    req =Request(url=request_link, headers=headers)
	    
	    response =urlopen(req)
	    html =response.read()
	    f.write(html)
	except:
		print ("downloading 2nd: ", link)
	    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'} #google url header to fake it like a human
	    request_link="http://" + link #try except for the domain without www.
	    req =Request(url=request_link, headers=headers)
	    
	    response =urlopen(req)
	    html =response.read()
	    f.write(html)
	f.close()
	time.sleep (10)




# if not os.path.exists ("domain_html"):
# 	os.mkdir("domain_html")
# df = pandas.read_csv("domains.csv")
# for link in df["domain_name"]:
# 	print(get_fld("http://" + link)
# 	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'} #google url header to fake it like a human
# 	fld_link =get_fld("http://") # new one for getting rid of the sub domain alert
# 	request_link="http://www." + fldlink
# 	req =Request(url=request_link, headers=headers)
# 	response =urlopen(req)
# 	html =response.read()
# 	f.write(html)

