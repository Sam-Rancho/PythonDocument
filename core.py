Import discord
Import random
Import asyncio


# Starts Client Events


Client = discord.Client
@client.event


Async def on_message(message):


If message.content.startswith(‘:test’):
	Await client.send_message(message.channel, ‘test is successful, your cool…’)


If message.content.startswith(‘:gamble ‘)
	Answer = message.content.replace(‘:gamble ‘, ‘’)
	AnswerKey = int(Answer)
	generatedNumber = random.randint(1,10)
	If AnswerKey == generatedNumber:
		Await client.send_message(message.channel, ‘you win!’)
	Else:
		Await client.send_message(message.channel, ‘you lose!’)


If message.content.startswith(‘:clear ‘):
	Try:
	Clear = message.content.replace(‘:clear ‘, ‘’)
		ClearKey = int(Clear)
	Await client.purge_from(message.channel, ClearKey)
	Await client.send_message(message.channel, ‘success!’)
Except ValueError:
	Await client.send_message(message.channel, ‘please enter a valid number…’)
Except discord.Forbidden
	Await client.send_message(message.channel, ‘please give bot proper permissions…’)


Password = ‘’
client.run(password)
	
# https://github.com/Sam-Rancho/PythonDocument	
