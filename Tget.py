# -*- coding:utf-8 -*-

import random
import time
import requests, bs4
import urllib.request
import sys
import os
import codecs

"""
    使い方：　python Tget.py [URL] [File]
    URLにあるトークメーカーのストーリーを取得してTextディレクトリにxhtmlページ(file)を作成します。
    自動的に画像も取得します。
    できたxhtmlファイルはSigilにつっこみ、表紙と目次等を追加すればEpub化できます。
    このプログラムからTG1.pyとTG2.pyを呼び出して処理します。
    
"""
#定数的ないろいろ
#改行コード
CR = chr(13)    #Mac

# 不要タグ除去


##if __name__ == '__main__':
def tgmain():
    argvs = sys.argv
    argc = len(argvs)
    argvs = sys.argv
    argc = len(argvs)
    ##setDir()
    print(argc)
    if(argc < 2):
        #指定なければ鉄研ページを取得URL
        ###https://talkmaker.com/works/episode/4c6bb92161b897ea0521474b0863662f.html','worktext.dat')
        ##https://talkmaker.com/works/episode/0c2cf55f68348d46a426706c77884faf.html
        file = codecs.open('workurl.dat' ,'w','utf-8')
        file.write('https://talkmaker.com/works/episode/4c6bb92161b897ea0521474b0863662f.html')
        file.close()
        file = codecs.open('workname.dat' ,'w','utf-8')
        file.write('testxhtml.xhtml')
        file.close()
    else:
        #argcが２以上なら、指定URLを指定fileに保存(今のところ１つだけ)
        ##TalkGet(argvs[1],argvs[2])
        file = codecs.open('workurl.dat' ,'w','utf-8')
        file.write(argvs[1])
        file.close()
        file = codecs.open('workname.dat' ,'w','utf-8')
        file.write('testxhtml.xhtml')
        file.close()
    import subprocess
    subprocess.call("python TG1.py")
    subprocess.call("python TG2.py")


if __name__ == '__main__':
    tgmain()


##print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する
