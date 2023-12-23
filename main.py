import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command()
async def request(ctx, res: str, amount: int, payment: str, payment_amount: int):
    user_name = ctx.author.name # Get the name of the user

    if amount and payment_amount <= 0: # Check if "amount" and "payment_amount" are negative or 0
        await ctx.send('Invalid amount. Please enter a positive number.')
        return

    flame_contact = bot.get_user(672992893685858397)
    steel_price = 7.5 * amount
    concrete_price = 5 * amount
    whiskey_price = 2 * amount

    formatted_steel = '{:,}'.format(steel_price) # format numbers with a ',' (Ex. 1,000 instead of 1000)
    formatted_concrete = '{:,}'.format(concrete_price) # format numbers with a ',' (Ex. 1,000 instead of 1000)
    formatted_whiskey = '{:,}'.format(whiskey_price) # format numbers with a ',' (Ex. 1,000 instead of 1000)
    formatted_amount = '{:,}'.format(amount) # format numbers with a ',' (Ex. 1,000 instead of 1000)
    formatted_payment = '{:,}'.format(payment_amount) # format numbers with a ',' (Ex. 1,000 instead of 1000)

    if res == 'steel': # If user chose steel, it displays this
        embed=discord.Embed(
            title='Steel Trade Request.',
            description=f'Your request for {formatted_amount} steel has been processed. This request will cost £{formatted_steel}. Flameknight has been contacted.',
            color=discord.Color.red()
            )
        await ctx.send(embed=embed)
        
        try:
            # Send a direct message to the user with the trade request
            await flame_contact.send(f'{user_name} has requested {formatted_amount} steel with a cost of £{formatted_steel}. They are offering {payment} with an amount of {formatted_payment}. Do you accept? (y/n)')


            def check(message):
                return (
                    message.author == flame_contact and
                    isinstance(message.channel, discord.DMChannel) and
                    message.content.lower() in ['y', 'n']
                    )

            response_message = await bot.wait_for('message', timeout=30, check=check)

            if response_message.content.lower() == 'y':
                await flame_contact.send("You have accepted the trade request.")
                await ctx.author.send("Your trade request has been accpeted.")
            else:
                await flame_contact.send("You have rejected the trade request.")
                await ctx.author.send("Your trade request has been rejected.")
        except asyncio.TimeoutError:
            await flame_contact.send("You took too long to respond. The trade request has been canceled.")



    elif res == 'concrete': # If user chose concrete, it displays this
        embed=discord.Embed(
            title='Concrete Trade Request.',
            description=f'Your request for {formatted_amount} concrete has been processed. This request will cost {formatted_concrete}. Flameknight has been contacted.',
            color=discord.Color.red()
            )
        await ctx.send(embed=embed)
        
        try:
            # Send a direct message to the user with the trade request
            await flame_contact.send(f'{user_name} has requested {formatted_amount} concrete with a cost of £{formatted_concrete}. They are offering {payment} with an amount of {formatted_payment}. Do you accept? (y/n)')


            def check(message):
                return (
                    message.author == flame_contact and
                    isinstance(message.channel, discord.DMChannel) and
                    message.content.lower() in ['y', 'n']
                    )

            response_message = await bot.wait_for('message', timeout=30, check=check)

            if response_message.content.lower() == 'y':
                await flame_contact.send("You have accepted the trade request.")
                await ctx.author.send("Your trade request has been accpeted.")
            else:
                await flame_contact.send("You have rejected the trade request.")
                await ctx.author.send("Your trade request has been rejected.")
        except asyncio.TimeoutError:
            await flame_contact.send("You took too long to respond. The trade request has been canceled.")

    elif res == 'whiskey' or res == 'scotch': # If user chose whiskey or scotch, it displays this
        embed=discord.Embed(
            title='Whiskey Trade Request.',
            description=f'Your request for {formatted_amount} whiskey has been processed. This request will cost {formatted_whiskey}. Flameknight has been contacted.',
            color=discord.Color.red()
            )
        await ctx.send(embed=embed)
        
        try:
            # Send a direct message to the user with the trade request
            await flame_contact.send(f'{user_name} has requested {formatted_amount} whiskey with a cost of £{formatted_whiskey}. They are offering {payment} with an amount of {formatted_payment}. Do you accept? (y/n)')


            def check(message): 
                return (
                    message.author == flame_contact and
                    isinstance(message.channel, discord.DMChannel) and
                    message.content.lower() in ['y', 'n']
                    )

            response_message = await bot.wait_for('message', timeout=30, check=check) # takes in the response of "y" or 'n'

            if response_message.content.lower() == 'y': # if the response is 'y'
                await flame_contact.send("You have accepted the trade request.")
                await ctx.author.send("Your trade request has been accpeted.")
            else: # if the response is 'n'
                await flame_contact.send("You have rejected the trade request.")
                await ctx.author.send("Your trade request has been rejected.")
        except asyncio.TimeoutError: # message times out after 30 seconds.
            await flame_contact.send("You took too long to respond. The trade request has been canceled.")


bot.run('YOUR_TOKEN_HERE')
