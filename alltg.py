# -*- coding:utf-8 -*-
#import subprocess
##from Tget import tgmain
import sys
import codecs
import os
import requests , bs4
from time import sleep

"""
全ストーリーまるっとゲットしちゃうプログラムです。
諸元を読み込んで逐次Tget.pyに丸投げする感じです。
"""



def tocGet(url):
    """ 目次を取得 """
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    print(soup.title)

    tt = soup.h3
    print(tt.text)

    tocSrc = soup.find("ul",class_="episode")
    #print(tocSrc)
    storyNo=0
    for a in tocSrc.select('li > a'):
        txt=str(a.text)
        st=txt.find("更新日")
        txt2=txt[:st]
        print(txt2)
        b=a['href']
        if b:
            storyNo = storyNo + 1
            print(b)
            storyUrl = 'https://talkmaker.com'+str(b)
            ##subprocess.call("TG1.py",storyUrl,'text'+'{0:04d}'.format(storyNo) +'.xhtml')
            strg='text'+'{0:04d}'.format(storyNo) +'.xhtml'
            maketxt(storyUrl,'text'+'{0:04d}'.format(storyNo) +'.xhtml')
            print("ーーーーー５秒間停止中ーーーーーー")
            sleep(5) #５秒スリープ
    print("ーーーーー　終了　ーーーーーー")



def maketxt(makestory,mkhtml):
    argc = len(makestory)
    if(argc < 2):
        #指定なければ鉄研ページを取得URL
        ###https://talkmaker.com/works/episode/4c6bb92161b897ea0521474b0863662f.html','worktext.dat')
        ##https://talkmaker.com/works/episode/0c2cf55f68348d46a426706c77884faf.html
        file = codecs.open('workurl.dat' ,'w','utf-8')
        file.write('https://talkmaker.com/works/episode/4c6bb92161b897ea0521474b0863662f.html')
        file.close()
        file = codecs.open('workname.dat' ,'w','utf-8')
        file.write(mkhtml)
        file.close()
    else:
        #argcが２以上なら、指定URLを指定fileに保存(今のところ１つだけ)
        ##TalkGet(argvs[1],argvs[2])
        file = codecs.open('workurl.dat' ,'w','utf-8')
        file.write(makestory)
        file.close()
        file = codecs.open('workname.dat' ,'w','utf-8')
        file.write(mkhtml)
        file.close()
    import subprocess
    subprocess.call("python TG1.py")
    subprocess.call("python TG2.py")



if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    #setDir()
    print(argc)
    if(argc != 2):
        #指定なければもしトラ全取得URL
        tocGet('https://talkmaker.com/works/775a2a585e0def77a993316d61ec594b.html')

    else:
        #argcが２以上なら、指定URL
        tocGet(argvs[1])


#######


#print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する
