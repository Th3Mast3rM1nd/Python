import sys , requests , bs4 , re

# python Script to pull links from a domain

total_arg = len(sys.argv)


if total_arg <= 1:
    print("Usage : Day11.py https://www.google.com")
    exit()

def get_links(url):
    list_of_links = []
    res = requests.get(url)
    url_soup = bs4.BeautifulSoup(res.text)
    href_element = url_soup.select("a")
    for i in range(0,len(href_element)):
        link = href_element[i].get('href')
        regex_search = re.compile(r"^https:\/\/\w+\.?\w+\.\w+")
        links = regex_search.findall(str(link))
        list_of_links.append(links)

    return list_of_links

url = sys.argv[1]
list_link = get_links(url)
uniq_link = []
uniq_link1 = []
def uniq_links(links):
    for x in links:
        for y in x:
            uniq_link.append(y)
    for i in uniq_link:
        if i not in uniq_link1:
            uniq_link1.append(i)

uniq_links(list_link)
for link in uniq_link1:
    print(link)
