from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup





#opening up connection and grabbing the page.


url = "https://fsbo.com/"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")


#finding list
listing = page_soup.findAll("ul",{"class":"home-listings"})
test1 = listing[0]
test2 = test1.findAll("li")

x=[]
for i in test2:
	x.append(i.a["href"])

	


#passing link to gather contacts
for j in x:
	my_url =j
	

	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	#html parsing
	page_soup = soup(page_html, "html.parser")


	#grabs each property
	container = page_soup.findAll("div",{"class":"col-md-4 col-xs-12 property-details-right"})
	

	for containers in container:
		owner_name = containers.findAll("div",{"class":"col-md-10 col-xs-12"})

		owner_Name = "".join((owner_name[0].text).strip())
		
		if(len(owner_Name[1])>15):
			contact_No = "1-800-690-5802"
		else:
			contact_No = "".join((owner_name[1].text).strip())



	print("Owner_Name: " + owner_Name)
	print("Contact_No:  " + contact_No)
	

 