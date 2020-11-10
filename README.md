# roulette-bot

slack roulette bot

## できること

slackで任意のリストからランダムに抽選結果を返します
あとping代わりに返事します

## 使い方

HUBOTを作成し、HUBOT_API_TOKENを取得しておいてください
対象チャンネルにhubotを招待しておいてください
bot名は任意ですが、下記例では @nagatto-chan としています

### 起動

cd roulette-bot
python3 run.py

### 終了

cmd + c / ctl + c

### レスポンス

@nagatto-chan roulette
--> 川田、山田、スズキ、のいずれかが抽選されます

@nagatto-chan ping
--> pong! が返却されます
