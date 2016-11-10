import sopel.module

@sopel.module.commands('versions')
def helloworld(bot, trigger):
    bot.say('Hello, world!')