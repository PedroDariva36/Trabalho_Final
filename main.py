from classes import *
from  functions import *

mainMenuInterupt = 1
while(mainMenuInterupt):
    print("Bem vindo ao PYmazon: \n")
    print("1) Cadastro")
    print("2) Entrar")
    print("$) Sair \n")

    mainMenuAction = input("==> ")
    if(mainMenuAction == "$"):
        mainMenuInterupt = 0

    elif(mainMenuAction == "1"):
        signupMenuInterupt = 1
        while(signupMenuInterupt):
            name = input("\nDigite seu nome de usuario: ")
            cpf = input("Digite seu CPF: ")
            email = input("Digite seu Endereço de email: ")
            password = input("Digite sua senha (min 6): ")
            passConfirm = input("Comfirme sua senha:")
            
            if("@" in email and password == passConfirm and cpfValidation(cpf)):
                user = User(name,cpf,email,password,0)
                createUser(user.toList())
                signupMenuInterupt = 0
            else:
                print("Algum erro foi encontrado, Digite os valores novamente \n\n")
                signupMenuInterupt = 0
            signupMenuInterupt = 0

    elif(mainMenuAction == "2"):
        loginMenuInterupt = 1
        while(loginMenuInterupt):
            cpf = input("\n\nDigite seu CPF: ")
            userSession = []
            userSession = getUserObjectForLogin(int(cpf))
            
            if len(userSession) != 5:
                print("CPF não cadastrado, digite novamente \n")
                loginMenuInterupt = 1
                break 

            password = input("Digite sua senha: ") 
            
            if userSession[3] != password:
                print("CPF não cadastrado, digite novamente \n")
                loginMenuInterupt = 1
                break

            userMenuInterup = 1
            while(userMenuInterup):


                print("\n\nOlá {}!\n".format(userSession[0]))
                print("1) Adicionar Credito")
                print("2) Comprar")
                print("$) Sair")
                userMenuAction = input("\n ==> ")

                if userMenuAction == "$":
                    userMenuInterup = 0
                    loginMenuInterupt = 0

                elif userMenuAction == "1":
                    balanceLimit = abs(float(userSession[4]) - 1000.0)
                    
                    if(balanceLimit == 0 or float(userSession[4]) == 1000.0):
                        print("\nCredito Maximizado \n ")
                        
                    else:
                        print("CRÉDITO: ")
                        numCard = input("Digite o numero do seu Cartão de Crédtio: ")
                        safeNumCard = input("Digite o Código de Segurança: ")
                        credit = float(input(f"Quanto voce pretende depotitar? (Max: R$ {balanceLimit:.02f}): "))
                        
                        if(credit <= balanceLimit and credit > 0 ):
                            print(userSession[1])
                            total = float(userSession[4]) + credit
                            alterUserBalance(userSession[1], total)
                            userSession = getUserObjectForLogin(int(cpf))


                elif userMenuAction == "2":
                    print("CARRINHO: ")
                    if(float(userSession[4]) > 0):
                        cart = makeShoppingCart()
                        printCart(cart)
                        
                        cartMenuInterupt = 1
                        while(cartMenuInterupt):
                            print("1) Adicionar Produto")
                            print("2) Finalizar Compra")
                            print("$) Cancelar")

                            cartMenuAction = input("===> ")

                            if(cartMenuAction == "$"):
                                cartMenuInterupt = 0
                                break

                            elif(cartMenuAction == "1"):
                                itemId = int(input("\nQual item você quer Selecionar (ID): "))
                                itemUnit = int(input("\nQuantas Unidade do Item: "))
                                addProductToCart(itemId,itemUnit,cart)
                                for i in range(len(cart)):
                                    cart[i][4] = float(cart[i][2]) * float(cart[i][3])
                                printCart(cart)

                            elif(cartMenuAction == "2"):
                                transactionConfirm = input("Você deseja mesmo finalizar a compra (y) para sim (n) para não: " )

                                if(transactionConfirm == "y"):
                                    total = getCartTotal(cart)
                                    if total > float(userSession[4]):
                                        print("\nCredito Insuficiente\n")
                                    else:
                                        print("\nObrigado por sua compra! \n")
                                        alterUserBalance(userSession[1],float(userSession[4]) - total)
                                        userSession = getUserObjectForLogin(int(cpf))
                                        cart = []
                                        cartMenuInterupt = 0

                    


                

        