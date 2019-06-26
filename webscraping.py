import requests
import bs4

upperBound = ""
lowerBound = ""

res = requests.get('https://www.instagram.com/xavier_v_tandova/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
meta_tag = soup('meta', property="og:description")
meta_data = soup.find("meta", property="og:description")
content = meta_tag[0].content
print(meta_data["content"])

# og:description