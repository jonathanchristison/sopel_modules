from sopel.module import commands, NOLIMIT, example

@commands('call')
@example('.call gss')
def calls(bot, trigger):
    text = trigger.group(2)
    if not text:
        bot.say("Please specify a param: gss|eng")
        return NOLIMIT
    if text == "gss":
        bot.say('https://redhat.bluejeans.com/u/sjavurek/')
    else:
        bot.say('https://bluejeans.com/9247086522/')
