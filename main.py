import keyboard
import time
import json
import customtkinter
import subprocess


writeconfig = {'write0': None , 'write1': None, 'write2': None, 'write3': None, 'write4': None, 'write5': None, 'write6': None, 'write7': None, 'write8': None}

pressconfig = {'press0': None, 'press1': None, 'press2': None, 'press3': None, 'press4': None, 'press5': None, 'press6': None, 'press7': None, 'press8': None}

holdconfig = {'hold0': None, 'hold1': None, 'hold2': None, 'hold3': None, 'hold4': None, 'hold5': None, 'hold6': None, 'hold7': None, 'hold8': None}

combinedconfig = {"writeconfig" : writeconfig , "pressconfig" : pressconfig , "holdconfig": holdconfig}

try:
    with open("config.json", "r") as file:
        loaded_data = json.load(file)
except FileNotFoundError:
    with open("config.json" , mode="+w") as file : 
        json.dump(combinedconfig , file , indent=4)
    with open("config.json", "r") as file:
        loaded_data = json.load(file)


writeconfig = loaded_data["writeconfig"]
pressconfig = loaded_data["pressconfig"]
holdconfig = loaded_data["holdconfig"]
combinedconfig = {"writeconfig" : writeconfig , "pressconfig" : pressconfig , "holdconfig": holdconfig}

class hold():  
    def __init__(self, button = "" , holdtime = 0):
        self.hotkey = ""
        self.button  = button
        self.holdtime = holdtime
        self.settings = [self.hotkey , self.button , int(self.holdtime)]

    def hold(self):
        keyboard.press(self.button)
        time.sleep(self.holdtime)
        keyboard.release(self.button)

    def active(self):
        self.ctkholdtime= customtkinter.CTkEntry(main , width=60 , height=40 , corner_radius=10 ,placeholder_text="holdtime")
        self.ctkholdtime.place(x =  300 , y = 130)
        self.ctktimesentry = customtkinter.CTkEntry(main , width=60 , height=40 , corner_radius=10 ,placeholder_text="times")
        self.ctktimesentry.place(x =  200 , y = 130)
        self.ctkbuttonbind = customtkinter.CTkButton(main , width=60 , height=40 , corner_radius=10 , text= "use" , command=self.keybind)
        self.ctkbuttonbind.place(x = 400 , y = 130)
        self.ctksavebutton = customtkinter.CTkButton(main , width=60 , height=40 , corner_radius=10 , text= "save" , command=self.save )
        self.ctksavebutton.place(x = 500 , y = 130)

    def keybind(self):
        self.button = keyboard.read_key()
        self.ctkbuttonbind.configure(text = self.button)

    def destroy(self):
        self.ctkholdtime.destroy()
        self.ctktimesentry.destroy()
        self.ctkbuttonbind.destroy()
        self.ctksavebutton.destroy()

    def save(self):
        self.hotkey = ctkhotkeybutton.cget("text")
        self.button = self.ctkbuttonbind.cget("text")
        self.times = self.ctktimesentry.get()
        self.holdtime = self.ctkholdtime.get() #only pasted , need make normal save
        self.settings = [self.hotkey , self.button , int(self.holdtime) , int(self.times)]
        for i in range(0, 9 ) : 
            if holdconfig[f"hold{i}"] != None : 
                pass
            else : 
                holdconfig[f"hold{i}"] = self.settings
                with open("config.json" , mode="+w") as file : 
                    json.dump(combinedconfig , file , indent=4)
                break


class press():
    def __init__(self , times = 1  , button = "", delay = 0 ):
        self.hotkey = ""
        self.times = times
        self.button = button
        self.delay = delay

        self.settings = [self.hotkey , self.button , int(self.times) , int(self.delay)]

    def press(self):
        for i in range(self.times):
            keyboard.press_and_release(f"{self.button}")
            time.sleep(self.delay)

    def save(self):
        self.hotkey = ctkhotkeybutton.cget("text")
        self.button = self.ctkbuttonbind.cget("text")
        self.times = self.ctktimesentry.get()
        self.delay = self.ctkdelayentry.get()
        self.settings = [self.hotkey , self.button , int(self.times) , int(self.delay)]
        for i in range(0, 9 ) : 
            if pressconfig[f"press{i}"] != None : 
                pass
            else : 
                pressconfig[f"press{i}"] = self.settings
                with open("config.json" , mode="+w") as file : 
                    json.dump(combinedconfig , file , indent=4)
                break


    def active(self):
        self.ctkdelayentry = customtkinter.CTkEntry(main , width=60 , height=40 , corner_radius=10 ,placeholder_text="delay")
        self.ctkdelayentry.place(x =  300 , y = 130)
        
        self.ctktimesentry = customtkinter.CTkEntry(main , width=60 , height=40 , corner_radius=10 ,placeholder_text="times")
        self.ctktimesentry.place(x =  200 , y = 130)
        self.ctkbuttonbind = customtkinter.CTkButton(main , width=60 , height=40 , corner_radius=10 , text= "use" , command=self.hotkeybind)
        self.ctkbuttonbind.place(x = 400 , y = 130)
        self.ctksavebutton = customtkinter.CTkButton(main , width=60 , height=40 , corner_radius=10 , text= "save" , command=self.save )
        self.ctksavebutton.place(x = 500 , y = 130)

    
    def destroy(self):
        self.ctkdelayentry.destroy()
        self.ctktimesentry.destroy()
        self.ctkbuttonbind.destroy()
        self.ctksavebutton.destroy()

    def hotkeybind(self):
        self.button = keyboard.read_key()
        self.ctkbuttonbind.configure(text = self.button)

# class repeatcombination():
#     def __init__(self , combination = " ", times = 1 , delay = 0 ):
#         self.hotkey = ""
#         self.combination = combination
#         self.times = times
#         self.delay = delay
#         self.settings = [self.hotkey , self.combination , self.times , self.delay]
#     def repeatcombination(self):
#     #print(keyboard.read_hotkey()
#         for i in range(self.times):
#             keyboard.press_and_release(self.combination)
#             time.sleep(self.delay)
    
#     def save(self):pass
    
class write():
    def __init__(self , text = "" , delay = 0):
        self.hotkey = ""
        self.text = text
        self.delay = delay
        self.settings = [self.hotkey , self.text , self.delay]
    def write(self):
        keyboard.write(f"{self.text}",delay=self.delay)


    def active(self): 
        self.ctktextentry = customtkinter.CTkEntry(main,width=200 , height=60 , placeholder_text="text")
        self.ctktextentry.place(x = 250 , y =120)
        self.ctksavebutton = customtkinter.CTkButton(main , width=60 , height=40 , corner_radius=10 , text= "save" , command=self.save)
        self.ctksavebutton.place(x = 500 , y = 130)
        
    def destroy(self) : 
        self.ctktextentry.destroy()
        self.ctksavebutton.destroy()

    def save(self):
        self.hotkey = ctkhotkeybutton.cget("text")
        self.text = self.ctktextentry.get()
        self.settings = [self.hotkey , self.text]
        for i in range(0, 9 ) : 
            if writeconfig[f"write{i}"] != None : 
                pass
            else : 
                writeconfig[f"write{i}"] = self.settings
                with open("config.json" , mode="+w") as file : 
                    json.dump(combinedconfig , file , indent=4)
                break
   

holdscript = hold()
pressscript = press()
#repeatcombinationscript = repeatcombination()
writescript = write()
   


# hold - button holdtime  , # press - times , button , delay , # repeatcombination - times , delay , combination , hotkey ,  # write - text  , delay , hotkey
def comboboxcheck(choice):
    ctkhotkeybutton.place(x = 130 , y = 130)
    ctkcombobox.configure(values = ["press" , "hold" , "write"] , width=90 , height=28)
    ctkcombobox.place(x = 10 , y = 135)
    ctkstartbutton.place(x = 220 , y = 250)
    ctkstartlabel.destroy()
    match choice:
            
            case "press" :
                try : holdscript.destroy()
                except AttributeError : pass

                try : writescript.destroy()
                except AttributeError : pass

                pressscript.active() # press - times+ , button , delay+ , +hotkey

                ctkcombobox.configure(values = ["hold" , "write"] , width=90 , height=28)



            case "hold" : # hold - button holdtime , hotkey
                try :pressscript.destroy()
                except AttributeError : pass

                try :writescript.destroy()
                except AttributeError : pass

                holdscript.active()

                ctkcombobox.configure(values = ["press" , "write"] , width=90 , height=28)


            case "write" :
                try : pressscript.destroy()
                except AttributeError : pass

                try : holdscript.destroy()
                except AttributeError : pass
                
                writescript.active()# write - text  , delay , hotkey

                ctkcombobox.configure(values = ["press" , "hold"] , width=90 , height=28)

# with open("config.json",mode="w") as file:
#     json.dump(config, file)


def hotkeybind():
    hkey = keyboard.read_key()
    ctkhotkeybutton.configure(text = hkey)

def startbinder():
    # Используем флаг CREATE_NO_WINDOW чтобы скрыть консоль
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    subprocess.Popen(
        ["python", "start.py"],
        startupinfo=startupinfo,
    )
    
main = customtkinter.CTk()
main.geometry("600x300")
main.title("keybinderPy by dveg")


#width-ширина,  height-высота

ctkhotkeybutton = customtkinter.CTkButton(main , width=60 , height=40 , corner_radius=10 , text= "hotkey" , command=hotkeybind )
# ctkentry = customtkinter.CTkEntry(main , width=60 , height=40 , corner_radius=10 ,placeholder_text="")
# ctkentry.place(x = 400 , y = 130)

#ctkcombobox = customtkinter.CTkComboBox(main, width=90 , height=28 ,values=[" " , "press" , "hold" , "repeatcombination", "write"] , command=comboboxcheck)
#ctkcombobox.place(x = 90 , y = 135)

ctkcombobox = customtkinter.CTkComboBox(main, width=200 , height=80 ,values=[ "press" , "hold" , "write"] , command=comboboxcheck)
ctkcombobox.place(x = 200 , y = 135)
ctkstartlabel = customtkinter.CTkLabel(main , corner_radius= 20 , text="choose bind")
ctkstartlabel.place(x = 250 , y = 13)


ctkstartbutton = customtkinter.CTkButton(main, corner_radius=10 , text="start binder " , command=startbinder)
main.mainloop()