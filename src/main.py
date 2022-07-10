from bs4 import BeautifulSoup
from requests import get
from sys import argv

def populate(filename: str, jlpt_level: str = 'N5') -> None:
    file = open(filename, "w")

    gojuon = [
        "あ行", "か行", "さ行", 
        "た行", "な行", "は行", 
        "ま行", "や行", "ら行", "わ行"
    ]

    for gyou in gojuon:
        page = get(f"https://en.wiktionary.org/wiki/Appendix:JLPT/{jlpt_level}/{gyou}").content
        soup = BeautifulSoup(page, "html.parser")
        words = soup.find("div", {"class": "mw-parser-output"}).text
        file.write(words)

def search_word(filename: str, word: str) -> None:
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        if word not in line:
            continue

        print(line)
    
def main() -> None:
    print("Choose between:\n[-1] - Exit\n[0] - Populate\n[1] - Search word meaning")
    option = int(input("Your option is: "))

    if option == -1:
        exit(0)

    if option == 0:
        populate(argv[1], argv[2])
        print("All words were exported from Wikipedia successfully")
        exit(0)

    if option == 1:
        word = input("Enter the word: ")
        search_word(argv[1], word)
        exit(0)
main()