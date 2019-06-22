from room import *

def main():
    print('DungeonCrawler')
    southNeighbor = Room('Você esta em outra sala', None)
    currentRoom = Room('Você esta em uma caverna!', southNeighbor)

    print(currentRoom.get_description())

    while True:
        command = input('>')
        result = currentRoom.execute_command(command)
        currentRoom = result.currentRoom
        print (result.toPrint)



if __name__ == "__main__":
   main()
   