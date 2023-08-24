from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

def extract_tender_data(table_element):
    data_rows = []
    rows = table_element.find_all('tr', class_=["even", "odd"])

    for row in rows:
        row_data = []
        cols = row.find_all('td')
        for col in cols:
            col_text = col.get_text(strip=True)
            row_data.append(col_text)
        data_rows.append(row_data)

    return data_rows

def scrape_and_save_tenders(url, filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        head_row = ['Tender Title', 'Reference No', 'Closing Date', 'Bid Opening Date']
        writer.writerow(head_row)

        tender_tables = soup.find_all('table', id='activeTenders')
        for table in tender_tables:
            tender_data = extract_tender_data(table)
            writer.writerows(tender_data)

    print("Successfully scraped and saved to", filename)

if __name__ == "__main__":
    url = "https://etenders.gov.in/eprocure/app"
    filename = "tender_details.csv"
    scrape_and_save_tenders(url, filename)
