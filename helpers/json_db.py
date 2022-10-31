import json
import os
from datetime import datetime

import requests
from dateutil import parser
from dotenv import load_dotenv

from utils import mention_id

load_dotenv()
url = 'https://api.jsonbin.io/v3/b/635968a72b3499323beb7dee?meta=false'
headers = {
    'X-Master-Key': os.getenv('JSON_KEY'),
}


def update_counter():
    req = requests.get(url, json=None, headers=headers)
    counter = json.loads(req.text)["counter"]
    counter += 1
    update_json = json.loads(req.text)
    update_json["counter"] = counter
    requests.put(url, json=update_json, headers=headers)
    return counter


def reset_counter():
    req = requests.get(url, json=None, headers=headers)
    update_json = json.loads(req.text)
    update_json["counter"] = 0
    requests.put(url, json=update_json, headers=headers)
    print("The counter has been reset")


async def update_king(ctx):
    # We request the data from the json
    req = requests.get(url, json=None, headers=headers)
    # We load said that to be able to access it
    update_json = json.loads(req.text)
    previous_king_id = update_json["koh"]["king"]["user_id"]
    if previous_king_id == str(ctx.message.author.id):
        await ctx.channel.send(f"You are already the King.")
        return
    # We get the date from the message and the date from the json
    current_date: datetime = ctx.message.created_at
    previous_date = update_json["koh"]["king"]["last_date"]
    previous_date = parser.parse(previous_date)
    # We calculate the difference between dates in hours
    time_delta = current_date - previous_date
    hours_lapsed = round(time_delta.total_seconds() / 3600, 1)
    # we check if this difference is bigger than the previous record
    previous_record = update_json["koh"]["record"]
    previous_record_holder = update_json["koh"]["record_id"]
    if hours_lapsed > previous_record:
        # If so, we update the record
        await ctx.channel.send(
            f"There is a new record of {hours_lapsed} hours. It is held by {mention_id(previous_king_id)}")
        update_json["koh"]["record"] = hours_lapsed
        # And set the last king as record owner
        update_json["koh"]["record_owner_id"] = previous_king_id
    else:
        hours_lapsed = update_json["koh"]["record"]
    # We set the new king and the current date
    new_msg = await ctx.channel.send(
        f"The new king is {mention_id(ctx.message.author.id)}. The current record is {hours_lapsed} hours and its "
        f"held by {mention_id(previous_record_holder)}.")
    await new_msg.add_reaction('👑')
    update_json["koh"]["king"]["user_id"] = str(ctx.message.author.id)
    update_json["koh"]["king"]["last_date"] = current_date.isoformat()
    # We transform the text back to json and put it back
    requests.put(url, json=update_json, headers=headers)


def backup_db():
    req = requests.get(url, json=None, headers=headers)
    # We load said that to be able to access it
    update_json = json.loads(req.text)
    with open("db_backup.json", "w") as to:
        to.write(json.dumps(update_json, indent=4))
