import os
import requests

from flask import Flask, request
from flask_discord_interactions import DiscordInteractions, Message, Embed, embed

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

# @discord.command()
# def check_balance(ctx):
#     "This should get the balance from the pv"

#     ctx.accon
#     r = requests.get("http://52.52.160.149/accounts/0067a4d2b153f62041a9cca5454aebd06ea1d0827828da889ddaad991d077401/balance?format=json")
#     print(r.json())
#     return "Check balance"

@discord.command()
def help(ctx):
    "Help Message for using the bot"

    return Message(embed = Embed(
        title = "Help",
        description = "Help description",
        fields=[
            embed.Field(
                name= "Command: `/check_balance`",
                value= "Responds with Pong!"
            )
        ]
    ))

@app.route('/', methods=["GET"])
def hello_world():
    return "Hello World"

discord.set_route("/api/interactions")
discord.update_commands()

if __name__ == "__main__":
    app.run(debug=True)