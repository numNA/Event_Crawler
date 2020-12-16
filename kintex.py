''' https://www.kintex.com/client/c010101/c010101_00.jsp?sField=&sWord=&eventClCode=&prmtrNm=&koreanEventNm=&searchType=period&periodSYear={year}&periodSMonth={Smonth}&periodEYear=2020&periodEMonth=12&cPage={page}

f"https://www.kintex.com/client/c010201/c010203_00.jsp?sField=&sWord=&eventClCode=&prmtrNm=&koreanEventNm=&searchType=period&periodSYear={year}&periodSMonth={Smonth}&periodEYear={year}&periodEMonth=12&cPage={page}"
 '''

import re
import requests
from bs4 import BeautifulSoup
from datetime import date
from dateutil.relativedelta import relativedelta

today = date.today()
edate = today + relativedelta(months=+2)

Syear = str(today.year)
Smonth = str(today.month)
Eyear = str(edate.year)
Emonth = str(edate.month)

title = []
period = []
url = []
events = []


def get_events():
    last_p = int(extract_pages())
    for pg in range(last_p):
        print(f"Scrapping KINTEX page {pg+1}")
        page = pg+1
        URL = f"https://www.kintex.com/client/c010101/c010101_00.jsp?sField=&sWord=&eventClCode=&prmtrNm=&koreanEventNm=&searchType=period&periodSYear={Syear}&periodSMonth={Smonth}&periodEYear={Eyear}&periodEMonth={Emonth}&cPage={page}"

        result = requests.get(f"{URL}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find("div", {"class": "schedule"}).find_all("tbody")
        # print(results)
        # print(results)
        # print(results[1])

        for result in results:
            extract_events(result)

    for i in range(len(title)):
        event = copy_events(i)
        events.append(event)
    # print(events)
    return events


def extract_pages():
    URL = f"https://www.kintex.com/client/c010101/c010101_00.jsp?sField=&sWord=&eventClCode=&prmtrNm=&koreanEventNm=&searchType=period&periodSYear={Syear}&periodSMonth={Smonth}&periodEYear={Eyear}&periodEMonth={Emonth}&cPage=1"
    kintex_res = requests.get(URL)
    kintex_soup = BeautifulSoup(kintex_res.text, 'html.parser')
    pgl = kintex_soup.find("ul", {"class": "paging"})

    pages = []
    for pg in pgl:
        pages.append(pg.text)

    max_page = pages[-3]

    return max_page


def extract_events(html):
    title_sp = html.find_all("td", {"class": "subject"})

    period_li = html.find_all("td")
   # print(period_li)

    url_sp = html.find_all("a")
    # print(len(url_sp))
    # print(url_sp)

   # for per in period_li:
   #   print(per["td"])

    for i in range(len(period_li)):
        if i % 5 == 2:
            # print(period_li[i].text.strip())
            period.append(period_li[i].text.strip())
    for i in range(len(title_sp)):
        title.append(title_sp[i].text.strip())
    for i in range(len(url_sp)):
        if i % 2 == 1:
            # print(url_sp[i]["href"])
            url.append(url_sp[i]["href"])
        #print("print url")
        #print(url, len(url))

    #print(period, title, url, len(period), len(title), len(url))


def copy_events(i):
    place = 'KINTEX'
    title_sp = title[i]
    period_li = period[i]
    price_li = None
    url_sp = f"https://www.kintex.com/client/c010101/{url[i]}"
    #print(title_sp, period_li, price_li, url_sp)
    return {'place': place, 'title': title_sp, "period": period_li, 'price': price_li, "url": url_sp}
