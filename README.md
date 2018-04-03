# Shiftgenerator (GUI)

## 使い方

### セットアップ
git cloneでこのリポジトリをクローンします。

```
cd ~/GUI_Shiftgenerator  
```  

上のコマンドでクローンしたディレクトリに移動し、以下のパッケージをインストールしてください。

```
# 必要なpythonモジュールのインストール
pip install -upgrade pip
pip install openpyxl

# 必要なnodeモジュールのインストール
npm update -g npm
npm install electron -g
```

これでセットアップ完了です。

### 使用方法

GUI_Shiftgeneratorディレクトリ直下で、以下のコマンドを入力することでアプリが立ち上がります。

```
electron .
```

画面の指示に従い、必要な情報を入力していきます。

全従業員分の情報入力が終了したら、下のボタンをクリックしてください。そうすると完成したExcelファイルがダウンロードできます。
