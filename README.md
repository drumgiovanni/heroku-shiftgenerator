# Shiftgenerator (GUI)

読売バイトのシフトを楽に組めるアプリ。

## 使い方

[Shiftgenerator](https://shiftgenerator.herokuapp.com/)の使い方を説明しまーす。

- 最初の画面

![画面の写真](https://github.com/drumgiovanni/heroku-shiftgenerator/blob/master/others/ss1.png)

シフトを組み始めるには「**始めよう**」 , 使い方がわからない場合は「**使い方**」 をクリック！



### シフトの組み方


「始めよう」をクリックすると、以下のような画面になります。

![画面の写真](https://github.com/drumgiovanni/heroku-shiftgenerator/blob/master/others/ss2.png)


画面上部に翌月のカレンダー、及び、祝日・休刊日が表示されます。

画面下部に所属する従業員 ***全員分*** の情報を入力していきます。
手順としては、

1. 名前を入力

1. 属性を選択（平日勤務 or 土日勤務）

1. 休み希望を入力（出勤できない日を **半角数字をコンマ区切り** で入力してください。）  
        ※土日要員は、土日祝の中から出勤できない日を入力してください。(平日は自動的に休みになるようになってます。)

        例） 1,8,15,22
        なお、出勤できない日が無い場合は、何も入力しなくてokです。

1. 一従業員分の情報の記入が完了したら、「登録する」をクリック  
        「登録する」をクリックすると、登録された従業員の情報が表示されます。  
        ※ ミスした場合は、再読み込みしてください。リセットされます。

1. 全従業員の情報の記入が完了したら、「従業員の登録を完了する」をクリック(画面が遷移します。)  
     ![画面の写真](https://github.com/drumgiovanni/heroku-shiftgenerator/blob/master/others/ss3.png)

1. 「ダウンロード」をクリック  
        好きな場所に生成されたエクセルシートを保存できます。  


ここまでの流れを動画にするとこんな感じ⬇︎

![再現映像](https://github.com/drumgiovanni/heroku-shiftgenerator/blob/master/others/mv1.gif)



### 完成したエクセルシートについて

ダウンロードしたエクセルファイルを開いてみましょう。  
※MicrosoftExcelが無い場合、[googleスプレッドシート](https://www.google.com/intl/ja_jp/sheets/about/)が無料で使えて便利（スマホでもアプリをダウンロードすることで使える）

![完成したエクセルシートの画像](https://github.com/drumgiovanni/heroku-shiftgenerator/blob/master/others/ss4.png)

☝︎これが完成したシフトです（全体写すために縮小したら見づらくなっちゃった）。  
見たらわかる通り、土曜日は緑、日曜日・祝日は赤、休刊日は黒塗りになっています。  


画面の下の方を見てもらうと、現在"5月"というタブにいることがわかります。  
このタブでは、完成したシフトを表示しています。  

"workerlist"というタブでは、従業員の勤務可能日が表示されています。  
万が一シフトを変更するとなった際に、参考にできるかと思います。  

"workingday"というタブでは、従業員の出勤日が○・×で表示されています。  
 好きに使ってください。  

![エクセル動画](https://github.com/drumgiovanni/heroku-shiftgenerator/blob/master/others/mv2.gif)

なお、ダウンロードしたエクセルファイルは好きに編集していただいて大丈夫です。  
手入力でシフトの微調整等の柔軟に対応していただければと思います。  


ちなみに、スマホでも使えます。  
スマホで使用する際は、Excelやgoogle spreadsheet等のアプリをインストールしてから使ってください。  

---

あ、もし、土日要員が平日入るシフトを組む場合、以下２通りの方法で対応してください。  

1. 手入力で修正  

1. 属性の項目で平日勤務を選択し、平日・土日祝の中から出勤できない日を休み希望として記入する。  

**以上!!**  

---  



不明点・疑問点があれば以下まで。  

giovannithedev@gmail.com
