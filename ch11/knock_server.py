from twisted.internet import protocol, reactor

class Knock(protocol.Protocol):
    def dataReceived(self, data):
        print("Client:{}".format(data))
        if data.startswith("Knock knock".encode('utf-8')):
            response = "Who's there?"
        else:
            response = data + " who?".encode('utf-8')
        print("Server:{}".format(response))
        print('Type of response {}'.format(type(response)))
        if isinstance(response, str): 
            self.transport.write(response.encode())
        else:
            self.transport.write(response)

class KnockFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Knock()

reactor.listenTCP(8000, KnockFactory())
reactor.run()