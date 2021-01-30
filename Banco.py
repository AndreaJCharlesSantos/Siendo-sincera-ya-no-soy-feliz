
import numpy as np

class Banco(object):
    count=0
    #Los atributos de cliente
    def __init__(self, name, date, curp, address, phone, first_deposit, account_type):
     self.name = name
     self.date = date
     self.curp = curp
     self.address = address
     self.phone =  phone
     self.first_deposit = first_deposit
     self.account_type = account_type

    def listToString(self):  
     return self.name + "," + self.date + "," + self.curp + "," + self.address + "," + self.phone + "," + str(self.first_deposit) + "," + self.account_type + "\n"
    #def Validar(self, v):     

class Menu(): 
    num=0
    global listaclientes
    listaclientes = []

    def  __init__(self):
     archivocliente = open("Archivo.txt", "r") 
     for j in archivocliente:
       listaclientes.append(j)
     archivocliente.close()
    def NewAccount(self):
     nombre = input("Ingrese el nombre del cliente: ")
     date = input("Ingrese la fecha de nacimiento dd/mm/yyyy: ")
     curp = input("Ingrese CURP de la persona: ")
     address = input("Ingrese la dirección: ")
     phone = input("Ingrese el número de teléfono: ")
     first_deposit = int(input("Ingrese el deposito: "))
     account_type = input("Seleccione el tipo de cuenta: \n1. Ahorro \n2. Actual \n3. Por un año. \n4. Por dos años \n5. Por tres años ")  
     NUEVACUENTA = Banco(nombre,date,curp,address,phone,first_deposit,account_type)
     listaclientes.append(NUEVACUENTA)

    def edit(self):

     num = input("Ingrese la CURP de la persona: ")
     for j in listaclientes:
      if j.curp == num:
       a = int(input("1. Direccion\n2. Número de teléfono\n¿Qué desea modificar?: "))
       if a == 1:
        modificacion = input("Ingrese la nueva dirección: ")
        j.address = modificacion
       elif a == 2:
        modificacion = input("Ingrese el nuevo número de teléfono: ")
        j.phone = modificacion
       else:
        print("Intente nuevamente")
      else:
       print("No existe el cliente")
     op = int(input("Ingrese un número para continuar: ")) 
       
    def transaccion(self):
     num = input("Ingrese la CURP de la persona: ")
     for j in listaclientes:
      if j.curp == num:
       a = int(input("Desea\n1. Depositar\n2. Sacar dinero: "))       
       if a == 1:
        modificacion = int(input("Ingrese cuanto desea depositar: "))
        j.first_deposit +=  modificacion
        print("Deposito con éxito")
       elif a == 2:
        modificacion = int(input("Ingrese cuanto desea retirar: "))
        if (j.first_deposit-modificacion) > 0: 
         j.first_deposit -= modificacion
        else:
         print("Cantidad insuficiente")
       else:
        print("Intente nuevamente")
      else:
       print("No existe el cliente")
     op=int(input("Ingrese algún digito para continuar: "))  

    def VerCliente(self):
     num=int(input("Lo buscará en base en: \n1. CURP\n2. Nombre\n"))
     if num == 1:
      a=input("CURP de la cuenta: ")
      for j in listaclientes:
       if j.curp == a:
         print('Nombre: {}|Fecha de nacimiento: {}|CURP: {}|Direccion: {}|Telefono: {}|Deposito: {}|Tipo de cuenta: {}'.format(j.name,j.date,j.curp,j.address,j.phone,j.first_deposit,j.account_type))
       else:
         print("No existe tal cuenta")
     elif num == 2:
       a=input("Nombre de la cuenta: ")
       for j in listaclientes:
        if j.name == a:
          print('Nombre: {}|Fecha de nacimiento: {}|CURP: {}|Direccion: {}|Telefono: {}|Deposito: {}|Tipo de cuenta: {}'.format(j.name,j.date,j.curp,j.address,j.phone,j.first_deposit,j.account_type))
        elif j.name != a:
         print("No existe tal cuenta")

    def BorrarCliente(self):
     num = input("Ingrese la CURP de la cuenta ")
     for j in listaclientes:
      if j.curp == num:
       listaclientes.remove(j)
      else:
       print("No existe tal cuenta")
     op=int(input("Ingrese un número para continuar "))        

    def view_list(self):
     for j in listaclientes:
      print('Nombre: {}|Fecha de nacimiento: {}|CURP: {}|Direccion: {}|Telefono: {}|Deposito: {}|Tipo de cuenta: {}'.format(j.name,j.date,j.curp,j.address,j.phone,j.first_deposit,j.account_type))
     op=int(input("Ingrese un número para continuar "))

    def menuprincipal(self):
     op = 0
     #Menu.Validar(self, valor)
     while op != 7:
        
      print("                                       ||||||BIENVENIDO AL MENÚ PRINCIPAL||||||  \n ")
      print("1.Crea una nueva cuenta")
      print("2.Editar información en una cuenta existente")
      print("3.Transacción")
      print("4.Checar los detalles de una cuenta existente")
      print("5.Borrar cuenta")
      print("6.Lista de los clientes existentes")
      print("7.Salir")
      op = int(input("Ingresa la opción "))
      if op == 1:
       Menu.NewAccount(self)
      elif op == 2:
       print("         ||||||||||EDITA UNA CUENTA||||||||||")
       Menu.edit(self)

      elif op == 3:
       print("         ||||||||||REALIZA UNA TRANSACCIÓN ||||||||||")
       Menu.transaccion(self)
      elif op == 4:
       print("         ||||||||||VER CLIENTE||||||||||")
       Menu.VerCliente(self)        
      elif op == 5:
       print("         |||||||||BORRAR CLIENTE||||||||")
       Menu.BorrarCliente(self)       
      elif op == 6:
       print("         |||||||||VER LISTA||||||||")
       Menu.view_list(self)
      elif op == 7:
       archivocliente = open("Archivo.txt", "a")
       for j in listaclientes:
        archivocliente.write(j.listToString())
       archivocliente.close()
       '''
       print("Gracias por usar el programa")
       archivocliente = open("Archivo.txt", "a")
       for linea in listaclientes:
        archivocliente.write(str(linea))

       archivocliente.close()
       
       archivocliente = open("Archivo.txt", "w")
       archivocliente.close()
       archivocliente = open("Archivo.txt", "r+")
       archivocliente.write(Menu.listToString(self,listaclientes))
       archivocliente.close()
       '''

       exit   
      elif op != 1 or op != 2 or op != 3 or op != 4 or op != 5 or op != 6 or op != 7:
        print("Ingrese una opción correcta")
 

#Termina clase

MenuBanco=Menu()
MenuBanco.menuprincipal()


#Termina clase