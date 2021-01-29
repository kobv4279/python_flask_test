from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

def kj():
    req = requests.get('http://www.gen.go.kr/xboard/board.php?mode=list&tbnum=32&addUrlQuery=&sCat=')
    soup = BeautifulSoup(req.text,'html.parser')
    title = soup.findAll('td', attrs={'class': 'left subject'})

    kj_sub_list = []
    kj_ref_list = []
    for i in title:

        sub = i.a.text

        kj_sub_list.append(str(sub))
        ref = i.find("a")["href"]

        ref_= "http://www.gen.go.kr/xboard/" + ref
        #print(ref_)
        kj_ref_list.append(ref_)

   # http: // www.gen.go.kr / xboard / board.php?mode = view & number = 378639 & tbnum = 32 & sCat = 0 & page = 1 & keyset = & searchword =

    return kj_sub_list, kj_ref_list
