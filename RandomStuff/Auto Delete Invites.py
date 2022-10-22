async def send_warning(ctx):
    warning = await ctx.channel.send(f"Don't send invites here <@{ctx.author.id}>")
    await asyncio.sleep(3)
    await warning.delete()

@dis_client.event
async def on_message(ctx):
    invites = await ctx.guild.invites()
    msg = ctx.content
    for v in invites:
        invite = str(v).replace("https://", "")
        msg = msg.replace(invite, "")
    if ".gg/" in msg:
        immuneroles = {"beta", "Chat Mod"}
        check = any(item in immuneroles for item in [str(i) for i in ctx.author.roles])
        if check: return
        await ctx.delete()
        await send_warning(ctx)
