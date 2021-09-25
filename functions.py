import csv

#  -> Ordem de gravação: name, cpf, email, pass, balance  

def getUserData():
    userData = []
    with open('users.csv', 'r', newline = '') as fileData:
        readerObject = csv.reader(fileData)  
        for item in readerObject:
            userData.append(item)
        fileData.close()   
    return userData


def getUserObjectForLogin(key):
    dataContent = getUserData()
    for i in dataContent:
        if int(i[1]) == key:
            return i


def createUser(uList):
    with open('users.csv', 'a', newline = '') as fileData:
        writerObject = csv.writer(fileData)
        writerObject.writerow(uList)  
        fileData.close()


def alterUserBalance(key, newUnitaddUnit):   
    dataContent = getUserData()
    for i in range(len(dataContent)):
        if dataContent[i][1] == key:
            dataContent[i][4] = newUnitaddUnit
    with open('users.csv', 'w', newline = '') as fileData:
        writerObject = csv.writer(fileData)
        writerObject.writerows(dataContent)
        fileData.close()


def getProductData():
    productData = []
    with open('products.csv', 'r', newline = '') as fileData:
        readerObject = csv.reader(fileData)  
        for item in readerObject:
            productData.append(item)
        fileData.close()   
    return productData

def makeShoppingCart():
    cartData = []
    cartData = getProductData()
    for i in range(len(cartData)):
        cartData[i].append(0)
        cartData[i].append(0)
    return cartData


def addProductToCart(pId,addUnit,cart):
    for i in range(len(cart)):
            if int(cart[i][0]) == pId:
                cart[i][3] = addUnit

def getCartTotal(cart):
    sum = 0.0
    for i in cart:
        sum = sum + float(i[4])
    return sum

def printCart(cart):
    print("{:<3} {:<22} {:<12} {:<7} {:<10}".format("ID"," Nome do Produto"," Preço","Unidade"," Preço Total"))
    for i in cart:
        x = f" {float(i[4]):.02f}" 
        print("{:<3} {:<22} {:<12} {:<7}  R$ {:<10}".format(str(i[0]),str(i[1]),str(i[2]),str(i[3]), str(x)))
    print("--------------------")
    sum = getCartTotal(cart)
    print(f"Total do Carrinho: R$ {sum:.02f}")
    

def cpfValidation(cpfOriginal):
    cpf = [int(i) for i in cpfOriginal]
    if len(cpf) != 11:
        return False
    elif cpf == cpf[::-1]:
        return False
    for i in range(9, 11):
        UnitaddUnit = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((UnitaddUnit * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True
