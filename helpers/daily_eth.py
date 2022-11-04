import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'slug': 'ethereum',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('CRYPTO_API_KEY'),
}


async def daily_eth(bot):
    req = requests.get(url, headers=headers, params=parameters)
    content = json.loads(req.text)
    dicc = list(content['data'].values())[0]
    crypto = dicc['name']
    price = dicc['quote']['USD']['price']
    percent_change = dicc['quote']['USD']['percent_change_24h']
    percent_change = round(percent_change, 2)
    message = f"{crypto.capitalize()} price is {round(price, 2)}$ now."
    if percent_change > 0:
        message += f" It has increased {percent_change}% in the last 24 hours."
    else:
        message += f" It has decreased {percent_change * -1}% in the last 24 hours."
    channel = bot.get_channel(1032968458964586526)
    await bot.wait_until_ready()
    await channel.send(message)
