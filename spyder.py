from bs4 import BeautifulSoup
import urllib.request as urllib2

#sys.stdout = os.devnull
#sys.stderr = os.devnull

def scrap(k=2):
	url = "https://www.studentnewsdaily.com/archive/daily-news-article/"
	req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	page1 = urllib2.urlopen(req)
	soup = BeautifulSoup(page1)
	links = [a.attrs['href'] for a in soup.find_all("a") if len(a.attrs['href'])>65]
	heads = [a.string for a in soup.find_all("a") if a.attrs['href'].find("daily-news-article")]


	j=0

	for url in links:
		j=j+1
		if j > k+1:
			break;
		desc = ""
		print("\n\n"+str(j)+"-------------------------------------------")
		req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		page = urllib2.urlopen(req)
		soup = BeautifulSoup(page,'html.parser')
		s1 = soup.select("div p")
		s2 = list(soup.find_all(class_="col-md-9 column"))
		for i in s1:
			s = i.get_text()
			if s.startswith("Watch") or s.startswith("About") or s.startswith("Launched in"):
				continue
			desc += str(i.get_text())
		#print(desc)
		#print("\n"+str())

		if j == 1:
			continue

		fileName = "parse/stories/"+str(j-1)+".story"
		with open(fileName, "w") as f:
			f.write(desc)

		headName = "parse/heads/"+str(j-1)+".head"
		with open(headName, "w") as f:
			f.write(str(heads[j-1]))

if __name__ == "__main__":
	scrap()