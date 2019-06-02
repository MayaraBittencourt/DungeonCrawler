from room import *

def main():
    print('DungeonCrawler')
    currentRoom = Room('Você esta em uma caverna!')

    print(currentRoom.get_description())

    while True:
        command = input('>')
        result = currentRoom.execute_command(command)
        print (result)

if __name__ == "__main__":
     main()

