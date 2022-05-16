import os
import requests
from datetime import date

def main():
    # get date
    today = date.today()
    d = today.strftime("%Y-%m-%d")
    url = "https://www.google.com/search?q=usd+to+krw&oq=usd+to+krw"
    r = requests.get(url, allow_redirects=True)
    print("Downloading USD to KRW information on: {}".format(d))

    # save content with name
    f = open(str(d), "wb")
    f.write(r.content)
    f.close()
    f = open(str(d), "r", encoding="ISO-8859-1")
    lines = f.readlines()
    f.close()
    
    found = None
    for line in lines:
        if "BNeawe iBp4i AP7Wnd" in line:
            found = line.split("BNeawe iBp4i AP7Wnd")[2]
            found = found.strip().split("&")[0].split(">")[1]
    if found:
        print(f"1 USD = {found} KRW")
    else:
        print("Cannot find currency info in downloaded file, check line #25 in currency.py")

    # erase dummy file
    os.remove(str(d))

if __name__ == "__main__":
    main()
