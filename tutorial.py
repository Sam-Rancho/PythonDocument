import discord
import asyncio
import random

'''
Discord API Wrapper Example

Copyright License: You may use this in anyway possible, this document is free to use for educational purposes ONLY.

https://github.com/Sam-Rancho/PythonDocument

Todo In Class:
Kicking Users
Banning Users
Exceptions

Begins Script
'''


# Defines discord.Client as client to call easier.
client = discord.Client()

# Starts a Client Event.
@client.event

# Async Message.
async def on_message(message):
        # If The Message Sent Starts With Ping, We Send an Output Of Pong.
        if message.content.startswith('ping'):
                # We are using async_timeout, so it does require an await statement, even though it doesn't make much sense.
                await client.send_message(message.channel, 'PONG!')
        # This Command is an Example of User Choice, We Will Allow The User To Choose There Choice And We Give Them an Output Based on There Input Given.
        if message.content.startswith('gamble '):
                # Alright, we are going to first send them a message saying to pick a number between 1 through 10
                await client.send_message(message.channel, 'Picking a number between 1 through 10... Let us see what you get!')
                answer = message.content.replace('gamble ', '')
                # Replace the content of there message to '' to call easier
                generatedNumber = random.randint(1,10)
                # Generate a Random Number
                await asyncio.sleep(3)
                # A 3 Second wait Period
                try:
                # If There Answer == generatedNumber Then They Win! Else, They Lose.
                    if int(answer) == generatedNumber:
                            await client.send_message(message.channel, "You Win! The Number Was " + str(generatedNumber))
                    else:
                            await client.send_message(message.channel, "You Lose! The Number Was " + str(generatedNumber))
                except ValueError:
                        # If It is This Certain Error, Which Occurs When They Input A String E.x. gamble agdhlaga This Happens:
                        await client.send_message(message.channel, "Please enter a valid number or try again later...")
        if message.content.startswith('spin'):
                gamble = random.randint(1, 6)
                if gamble == 6:
                        await client.send_message(message.channel, 'you got shot, rip...')
                else:
                        await client.send_message(message.channel, 'you are safe, gg!')
                        

                                                                          

'''
Here is the final step, you must go to discordapp.com
If you haven't made an account yet, make one...
On The Top Menu on discordapp.com, There is a few options these options are:
Features
Download
Partners
Merch
Blog
More V

Hover Over "More V" To Get a List of Options...
These Options Are:
Status
Help & Support
Feedback
HypeSquad
StreamKit
Company
Jobs
---------
Security
Developers
Branding

Click Developers...
On The Left Hand Side, There is a List Of Options, Find "My Applications"
Click on it.
If you haven't made an application yet, click on "New Application"
Give your Application a Name... e.x. Superman
Everything else is optional at this point, you may choose to add an image and an app description.
Once you are done, click "Create Application"
If you see "Waiting for form completion", you have not fillen out the required amount of information

FOR PEOPLE WITH EXISTING APPS:
If you have an application already and you haven't made it a Bot, Click Create a Bot User...

FOR PEOPLE WHO JUST MADE THEM WITH THE TUTORIAL GIVEN:
It should open a new page, once this page loads up, it gives a success message at the top saying that your application has been made, if this is what you see, you must follow this simple steps:
Click "Create a Bot User"
It should give you a warning saying this is irrevocable, click "Yes, do it!"

---------

Once these steps have been completed, on the top, you will see Token: click to reveal
Copy and paste the "TOKEN" into the API_KEY... e.x. API_KEY = 'ajglshaga;djahg;ajh148u124'

Boom, you are all done, congratulations!
'''


API_KEY = ''
client.run(API_KEY)

                
