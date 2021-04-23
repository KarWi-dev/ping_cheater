# Version 2.1
# please enter username and password for launcher
username = str("username")
password = str("password")


import time
import subprocess
import sys

try:
    import tkinter as tk
    from tkinter import messagebox
except:
    subprocess.check_call('pip install tk-tools')
    import tkinter as tk
    from tkinter import messagebox

if sys.version_info[0] == 3 and sys.version_info[1] == 9:
    messagebox.showerror("version error", "Python 3.9 not supported")
    exit()

try:
    import pyautogui
except:
    subprocess.check_call('pip install PyAutoGui')
    import pyautogui
try:
    import cv2
except:
    subprocess.check_call('pip install opencv-python')
    import cv2

try:
    import pytesseract
except:
    subprocess.check_call('pip install pytesseract')
    import pytesseract

try:
    from PIL import Image
except:
    subprocess.check_call('pip install pillow')
    from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Programme\Tesseract-OCR\tesseract.exe'


def btn_change():
    global onoff

    if onoff == False or None:
        onoff = True
        lbl_on["text"] = "Active!!"
        lbl_on["bg"] = "Green"
    else:
        onoff = False
        lbl_on["text"] = "Not active!!"
        lbl_on["bg"] = "Red"


def btn_exit():
    global onoff
    global timedsd

    if timedsd:
        if messagebox.askyesno(title="warning!", message="Auto shutdown active!\n\nWant do deactivate?",
                                     default=messagebox.YES):
            timedsd = False
            subprocess.check_call('shutdown -a')
            root.destroy()
        else:
            onoff = False
            root.destroy()
    else:
        onoff = False
        root.destroy()


def btn_shutdown():

    def btn_cancel():
        global timedsd
        timedsd = False
        subprocess.check_call('shutdown -a')
        sd.destroy()


    def btn_ok():
        global timedsd
        timedsd = True
        time = int(ntr_minutes.get()) * 60
        subprocess.check_call('shutdown -s -t ' + str(time))
        sd.destroy()


    sd = tk.Toplevel(root)
    sd.title("auto Shutdown")
    sd.geometry("195x50+350+150")
    ntr_minutes = tk.Entry(sd, borderwidth=2)
    ntr_minutes.insert(0, "[minutes]")
    btn_ok = tk.Button(sd, text="***OK***", borderwidth=2, command=btn_ok)
    btn_canel = tk.Button(sd, text="***cancel Shutdown***", borderwidth=2, command=btn_cancel)

    ntr_minutes.grid(row=0, columnspan=4, sticky="n")
    btn_ok.grid(row=1, sticky="sw", padx=2)
    btn_canel.grid(row=1, column=1, sticky="se", columnspan=2)


def restart(name, pw):
    try:
        subprocess.check_call('taskkill /im  java.exe /f')
    finally:
        time.sleep(5)
        subprocess.check_call("C:\\CCLauncher-Client-3\\CCLauncher_Client_3.0.exe")
        time.sleep(10)
        pyautogui.typewrite(name, interval=0.2)
        pyautogui.hotkey('tab')
        pyautogui.typewrite(pw, interval=0.2)
        pyautogui.hotkey('enter')


def login():
    restart(username, password)


def cheat():
    def ping_check():
        feld_pos = pyautogui.locateOnScreen(r'C:\ping_cheater\ping_buttons\ping_feld.png', confidence=0.5)

        if feld_pos is not None:
            ping_screen = pyautogui.screenshot(region=feld_pos)
            ping_screen.save(r'C:\ping_cheater\ping_screen.png')
        return feld_pos

    def find_numbers():
        search_img = cv2.imread(r'C:\ping_cheater\ping_screen.png')
        numberstring = pytesseract.image_to_string(search_img)
        numberstring = numberstring[162:167]
        return numberstring

    check_pos = ping_check()
    global numberold

    if check_pos is not None:
        number_long = find_numbers()

        if numberold == number_long:
            global repeat
            repeat = repeat + 1
        else:
            repeat = 0

        for x in number_long:
            time.sleep(1)
            if x == "0":
                fucku = pyautogui.locateOnScreen(r'C:\ping_cheater\ping_buttons\ping_0.png')
                pyautogui.click(fucku)
            elif x == "1":
                fucku = pyautogui.locateOnScreen(r'C:\ping_cheater\ping_buttons\ping_1.png')
                pyautogui.click(fucku)
            elif x == "2":
                fucku = pyautogui.locateOnScreen(r'C:\ping_cheater\ping_buttons\ping_2.png')
                pyautogui.click(fucku)
            elif x == "3":
                fucku = pyautogui.locateOnScreen(r'C:\ping_cheater\ping_buttons\ping_3.png')
                pyautogui.click(fucku)
            elif x == "4":
                fucku = pyautogui.locateOnScreen(r'C:\ping_cheater\ping_buttons\ping_4.png')
                pyautogui.click(fucku)
            elif x == "5":
                fucku = pyautogui.locateOnScreen(r'C:\ping_cheater\ping_buttons\ping_5.png')
                pyautogui.click(fucku)
            elif x == "6":
                fucku = pyautogui.locateOnScreen(r'C:\ping_cheater\ping_buttons\ping_6.png')
                pyautogui.click(fucku)
            elif x == "7":
                fucku = pyautogui.locateOnScreen(r'C:\ping_cheater\ping_buttons\ping_7.png')
                pyautogui.click(fucku)
            elif x == "8":
                fucku = pyautogui.locateOnScreen(r'C:\ping_cheater\ping_buttons\ping_8.png')
                pyautogui.click(fucku)
            elif x == "9":
                fucku = pyautogui.locateOnScreen(r'C:\ping_cheater\ping_buttons\ping_9.png')
                pyautogui.click(fucku)

        numberold = number_long
        time.sleep(1)
        fucku = pyautogui.locateOnScreen(r'C:\ping_cheater\ping_buttons\ping_absenden.png', confidence=0.8)
        pyautogui.click(fucku)
        time.sleep(15)


numberold = int()
repeat = int()
timedsd = bool(None)
onoff = bool(None)

root = tk.Tk()
root.title("Ping_Cheater")
root.geometry("240x150+300+100")

lbl_on = tk.Label(root, bg="grey", text="Please activate!")
btn_change = tk.Button(root, text="***on/off***", borderwidth=2, command=btn_change)
btn_shutdown = tk.Button(root, text="auto Shutdown", borderwidth=2, command=btn_shutdown)
btn_login = tk.Button(root, text="launcher login", borderwidth=2, command=login)
btn_exit = tk.Button(root, text="Exit", borderwidth=2, command=btn_exit)

lbl_on.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
btn_change.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
btn_shutdown.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
btn_login.pack(fill=tk.BOTH,side=tk.TOP, expand=True)
btn_exit.pack(fill=tk.BOTH, side=tk.TOP, expand=True)


while True:
    if onoff:
        if repeat == 2:
            restart(username, password)
            repeat = 0
        else:
            cheat()

    root.update_idletasks()
    root.update()
