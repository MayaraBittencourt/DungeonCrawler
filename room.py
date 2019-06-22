class Room:
    def __init__(self, description, southNeighbor):
        self._description = description
        self._southNeighbor = southNeighbor
        
    def get_description (self):
        return self._description
    
    def execute_command (self, command):
        if command == 'look':
            return ExecuteCommandResult(self.get_description(), self)
        elif command == 'go south':
            if self._southNeighbor == None:
                return ExecuteCommandResult ('Não tem sul O.o', self)
            else:
                return ExecuteCommandResult(self._southNeighbor.get_description(), self._southNeighbor)
        else:
            return ExecuteCommandResult('Não entendi.', self)

class ExecuteCommandResult:
    def __init__(self,toPrint,currentRoom):
        self.toPrint = toPrint
        self.currentRoom = currentRoom