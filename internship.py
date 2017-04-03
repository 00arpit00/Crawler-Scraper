import requests
from bs4 import BeautifulSoup
main_url='https://www.carwale.com'
url = '/marutisuzuki-cars/wagonr10/lxi-2783/'
print(main_url+url)
response = requests.get(main_url+url).text
#print(type(response))
soup = BeautifulSoup(response,'html.parser')
#print(soup.prettify())
file_2_print = open('output.txt','w')
content = soup.find_all('div',class_='mid-box')
for types in content[1:]:
	heading = types.find('h2').text
	print(heading,file=file_2_print)
	if 'Technical' in heading:  # For technical features
		for tables in types.find_all('table'):


			if tables.th.div==None:

				print(tables.th.text,file=file_2_print)
				#pass
			else:
				
				print('Engine & Transmission',file=file_2_print)
			for tags in tables.find_all('tr'):
				if 'Wheels' in tags.text:
					print('Wheels & Tyres',file=file_2_print)
				print(tags.text,file=file_2_print)
	else:
		for tables in types.find_all('table'):     # for standard features


			if tables.th.div==None:
				#print(tables.th.text,file=file_2_print)
				pass
			else:
				
				print('Engine & Transmission',file=file_2_print)
			for tags in tables.find_all('tr'):
				print(tags.text,file=file_2_print)
try_links=soup.find_all('ul',id='lstOtherVersions')
#print(try_links)
'''for linking in try_links:
	print(linking.find('li'))'''
links=[]
for linking in try_links:
	linking=linking.find_all('li')
for link in linking:
	links.append(link.a['href'])
#print(links)
i=1
for url in links:
	print(main_url+url)
	response = requests.get(main_url+url).text
	#print(type(response))
	soup = BeautifulSoup(response,'html.parser')
	#print(soup.prettify())
	file_2_print = open('output'+str(i)+'.txt','w')
	content = soup.find_all('div',class_='mid-box')
	for types in content[1:]:
		heading = types.find('h2').text
		print(heading,file=file_2_print)
		if 'Technical' in heading:  # For technical features
			for tables in types.find_all('table'):


				if tables.th.div==None:

					print(tables.th.text,file=file_2_print)
					#pass
				else:
					
					print('Engine & Transmission',file=file_2_print)
				for tags in tables.find_all('tr'):
					if 'Wheels' in tags.text:
						print('Wheels & Tyres',file=file_2_print)
					print(tags.text,file=file_2_print)
		else:
			for tables in types.find_all('table'):     # for standard features


				if tables.th.div==None:
					#print(tables.th.text,file=file_2_print)
					pass
				else:
					
					print('Engine & Transmission',file=file_2_print)
				for tags in tables.find_all('tr'):
					print(tags.text,file=file_2_print)
	i+=1
#heading = content[2].find_all('h2')[0].text
#print(heading)
#print(len(content[2].find_all('td')))