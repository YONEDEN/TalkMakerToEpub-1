# -*- coding:utf-8 -*-

import random
import time
import requests, bs4
import urllib.request
import sys
import os
import codecs
import shutil

"""
    要らない物を消すだけの補助プログラムです。
    どうしても要らない物はこれで消します。
    2ndtext.datから指定のタグを消して、3rdtext.datを生成。
    それをworkname.datのファイル名で保存します。
"""
#定数的ないろいろ
#改行コード
CR = chr(13)    #Mac

# 不要タグ除去
def divCng():
    #urllib.request.urlretrieve(url,"{0}".format('3rdtext.dat'))#download(url,'work.html')
    file = codecs.open('3rdtext.dat' ,'w','utf-8')
    lineCount = 0
    for Line in codecs.open("2ndtext.dat", "r",'utf-8'):
        lineCount += 1
        Line = Line.replace('<div>','')
        Line = Line.replace('<div class="r mt10 f72">','')
        ##Line = Line.replace('</div>','')
        file.write(Line)
    file.close()



if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    divCng()
    file = codecs.open("workname.dat","r",'utf-8')
    newname = file.read()
    newname2 ='Text/'+newname
    file.close()
    shutil.copyfile('3rdtext.dat','writehtm.dat')
    if os.path.exists(newname2):
        os.remove(newname2)
        os.rename('Writehtm.dat',newname2)
    else:
        os.rename('Writehtm.dat',newname2)


##print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する
