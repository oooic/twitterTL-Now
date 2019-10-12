# twitter-TL上の話題解析プログラム
twitterAnalyze_example.jpegのような画像を作るプログラムです。
## 使ったモジュール
- mecab(形態素解析ツール)
- wordcloud(単語をカウントして画像化)
- PIL(画像を開く)
- numpy(画像データを配列化する)
- python-twitter(ツイートする、データを取得する)

## 使う際に必要なもの
twitterDeveloperAPI
申請(英語)が必要です！ツイッター上からデータを取得するのに必要です。あると色々できていいよ。config.pyに入れてあります。（今回はセキュリティ上の観点から公開してません。)
あとは、青空文庫データベースとかが無料で公開されているツールです。

## 実際のコード
twitterAPI->data.py->txtMold.py->mecab.py->makeImage.py->tlNow.png

### data.py
twitterからデータを取ってきて、data.txtに保存する。
また取得できた時間を得て、テキストを付与してtweeetText.txtに保存する。
### txtMold.py
data.txtから文字データを読み込み、正規表現を使ってURL、タグ、メンション、改行、絵文字を除く。data2.txtに保存する。
### mecab.py
data2.txtから文字データを読み込み、mecabというライブラリを使って形態素解析を行う。名詞だけを取り出しdata3.txtに保存する。
(print(keyword)すると元データがみれるよ)
### makeImage.py
data3.txtから文字データを読み込み、wordCloudを用いて表示する。この時、PILで画像を読み込み、numpyで配列化してwordcloudに渡すことで形に成形することができる。
### makeImage2.py
data3.txtから文字データを読み込み、wordCloudを用いて表示する。この時、PILで画像を読み込み、numpyで配列化してwordcloudに渡すことで形に成形することができる。こちらでは、元画像の色も反映させられるようになっている。(hoge.pngにいろいろ入れれば好きにできる)

何日かに分けて作ったので、途中途中でファイルに書き出す感じにしてます。
モジュール使うと色々できるのでドキュメント読むと良さそう。
