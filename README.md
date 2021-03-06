# TalkMakerToEpub

by 神楽坂らせん version 0.003

トークメーカーのストーリー（エピソード）をEPUB化します。

今のところは、吹き出しとしてではなく、キャラの画像のわきに回り込みテキストでセリフを流し込む仕様です。

## 環境

開発＆試験環境は

* MacOS HighSierra 10.13.3
* Python 3.6.2
   * Pythonのモジュール
   * beautifulsoup4
   * requests

### あるといいもの

* Sigil 0.9.7

## インストールとか

Pythonは適当にいれてください。（Version 3.6以上）

beautifulsoupのインストールは

>$ pip install beautifulsoup4

でOK。
あ、requestsも入れないとおこられるかも。

>$ pip install requests

してあげてください。

## 使い方

>python TalkGet.py [URL] [File]

で指定したURLのトーク（エピソード）をEPUB用のxhtmlとして取得し、/Textフォルダに[File]として保存します。

URLを省略すると「もしも敬虔な女子高生が〈神は死んだ〉のニーチェ作『ツァラトゥストラ』を読んだなら」の表紙ページ（ https://talkmaker.com/works/e39da839e2d4cf3d1706b528d846e7ba.html ）を取得します。（Fileのデフォルトはtext01.xhtml)

作成されたxhtmlファイルをSigilのファイル->追加で追加すると、Epubファイル化することができます。画像ファイル等も自動的に読み込んでくれます（どちらかと言うとSigilが偉い）

>python allStorys.py [URL]

URLで指定した目次ページにある全ストーリーを一気にやります、TEXT0001.xhtmlからの連番で取得。
URLを指定しないと、『もしトラ』の目次ページ（ https://talkmaker.com/works/e39da839e2d4cf3d1706b528d846e7ba.html ）からもってきます。
サーバーの負荷対策で各ストーリーごとに５秒間停止します。（途中でキャンセルはそのタイミングでCTRL+Cしてください）

### 現状の問題点
* 複数のストーリーの一括取得と同時に目次も生成したいけれど手付かず。


