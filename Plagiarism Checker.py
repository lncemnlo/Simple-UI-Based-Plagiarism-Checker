from difflib import SequenceMatcher
import tkinter as tk
from tkinter import filedialog, Text, messagebox

checkPlag = tk.Tk()


class commands():
        def addText1():
                global text1_data
                text1 = filedialog.askopenfilename(initialdir="/", title="Select File #1",
                filetypes=(("Text Files", ".txt"),("All Files", "*.*")))
                text1 = open(text1, 'r')
                text1_data = text1.read()
                text1_show.insert(tk.END, text1_data)
                text1.close

        def addText2():
                global text2_data
                text2 = filedialog.askopenfilename(initialdir="/", title="Select File #2",
                filetypes=(("Text Files", ".txt"),("All Files", "*.*")))
                text2 = open(text2, 'r')
                text2_data = text2.read()
                text2_show.insert(tk.END, text2_data)
                text2.close

        def checkFile():
                global text1_data, text2_data, similarity
                try:
                        text1_data, text2_data
                except NameError:
                        messagebox.showinfo("Error", "Please make sure to select files using the button below! Then try again thank you. :)")
                else:
                        similarity=SequenceMatcher(None,text1_data,text2_data).ratio()
                        messagebox.showinfo("Details", f"Percentage of Plagiarized Content: {similarity*100}%")
        
        def clearVal():
                global text1_data, text2_data, text1_show, text2_show, similarity
                text1_data = None
                text1_show.delete("1.0", "end")
                text2_data = None
                text2_show.delete("1.0", "end")
                similarity = None
                


checkPlag.geometry("1280x720")
checkPlag.configure(background="black")
fr1=tk.Frame(checkPlag)
fr1.pack(side="top")
bg_image = tk.PhotoImage(file = "bgmenu.png")
bg_menu = tk.Label (image = bg_image)
bg_menu.place(relheight=1, relwidth=1)

openFile1 = tk.Button(checkPlag, text="Open File #1", padx=10, 
pady=5, fg="white", bg="#263D42", command=commands.addText1)
openFile1.place(x=655, y=600)

openFile2 = tk.Button(checkPlag, text="Open File #2", padx=10,
pady=5, fg="white", bg="#263D42", command=commands.addText2)
openFile2.place(x=1015, y=600)

checkFile = tk.Button(checkPlag, text="Check Now", padx=10,
pady=5, fg="white", bg="#263D42", command=commands.checkFile)
checkFile.place(x=835, y=620)

clearVal = tk.Button(checkPlag, text="Try Again", padx=10,
pady=5, fg="white", bg="#263D42", command=commands.clearVal)
clearVal.place(x=841, y=657)

text1_show = Text(checkPlag, width=40, height=35, bg="white")
text1_show.place(x=540, y=25)
text2_show = Text(checkPlag, width=40, height=35, bg="white")
text2_show.place(x=900, y=25)
checkPlag.title("Plagiarism Checker")
checkPlag.mainloop()