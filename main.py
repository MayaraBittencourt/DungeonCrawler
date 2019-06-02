from room import *

def main():
    print('DungeonCrawler')
    currentRoom = Room('Você esta em uma caverna!')

    print(currentRoom.get_description())

    while True:
        command = input('>')

        if command == 'look':
            print(currentRoom.get_description())
        else:
            print ('Não entendi.')

if __name__ == "__main__":
     main()

