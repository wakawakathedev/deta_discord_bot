import os

from flask import Flask, request
from flask_discord_interactions import DiscordInteractions

app = Flask(__name__)
discord = DiscordInteractions(app)

app.config["DISCORD_CLIENT_ID"] = os.getenv("CLIENT_ID")
app.config["DISCORD_PUBLIC_KEY"] = os.getenv("PUBLIC_KEY")
app.config["DISCORD_CLIENT_SECRET"] = os.getenv("SECRET")

@discord.command()
def ping(ctx):
    "Respond with a friendly 'pong'!"
    return "Pong!"

@discord.command()
def test(ctx):
    "Respond with I am not a test!"
    return "I am an updated a test!"

@app.route('/', methods=["GET"])
def hello_world():
    return "Hello World"

discord.set_route("/api/interactions")

if __name__ == "__main__":
    app.run(debug=True)