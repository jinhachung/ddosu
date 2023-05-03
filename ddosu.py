import os
import requests
from datetime import date

def str_no_num(s):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for num in nums:
        if num in s:
            return False
    return True

def print_without_numbers_if_has_numbers(s):
    r = s.split("(")[0].strip()
    if r == "":
        return
    print(r)

def main():
    # get date
    today = date.today()
    d = today.strftime("%Y-%m-%d")
    url = "https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=emp&stt_dt=" + d
    r = requests.get(url, allow_redirects=True)
    print("Downloading request items' information on: {}".format(d))

    # save content with name
    f = open(str(d), "wb")
    f.write(r.content)
    f.close()
    f = open(str(d), "r")
    lines = f.readlines()
    f.close()
   
    # set which words we wish to leave out
    filter_words = ["kcal", "그린샐러드"]

    menu = [[], []]
    p = False
    ind = 0
    for l in lines:
        should_append = True
        # printing --> check if we keep printing
        if p:
            if "</ul>" in l:
                p = False
                ind = 1
            else:
                for w in filter_words:
                    if w in l.lower():
                        should_append = False
                if should_append:
                    menu[ind].append(l)
                p = True # redundant
        # not printing --> check if we start printing
        else:
            if ("list-1st" in l) and ("!" not in l):
                p = True
            else:
                p = False
    
    print("Lunch: ")
    for m in menu[0]:
        _m = m.strip().strip("<br/>")
        # replace values if necessary
        _m = _m.replace("&lt;", "<").replace("&gt;", ">")
        if (str_no_num(_m)) and (len(_m) > 0):
            print(_m)
        else:
            print_without_numbers_if_has_numbers(_m)

    print("\nDinner: ")
    for m in menu[1]:
        _m = m.strip().strip("<br/>")
        # replace values if necessary
        _m = _m.replace("&lt;", "<").replace("&gt;", ">")
        if (str_no_num(_m)) and (len(_m) > 0):
            print(_m)
        else:
            print_without_numbers_if_has_numbers(_m)
    
    os.remove(str(d))

if __name__ == "__main__":
    main()
