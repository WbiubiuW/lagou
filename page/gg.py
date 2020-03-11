


msg = """lastCity=101280600; __c=1583668618; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1582983683,1583027130,1583068146,1583668618; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1583668618; __l=l=https%253A%252F%252Fwww.zhipin.com%252Fshenzhen%252F&r=&friend_source=0&friend_source=0; __a=89382694.1583034028.1583068146.1583668618.14.3.2.14; __zp_stoken__=37d42ghx1R5ZzdXy9ENcsMnad14ZSN1jQwE26p2pgGiLkSdjWmJr1F5t0brFCFWT1NJqKALsR94NnsVVmUjS34Swg%2Bns8TH840FSzyCxgjbzSPQ6nFLKXQ5estbnlxPOLflR"""

cookie = {}
for i in msg.split(";"):

    cookie[i.split("=")[0]] = i.split("=")[1]
    print(cookie)

