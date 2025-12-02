class Fone:
    def __init__(self, label: str, number: str):
        self.label = label
        self.number = number

    def __str__(self):
        return f"{self.label}:{self.number}"

class Contact:
    def __init__(self,name:str):
        self.name = name
        self.fones: list [Fone] = []
        self.favorited = False

    def addFone(self, fone: Fone):
        self.fones.append(fone)

    def remove(self, index: int):
        if index < 0 or index >= len(self.fones):
            raise Exception ("fail: index invalido")
        self.fones.pop(index)
    def validar(self, fone: Fone) -> bool:
        validos = "0123456789()."
        for i in fone.number:
            if i not in validos:
                return False
        return True
        
    def Favorito(self):
        self.favorited = not self.favorited
    


    def __str__(self):
        fav = '@' if self.favorited else '-'
        lista = ", ".join([str(fone) for fone in self.fones])
        return f"{fav} {self.name} [{lista}]"
        
class Agenda:
    def __init__(self):
        self.contato: dict[Contact] = {}

    def add_contato(self,name, fones):
        if name not in self.contato:
          self.contato[name] = Contact(name)
        for fone in fones:
            self.contato[name].addFone(fone)
    def get_contato(self, nome:str):
         try:   
            return self.contato[nome]
         except KeyError as _:
            raise Exception(f"Contato nome {nome} nao existe")
    
        
    def __str__(self):
        lista = sorted(self.contato.values(), key = lambda c: c.name)
        return "\n".join(str(contato) for contato in lista)

        
def main():

    agenda = Agenda()

    while True:
        line = input()
        print("$"+line)
        args = line.split()
        try:

            if args[0] == "end":
                break
            elif args[0] == "show":
                print(agenda)
            elif args[0] == "add": 
               name = args[1]
               fone = []
               for token in args[2:]:
                   if ":" not in token:
                       continue
                   label, number = token.split(":")
                   fone.append(Fone(label,number))
               agenda.add_contato(name,fone)         
            else:
                print("fail: comando invalido")
        except Exception as e:
            print(e)
if __name__ == "__main__":
    main()