import tkinter
import customtkinter
from PIL import Image, ImageTk
#import accounts

#https://www.youtube.com/watch?v=71X58zIzrgA
#import winreg
#import konto
#import os

#print(os.listdir(r'C:\Windows\fonts'))

#reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

#key = winreg.OpenKey(reg, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\FontSubstitutes', 0, winreg.KEY_READ)


#print(winreg.EnumValue(key, 26)[1])

#winFont = winreg.EnumValue(key, 26)[1]

#Cfont = customtkinter.CTkFont(family=winFont)
mode = "dark"

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue")


app = customtkinter.CTk()
app.title("Svedbank")
app.iconbitmap("svedbank.png")
app.geometry("600x360")



def switch_E_DL():
    global mode
    if mode == "dark":
        mode = "light"
        customtkinter.set_appearance_mode("light")
    elif mode == "light":
        mode = "dark"
        customtkinter.set_appearance_mode("dark")
    
def reg_btn():
    FPage.pack_forget()
    RegPage.pack()
    

    

def reg_acc():
    a = entryFname.get()
    b = entrySname.get()
    c = entryPassword.get()
    print(a, b, c)

def loginB():
    progressbar.configure()
    progressbar.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)
    
    progressbar.start()

    
    if progressbar.get() == 100:
        progressbar.stop()


def ret():
    RegPage.pack_forget()
    FPage.pack()
    
#cFont = customtkinter.CTkButton(app, font=)



#-------------------frames------------------------
BankPage = customtkinter.CTkFrame(master=app, width=200, height=200, corner_radius=20, bg_color="yellow")

RegPage = customtkinter.CTkFrame(master=app, width=600, height=360, corner_radius=20, bg_color="blue")

FPage = customtkinter.CTkFrame(master=app, width=600, height=360, corner_radius=20, bg_color="green")

FPage.pack()


#-------------------images-------------------------
bankimage = customtkinter.CTkImage(light_image=Image.open('svedbank.png'), dark_image=Image.open('svedbank.png'), size=(70, 70))
imglabel = customtkinter.CTkLabel(FPage, text="", image=bankimage)
imglabel.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
bankimage = customtkinter.CTkImage(light_image=Image.open('svedbank.png'), dark_image=Image.open('svedbank.png'), size=(70, 70))
imglabel = customtkinter.CTkLabel(RegPage, text="", image=bankimage)
imglabel.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)


#------------------progressbar----------------------
progressbar = customtkinter.CTkProgressBar(FPage, mode="indeterminate", determinate_speed=1, indeterminate_speed=0.5)



#-------------------entry_Login----------------------
entryA = customtkinter.CTkEntry(FPage, placeholder_text="Name")
entryA.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

entryL = customtkinter.CTkEntry(FPage, show="*", placeholder_text="Pin")
entryL.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

#-----------------------entry_Reg------------------------

regbtn = customtkinter.CTkButton(FPage, text="Register", fg_color="#EE7023", command=reg_btn)

regbtn2 = customtkinter.CTkButton(RegPage, text="Register", fg_color="#EE7023", command=reg_acc)
returnbtn = customtkinter.CTkButton(RegPage, text="↩", command=ret)

entryFname = customtkinter.CTkEntry(RegPage, placeholder_text="Name")
entrySname = customtkinter.CTkEntry(RegPage, placeholder_text="Surname")

entryPassword = customtkinter.CTkEntry(RegPage, show="*", placeholder_text="Pin")



#-----------------------buttons-----------------------
loginbtn = customtkinter.CTkButton(FPage, text="Login", fg_color="#EE7023", command=loginB)

dark_light_button = customtkinter.CTkSwitch(FPage, text="", command=switch_E_DL)



#--------------------place_FPage-----------------------
loginbtn.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
regbtn.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
dark_light_button.place(relx=0.9, rely=0.1)


#--------------------place_RegPage--------------------
entryFname.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
entrySname.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
entryPassword.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
returnbtn.place(relx=0.1, rely=0.1)
regbtn2.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
entryA.focus()

app.mainloop()



'''
Class
	Account
		number - ska vara slumpat och unique
		pincode - 4 siffror
		fname
		lname
		balance - float ex: 302,39
GUI
	logga in
		ta ut och in pengar
		överföra till andra konton

'''




