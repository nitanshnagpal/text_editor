import tkinter as tk
from tokenize import String
import aspose.words as aw

# Import module
import tkinter
import tkinter.font
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor Application - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="doc",
        filetypes=[("Doc Files", "*.doc"), ("All Files", "*.*")],
    )
    if not filepath:
        return

    save_doc(filepath)
    window.title(f"Text Editor Application - {filepath}")

def save_doc(file_path):

    # create document object
    doc = aw.Document()

    # create a document builder object
    builder = aw.DocumentBuilder(doc)
    font = builder.font
    if font_size_input.compare("end-1c", "==", "1.0"):
        font.size = 12
    else:
        font.size = (int)(font_size_input.get(1.0, tk.END))
    
    if(CheckVar1.get() == 1):
        font.bold = True
    else:
        font.bold = False

    if(CheckVar2.get() == 1):
        font.underline = aw.Underline.DASH
  

    font.name = clicked.get()
    #font.underline = aw.Underline.DASH
    text = txt_edit.get(1.0, tk.END)
    # add text to the document
    builder.write(text)

    # save document
    doc.save(file_path)


def show():
  
    font_size = 12

    if font_size_input.compare("end-1c", "==", "1.0"):
        font_size = 12
    else:
        font_size = (int)(font_size_input.get(1.0, tk.END))

    underline_check = False
    if(CheckVar2.get() == 1):
        underline_check = True
    else:
        underline_check = False

    if(CheckVar1.get() == 1):
        Desired_font = tkinter.font.Font( family = clicked.get(), 
                                    size = font_size, 
                                    weight = "bold",
                                    underline=underline_check)
    else:
         Desired_font = tkinter.font.Font( family = clicked.get(), 
                                    size = font_size, 
                                    weight= "normal",
                                    underline=underline_check)
    txt_edit.configure( font = Desired_font)

options = [
    "Courier",
    "Arial",
    "Bahnschrift Light",
    "Microsoft JhengHei UI",
    "Impact",
    "Segoe UI Light",
    "Segoe UI"
]

window = tk.Tk()
window.title("Text Editor Application")

window.geometry("420x500")
window.resizable(False, False)

clicked = StringVar()
labelText = StringVar()
labelText.set("Text Editor")
  
# initial menu text
clicked.set( "Courier" )

# Create Label
label = Label( window , text = "Text Editor" )
label.place(x=160, y=0,width=100, height=20)

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
fr_buttons.place(x=10, y=30, width=100, height = 30)

txt_edit = tk.Text(window)
txt_edit.place(x=10, y=100, width= 400, height= 300)

fr_edit = tk.Frame(window, relief=tk.RAISED, bd=2)
fr_edit.place(x=10, y=450, width=400, height = 40)


btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
# Create Dropdown menu
drop = OptionMenu( fr_edit , clicked , *options )
drop.pack(side=LEFT)

font_size_input = tk.Text(fr_edit, width=30, height=20)
font_size_input.place(x=320,y=10, width=30, height=20)
  
# Create button, it will change label text
button = Button( fr_edit , text = "click Me" , command = show ).pack(side=LEFT)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(fr_edit, text = "Bold", variable = CheckVar1, 
                 onvalue = 1, offvalue = 0)
C1.pack(side=LEFT)

C2 = Checkbutton(fr_edit, text = "UnderLine", variable = CheckVar2, 
                 onvalue = 1, offvalue = 0)
C2.pack(side=LEFT)
font_size_label = Label(fr_edit,  text = "Font Size")
font_size_label.pack(side=LEFT)

btn_open.pack(side=LEFT)
btn_save.pack(side=LEFT)

window.mainloop()
