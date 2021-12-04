# discord bot test on deta

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/wakawakathedev/deta_discord_bot)

### description

This is a a serverless discord bot using `flask` and `flask_discord_interactions`.


### clone deta project
```
$ deta new --node discord_test_bot
```

### Set your env with deta cli

1. Create .env with discord tokens
2. deploy updated env variables with the command below

```
$ deta update -e .env
```

### How to deploy
```
deta deploy
```

### update your discord interactions url with the deta_url

e.g.

if your deployed app is `https://example.deta.dev` use `https://example.deta.dev/api/interactions`


### how to run locally

```
pip install -r requirements.txt 
python3 main.py
```


### License
MIT

### author
wakawakathedev <wakawakathedev@gmail.com>