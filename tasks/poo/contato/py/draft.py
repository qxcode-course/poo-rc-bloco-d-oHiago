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
        if index < 0 or index > len(self.fones):
            print("index invalido")
        
        else:
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
        

def main():
    contato = Contact("")

    while True:
        line = input()
        print("$" + line)
        args = line.split()
        try:

            if args[0] == "end":
                break
            elif args[0] == "show":
                print(contato)
            elif args[0] == "init":
                contato = Contact (str(args[1]))
            elif args[0] == "add":
                fone = Fone(args[1], args[2])
                if contato.validar(fone):
                    contato.addFone(fone)
                else:
                 print("fail: invalid number")
            elif args[0] == "rm":
                contato.remove(int(args[1]))
            
            elif args[0] == "tfav":
                contato.Favorito()

            else:
                print("fail comando invalido")
        except Exception as e:
            print(e)


if __name__ == "__main__":   
    main()
