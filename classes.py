class User:
    def __init__(self, name,cpf, password,email,balance ):
        self.uName = name
        self.uCpf = cpf
        self.uPass = password
        self.uEmail = email
        self.uBalance = balance
    

    @classmethod

    # Método objInit:
    #   Permite a classe ser construida a partir de um objeto iteravel
    #   facilita na conversão das informaçoes do csv
    
    def objInit(cls, obj):
        return(cls(obj[0],obj[1],obj[2],obj[3],obj[4]))

    # Método toList:
    #   Converte a o objeto em uma list 
    #   facilita a gravação de usuarios 

    def toList(self):
        return [self.uName,self.uCpf,self.uPass,self.uEmail,self.uBalance]

class Product:
    def __init__(self, productId, productName, productValue):
        self.pId = productId
        self.pName = productName
        self.pValue = productValue

    @classmethod

    def objInit(cls, obj):
        return(cls(obj[0],obj[1],obj[2]))
    
    def toList(self):
        return [self.pId,self.pName,self.pValue]