## 🇱🇰 Sri Lankan Government Data Sources for Web-Based Data Collection

| No. | Website / Institution | Type of Data | Suitable Tools | Notes |
|-----|------------------------|--------------|----------------|-------|
| 1 | [Central Bank of Sri Lanka](https://www.cbsl.gov.lk) | Exchange rates, inflation, monetary policy, economic indicators | `requests`, `BeautifulSoup` | Exchange rate tables are static and easy to parse |
| 2 | [Department of Census & Statistics](https://www.statistics.gov.lk) | Labour, population, agriculture, economic reports | `requests`, `BeautifulSoup`, `PyPDF2`, `OCR` | Some reports are in PDF, useful for OCR tasks |
| 3 | [IRCSL](https://www.ircsl.gov.lk) | Insurance statistics, circulars, company lists | `requests`, `BeautifulSoup`, `PyPDF2` | Good for PDF scraping and extracting structured tables |
| 4 | [Colombo Stock Exchange (CSE)](https://www.cse.lk) | Stock prices, company data, announcements | `Selenium` | Dynamic content; use Selenium to interact with dropdowns |
| 5 | [Ministry of Finance](https://www.treasury.gov.lk) | Budget documents, economic policy, reports | `PyPDF2`, `OCR` | Reports are mostly PDF — ideal for document extraction |
| 6 | [PUCSL](https://www.pucsl.gov.lk) | Electricity tariffs, regulations, complaints data | `requests`, `BeautifulSoup` | Website structure is clean and beginner-friendly |
| 7 | [Sri Lanka Customs](http://www.customs.gov.lk) | Trade regulations, duty calculators, circulars | `BeautifulSoup`, `Selenium` | Basic site; data hidden in nested HTML or PDFs |
| 8 | [Elections Commission](https://www.elections.gov.lk) | Election results, turnout, polling info | `BeautifulSoup`, `PyPDF2` | Great for scraping result tables from past elections |
| 9 | [Sri Lanka Ports Authority](http://www.slpa.lk) | Port statistics, maritime notices | `requests`, `BeautifulSoup` | Data includes traffic stats and reports |
| 10 | [National Transport Commission (NTC)](https://www.ntc.gov.lk) | Bus fares, transport schedules, permits | `BeautifulSoup`, `OCR` | Fare tables or route lists available for scraping or OCR |
| 11 | [Sri Lanka Tourism Promotion Bureau](https://www.srilanka.travel) | Tourist arrival statistics, travel advisories, promotional material | `requests`, `BeautifulSoup`, `Selenium` | Includes monthly arrival data tables; some sections are JavaScript-rendered |