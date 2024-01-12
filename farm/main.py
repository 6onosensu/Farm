from player import Player


class Controller:
    def __init__(self):
        self.player = Player()

    def process_input(self, user_input):
        commands = user_input.split()
        if len(commands) == 0:
            return

        command = commands[0].lower()
        if command == 'plant':
            if len(commands) > 1:
                self.player.plant(commands[1])
            else:
                print('Please specofy a plot to plant.')
        elif command == 'harvest':
            if len(commands) > 1:
                self.player.harvest(commands[1])
            else:
                print('Please specify a plot to harvest.')
        elif command == 'buy':
            if len(commands) > 2:
                item = commands[1]
                quantity = int(commands[2])
                self.player.buy(item, quantity)
            else:
                print('Please specify what to buy and the quantity')
        elif command == 'sell':
            if len(commands) > 2:
                item = commands[1]
                quantity = int(commands[2])
                self.player.sell(item, quantity)
            else:
                print('Please specify what to buy and the quantity')
        else:
            print('Unknown command.')


control = Controller()

while True:
    user_input = input('Enter coommand: ')
    if user_input == 'quit':
        break
    else:
        control.process_input(user_input)
