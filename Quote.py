from bs4 import BeautifulSoup
import requests
import openpyxl


url = 'https://test-scrape-site.onrender.com/quotes.html'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('h1')
    quotes = soup.find_all('figure')


    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Quotes'


    ws.append(['Title', 'Quote'])


    for title in titles:
        for quote in quotes:
            cleaned_quote = quote.text.strip().replace('\n', ' ')
            ws.append([title.text.strip(), cleaned_quote])


    wb.save('quotes.xlsx')
    print('Data saved to quotes.xlsx')
else:
    print(f'Failed to retrieve the page.')
