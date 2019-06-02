class Room:
    def __init__(self, description):
        self._description = description
    
    def get_description (self):
        return self._description
    
    def execute_command (self, command):
        if command == 'look':
            return self.get_description()
        else:
            return 'Não entendi.'