import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text, "html.parser")
# print(soup.find(id="up_34061511"))
# print(soup.title)

title = soup.select(".titleline")
subline = soup.select(".subtext")

# print(title.find("a"), vote.select(".id"))

def sort_by_votes(votes):
    return sorted(votes, key= lambda k: k["vote"], reverse=True)


def create_custom_hn(links,subline):
    # print(links[0].find("a").get("href"))
    hn = []
    for idx,title in enumerate(links):
        title = links[idx].getText()
        href = links[idx].find("a", None).get("href")
        votes = subline[idx].select(".score")
        if(len(votes)):
            vote = int(votes[0].getText().replace(" points",""))
            if(vote > 99):
                hn.append({"title": title, "vote": vote, "href": href})
    return sort_by_votes(hn)

pprint.pprint(create_custom_hn(title,subline))