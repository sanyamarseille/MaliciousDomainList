# MaliciousDomainList

このツールは以下のサイトで公開されている悪意あるURL情報を取得し、保持するためのツールです。  
データの詳細情報はサイトで確認してください。

## データソース

|サイト名|URL|
|---|---|
|URLhaus|https://urlhaus.abuse.ch/downloads/csv/|
|Malwaredomains|http://mirror1.malwaredomains.com/files/domains.txt|

## データフォーマット

### URLhaus
|フィールド|データ|
|---|---|
|field[0]|ID|
|field[1]|dateadded|
|field[2]|URL|
|field[3]|URL status|
|field[4]|threat|
|field[5]|tags|
|field[6]|urlhaus_link|

### Malwaredomains
フィールドはタブ区切りとなっています。
|フィールド|データ|
|---|---|
|field[0]|blank|
|field[1]|blank|
|field[2]|domain|
|field[3]|type|
|field[4]|original_reference-why_it_was_listed|
|field[5]|databaseadded|
