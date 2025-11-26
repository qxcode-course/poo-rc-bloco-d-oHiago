class Fone:
    def __init__(self, id:int):
        self.__id: int
        self.__number: str

    def getId(self):
        return self.__id
    def getNumber(self):
        return self.__number
    
    def __str__(self):
        return f"{self.__id} {self.__number}"

class Contact:
    def __init__(self,name:str):
        self.name = name
        self.fones: list [Fone] = []
        self.favorited = True

