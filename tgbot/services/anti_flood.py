async def anti_flood(*args, **kwargs):
    message = args[0]
    print("flood, message deleted!")
    await message.delete()