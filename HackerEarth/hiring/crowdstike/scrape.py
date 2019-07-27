import urllib3
from bs4 import BeautifulSoup
from git import Repo
import os

http = urllib3.PoolManager()
url = "hck.re/crowdstrike"
#html = urlopen(url)
html = http.request('GET', url)
print(html.data)
soup = BeautifulSoup(html.data, "lxml")
table = soup.find("table")
headings = [th.get_text() for th in table.find("tr").find_all("th")]
print(headings)
datasets = []
for row in table.find_all("tr")[1:]:
    dataset = dict(zip(headings, (td.get_text() for td in row.find_all("td"))))
    datasets.append(dataset)
print(datasets)


for dataset in datasets:
    repo = Repo.clone_from(dataset['Repo Url'],dataset['Repo Name'])
    git = repo.git
    git.checkout('HEAD', b=dataset['Branch Name'])
    git.branch('another_one')
    
