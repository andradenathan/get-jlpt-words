from bs4 import BeautifulSoup
from requests import get

file = open("words.txt", "w")

gojuon = [
    "あ行", "か行", "さ行", 
    "た行", "な行", "は行", 
    "ま行", "や行", "ら行", "わ行"
]

for gyou in gojuon:
    page = get(f"https://en.wiktionary.org/wiki/Appendix:JLPT/N2/{gyou}").content
    soup = BeautifulSoup(page, "html.parser")
    words = soup.find("div", {"class": "mw-parser-output"}).text
    file.write(words)

print("All words were exported from Wikipedia successfully")
exit(0)