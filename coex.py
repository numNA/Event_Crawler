import requests
from bs4 import BeautifulSoup
from datetime import date
from dateutil.relativedelta import relativedelta

today = date.today()
edate = today + relativedelta(month=7)
today = today.isoformat()
edate = edate.isoformat()
page = 1
events =[]
'''f"http://www.coex.co.kr/event-performance/total-schedule-2/page/{page}?type=visitor&sv&period=six_month&search_sdate={today}&search_edate={edate}"

http://www.coex.co.kr/event-performance/total-schedule-2/page/2?type=visitor&sv&period=six_month&search_sdate=2020-01-31&search_edate=2020-07-31

f"https://www.coex.co.kr/blog/event_exhibition/page/{page}?list_type=list&sv&period=six_month&search_sdate={today}&search_edate={edate}"'''


def get_events():
  
  last_p = extract_pages()
  for pg in range(last_p):
    print(f"Scrapping COEX page {pg+1}")
    page = pg+1
    URL = f"http://www.coex.co.kr/event-performance/total-schedule-2/page/{page}?type=visitor&sv&period=six_month&search_sdate={today}&search_edate={edate}"
    result = requests.get(f"{URL}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("ul",{"class":"info"})
    #print(results)

    for result in results:
      event=extract_events(result)
      events.append(event)
      #print(events)
  #print(events)
  return events
    

def extract_pages():
    URL = f"http://www.coex.co.kr/event-performance/total-schedule-2/page/{page}?type=visitor&sv&period=six_month&search_sdate={today}&search_edate={edate}"
    coex_res = requests.get(URL)
    coex_soup = BeautifulSoup(coex_res.text, 'html.parser')
    pgl = coex_soup.find_all("a", {"class": "page larger"})
    
    pages = []
    for pg in pgl:
        pages.append(int(pg.string))

    max_page = pages[-1]
    #print(max_page)
    return max_page


def extract_events(html):
    place = 'COEX'
    #print(html)
    title_sp = html.find("span", {"class": "subject"}).string
    period_li = html.find("li",{"class":"period"}).text

    if html.find("li",{"class":"price"}) is None:
      price_li = None
    else:
      price_li = html.find("li",{"class":"price"}).text

    if html.find("span", {"class": "url"}) is None:
      url_sp = None
    else:
      url_sp = html.find("span", {"class": "url"}).string
   
    return {'place': place,'title': title_sp, "period": period_li,'price':price_li,"url":url_sp}
    
