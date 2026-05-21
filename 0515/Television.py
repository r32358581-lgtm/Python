class Television:
    serialNumber = 0

    def__init__(self, channel, voiume, on):
       self.channel = channel
       self.voulume = volume
       self.on = open
       Television.serialNumber += 1
    
       self.number = Television.serialNumber
    
    def show(self):
        print(self.channel, self.volume, self.on, self.number)

myTV = Television(11, 10, True):
myTV.show()