from helpers.json_db import update_counter


async def show_counter(ctx):
    counter = update_counter()
    await ctx.channel.send(f"{counter} people have been shrekt")
