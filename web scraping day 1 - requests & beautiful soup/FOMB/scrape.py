from bs4 import BeautifulSoup

documents = []
with open('site.html', 'r') as file:
	soup = BeautifulSoup(file, 'html.parser')
	table = soup.find('table', {'id': 'docsDataTable'})
	rows = table.find_all('tr')
	for row in rows:
		cells = row.find_all('td')
		if len(cells) == 5: # Line added to filter out empty/malformed table rows
			document = {"title": cells[0].text, "link": cells[4].find('a')['href']}
			documents.append(document)

output_file = 'links.txt'

for document in documents:
	doc_link = document.get('link')
	with open(output_file, 'a') as file:
		file.write(f'{doc_link}\n')