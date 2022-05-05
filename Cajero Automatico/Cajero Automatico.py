'''
CAJERO AUTOMATICO
'''
import tkinter as tk
from tkinter import messagebox
import json
import requests



#Funciones
def abrirVentana2():
    if entrada1.get()=="2021":
        ventana.destroy()
        
        def aceptar():
            global saldo
            #Se abre el archivo donde esta el saldo disponible y lo lee
            plata = open("saldo.txt", "r")
            moneda = plata.readlines()
            #se convierte en flotante el string del .txt
            saldo = float(moneda[0])
            opc = float(opcion.get())
            plata.close()
            
            
            if opc==1:
                def agregar(saldo):
                    saldo += extra.get()
                    #Una vez cambiado el valor del saldo se guarda en el .txt
                    plata = open("saldo.txt", "w")
                    plata.write(str(saldo))
                    plata.close()
                    #Se destruye la pantalla
                    ventana3.destroy()
                    messagebox.showinfo("Banco PioIX", f"su saldo actual es ${round(saldo,2)}")
                    #Luego de realizar la operacion se actualiza
                    actualizar()

                
                #Ventana para colocar el monto que se quiere agregar
                ventana3=tk.Toplevel(root)
                lblExtra = tk.Label (ventana3, text="Ingrese dinero-> ")
                extra = tk.IntVar()
                extra.set(" ")
                txtExtra = tk.Entry (ventana3, textvar=extra)
                btnAgregar = tk.Button(ventana3, text="Agregar", command=lambda x=saldo: agregar(x))
                
                #Configuracion estetica
                ventana3.configure(background="#88E0EF")
                ventana3.geometry("250x95")
                ventana3.iconbitmap("banco.ico")
                lblExtra.configure(background="#88E0EF", font=(10))
                txtExtra.configure(background="#C8E3D4")
                
                #Ubicacion
                lblExtra.grid (row=0 , column=0)
                txtExtra.grid (row=0 , column=1)
                btnAgregar.grid (row=1 , column=1, pady=10)
                ventana3.protocol("WM_DELETE_WINDOW", agregar)
                
                ventana3.mainloop()
            
            elif opc==2:
                def retirar(saldo):
                    if retiro.get()>saldo:
                        messagebox.showinfo("Banco Pio Ix","Excede el valor de su saldo")
                    else:
                        saldo -= retiro.get()
                        plata = open("saldo.txt", "w")
                        plata.write(str(saldo))
                        plata.close()
                        ventana3.destroy()
                        messagebox.showinfo("Banco PioIX", f"su saldo actual es ${round(saldo,2)}")
                        actualizar()
                     #Ventana para colocar el monto que se quiere retirar   
                ventana3=tk.Toplevel(root)
                lblRetiro = tk.Label (ventana3, text=("cuanto dinero desea retirar-> "))
                retiro = tk.IntVar()
                retiro.set(" ")
                txtRetiro = tk.Entry (ventana3, textvar=retiro)
                btnRetiro = tk.Button(ventana3, text="retirar", command=lambda x=saldo: retirar(x))
                 
                 #Configuracion Estetica
                ventana3.configure(background="#88E0EF")
                ventana3.geometry("350x95")
                ventana3.iconbitmap("banco.ico")
                lblRetiro.configure(background="#88E0EF", font=(10))
                txtRetiro.configure(background="#C8E3D4")
                 #Ubicacion
                lblRetiro.grid (row=0 , column=0)
                txtRetiro.grid (row=0 , column=1)
                btnRetiro.grid (row=1 , column=1)
                ventana3.protocol("WM_DELETE_WINDOW", retirar)
                
                ventana3.mainloop()
                
                
            elif opc==3:
                #Nuevo .txt con el saldo en dolares
                dolares = open("dolar.txt", "r")
                moneda_dolar = dolares.readlines()
                saldo_dolar =float(moneda_dolar[0])
                dolares.close()
                
                
                def comprar(saldo, saldo_dolar):
                    #Se toma el valor del dolar-compra del url
                    dolar =compraDolar.get() * compra
                    if dolar>saldo:
                        messagebox.showinfo("Cuidado", "Excede limite de dolares")
                    else:
                        saldo = saldo-dolar
                        #Se resta el monto comprado del saldo disponible
                        plata = open("saldo.txt", "w")
                        plata.write(str(saldo))
                        plata.close()
                        dolares=open("dolar.txt", "w")
                        saldo_dolar += compraDolar.get()
                        dolares.write(str(saldo_dolar))
                        dolares.close()
                        ventana3.destroy()
                        messagebox.showinfo("Banco Pio IX", f"su saldo en dolar es usd$ {saldo_dolar}")
                        actualizar()
                #Pantalla para comprar dolares
                ventana3=tk.Toplevel(root)
                lblCompra = tk.Label (ventana3, text=("Ingrese el monto que desea comprar-> "))
                compraDolar = tk.IntVar()
                compraDolar.set(" ")
                txtCompra = tk.Entry (ventana3, textvar=compraDolar)
                btnCompra = tk.Button(ventana3, text="comprar", command=lambda x=saldo, y=saldo_dolar: comprar(x,y))
                #configuracion estetica
                ventana3.configure(background="#88E0EF")
                ventana3.geometry("400x95")
                ventana3.iconbitmap("banco.ico")
                lblCompra.configure(background="#88E0EF", font=(10))
                txtCompra.configure(background="#C8E3D4")
                #ubicacion
                lblCompra.grid (row=0 , column=0)
                txtCompra.grid (row=0 , column=1)
                btnCompra.grid (row=1 , column=1)
                ventana3.protocol("WM_DELETE_WINDOW", comprar)
                
                ventana3.mainloop()

                
            elif opc==4:
                dolares = open("dolar.txt", "r")
                moneda_dolar = dolares.readlines()
                saldo_dolar = float(moneda_dolar[0])
                dolares.close()
                


                def vender(saldo, saldo_dolar):
                    if ventaDolar.get()>saldo_dolar:
                        messagebox.showinfo("Cuidado", "Excede limite de dolares")
                        
                    else:
                        dolar = ventaDolar.get() * venta
                        saldo = saldo + dolar
                        plata = open("saldo.txt", "w")
                        plata.write(str(saldo))
                        plata.close()
                        dolares = open("dolar.txt", "w")
                        saldo_dolar -= ventaDolar.get()
                        dolares.write(str(saldo_dolar))
                        dolares.close()
                        ventana3.destroy()
                        messagebox.showinfo("Banco Pio IX", f"su saldo en dolar es usd$ {saldo_dolar}")
                        actualizar()

                ventana3=tk.Toplevel(root)
                lblVenta = tk.Label (ventana3, text=("cuanto dinero desea vender-> "))
                ventaDolar = tk.IntVar()
                ventaDolar.set(" ")
                txtVenta = tk.Entry (ventana3, textvar=ventaDolar)
                btnVenta = tk.Button(ventana3, text="vender", command=lambda x=saldo, y=saldo_dolar: vender(x,y))
                
                ventana3.configure(background="#88E0EF")
                ventana3.geometry("350x95")
                ventana3.iconbitmap("banco.ico")
                lblVenta.configure(background="#88E0EF", font=(10))
                txtVenta.configure(background="#C8E3D4")
                
                lblVenta.grid (row=0 , column=0)
                txtVenta.grid (row=0 , column=1)
                btnVenta.grid (row=1 , column=1)
                ventana3.protocol("WM_DELETE_WINDOW", vender)
                
                ventana3.mainloop()

            elif opc==5:
                salida=messagebox.askokcancel("atención!!", "confirmar salir")
                if salida:
                    exit()

            else:
                print ("vuelva a digitar bien la opcion")


        #ventana principal
        ventana2= tk.Frame(root)
        ventana2.grid()
        ventana2.configure(background="#88E0EF")
        root.geometry("410x250")
        root.configure(background="#88E0EF")
    
        
        dolares = open("dolar.txt", "r")
        dolar=float(dolares.readline())
        plata = open("saldo.txt", "r")
        saldo= float(plata.readline())
        dolares.close()
        plata.close()
        
            #Funcion para actualizar el saldo luego de una operacion
        def actualizar():
            dolares = open("dolar.txt", "r")
            dolar=float(dolares.readline())
            plata = open("saldo.txt", "r")
            saldo= float(plata.readline())
            dolares.close()
            plata.close()
            
            lblSaldo2.config(text=f"${round(saldo,2)}")
            lblDolar2.config(text=f"USD${dolar}")     
        
        
            #los objetos de la Ventana Principal
        lblMenu = tk.Label (ventana2, text="   .:MENU:.")
        lblOpcion1 = tk.Label (ventana2, text="1. Ingresar dinero en la cuenta")
        lblOpcion2 = tk.Label (ventana2, text="2. Retirar dinero de la cuenta")
        lblOpcion3 = tk.Label (ventana2, text="3. Comprar dolar")
        lblOpcion4 = tk.Label (ventana2, text="4. Vender dolar")
        lblOpcion5 = tk.Label (ventana2, text="5. Salir")
        opcion = tk.IntVar()
        opcion.set(" ")
        lblOpcion = tk.Label(ventana2, text= "Igrese su opcion: ")
        txtOpcion = tk.Entry (ventana2, textvar=opcion)
        btnAceptar = tk.Button(ventana2, text="aceptar", command=aceptar)
        lblSaldo1 = tk.Label (ventana2, text="Saldo Actual:")
        lblSaldo2 = tk.Label (ventana2, text=f"${round(saldo,2)}")
        lblDolar1 = tk.Label (ventana2, text="Saldo En Dolares Actual:")
        lblDolar2 = tk.Label (ventana2, text=f"USD${dolar}")
            #Configuracion de la ventana principal
        lblMenu.configure(background="#88E0EF", font=("Arial",12, "bold"))
        lblOpcion1.configure(background="#88E0EF", font=(10))
        lblOpcion2.configure(background="#88E0EF", font=(10))
        lblOpcion3.configure(background="#88E0EF", font=(10))
        lblOpcion4.configure(background="#88E0EF", font=(10))
        lblOpcion5.configure(background="#88E0EF", font=(10))
        lblOpcion.configure(background="#88E0EF", font=(10))
        lblSaldo1.configure(background="#88E0EF",font=(10), padx=10)
        lblSaldo2.configure(background="#C8E3D4",font=(10), padx=10)
        lblDolar1.configure(background="#88E0EF", font=(10),padx=10)
        lblDolar2.configure(background="#C8E3D4",font=(10), padx=10)
        btnAceptar.configure(width=25)
                #Ubicacion de los objetos en la ventana principal
        lblMenu.grid (row=0 , column=0)
        lblOpcion1.grid (row=1 , column=0, sticky="W")
        lblOpcion2.grid (row=2 , column=0, sticky="W")
        lblOpcion3.grid (row= 3, column=0, sticky="W")
        lblOpcion4.grid (row= 4, column=0, sticky="W")
        lblOpcion5.grid (row= 5, column=0, sticky="W")
        lblOpcion.grid (row=7 , column=0)
        txtOpcion.grid (row=8 , column=0)
        btnAceptar.grid (row=8 , column=2, columnspan=2)
        lblSaldo1.grid (row=0 , column=2)
        lblSaldo2.grid (row=1 , column=2)
        lblDolar1.grid (row=2 , column=2)
        lblDolar2.grid (row=3 , column=2)

        
       
        
    else:
        messagebox.showwarning("Alerta", "contraseña invalida")



    
   





#PaginaPrincipal
root=tk.Tk()
root.title("Banco PIOIX")
root.geometry("300x150")
root.iconbitmap("banco.ico")
root.config(background="#88E0EF")

#Ventana de contraseña
ventana=tk.Frame(root)
ventana.config(background="#88E0EF")
ventana.grid()


lblBienvenidos = tk.Label(ventana, text="Bienvenidos al Banco Pio IX", anchor="center")
lblBienvenidos.configure(background="#88E0EF", font=("Arial", 15, "bold"))
lblContraseña=tk.Label(ventana, text="Por favor ingrese su Contraseña",
                       padx=20, pady=5)

#Configuraciones
lblContraseña.configure(background="#88E0EF", font=("Arial", 10))
entrada1=tk.Entry(ventana, show="*")
btnIngresar=tk.Button(ventana, text="Ingresar", command=abrirVentana2, anchor="center")


#Ubicacion
lblBienvenidos.grid(row=0, column=0, padx=5, pady=5)
lblContraseña.grid(row=1, column=0, padx=5, pady=5)
btnIngresar.grid(row=3, column=0, padx=5, pady=10)
entrada1.grid(row=2, column=0)


#Direccion url de la api para saber el valor del dolar
u="https://www.dolarsi.com/api/api.php?type=valoresprincipales"
c= requests.get(u)
c= c.text
y= json.loads(c)

#valores de compra y venta del dolar
compra = float(y[0]["casa"]["compra"].replace(",","."))
venta = float(y[0]["casa"]["venta"].replace(",","."))


root.mainloop()