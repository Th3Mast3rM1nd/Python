import sys , requests , bs4 

# python Script to pull links from a domain

total_arg = len(sys.argv)


if total_arg <= 1:
    print("Usage : Day11.py https://www.google.com")
    exit()

url = sys.argv[1]
res = requests.get(url)
url_soup = bs4.BeautifulSoup(res.text)
href_element = url_soup.select("a")
for i in range(0,len(href_element)):
    print(href_element[i].get("href"))

