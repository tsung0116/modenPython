from twisted.internet import reactor

def throwExcept():
    raise Exception("Hi")

def upagain():
    print('But I get up again.')
    reactor.stop()

def falldown():
    try:
        throwExcept()
    except (Exception):
        print ('I fall down.')
        raise
    else:
        print (2)

reactor.callWhenRunning(falldown)
reactor.callWhenRunning(upagain)

print('Starting the reactor.')
reactor.run()