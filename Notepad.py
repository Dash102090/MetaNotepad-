from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
import os


Current_file = None


#Sets Background color
#===============================================================
def color_wheel():

    color = colorchooser.askcolor(title='Choose a Color')

    text_area.config(bg=color[1])
#===============================================================


#Sets foreground color
#===============================================================
def text_color_wheel():
    text_color = colorchooser.askcolor(title='Choose a Color')

    text_area.config(fg=text_color[1])
#===============================================================


#Lists of Font styles
#===============================================================
def Lists():
    global listbox_1, listbox_2, listbox_3, new_window,x, label_of_sample

    new_window=Toplevel(window)

    new_window.geometry('500x400')
    new_window.title('FONTS - Meta Notepad')
    new_window.resizable(False, False)


    frame = Frame(new_window)
    frame.pack()

    labeloffont = Label(frame, text='Font', fg="#5E69D3", font=('Algerian'))
    labeloffont.place(x=60, y=15)

    listbox_1 = Listbox(frame, font=('Constantia', 15, 'bold'), width=13, height=5, exportselection=False)
    listbox_1.pack(side=LEFT, padx=10)

    fonts = [
        'Ariel', 'Comic Sans MS', 'Constantia', 'Ink Free', 'Algerian',
        'Jokerman', 'Chiller', 'Harlow Solid Italic', 'Arial Black', 'Courier New',
        'Viner Hand ITC', 'Franklin Gothic Medium', 'Georgia', 'Verdana'
    ]

    for i in fonts:
        listbox_1.insert(END,i)
    

    labeloffontstyle = Label(frame, text='Font Style', fg='#646EC8', font=('Algerian'))
    labeloffontstyle.place(x=200, y=15)

    listbox_2 = Listbox(frame, font=('Constantia', 15, 'bold'), width=10, height=5, exportselection=False)
    listbox_2.pack(side=LEFT, pady=40)

    fontstyle = [
        'normal', 'bold', 'italic', 'bold italic'
    ]

    for i in fontstyle:
        listbox_2.insert(END, i)

    labeloffontsize = Label(frame, text='Font Size', fg='#646EC8', font=('Algerian'))
    labeloffontsize.place(x=305, y=15)

    listbox_3 = Listbox(frame, font=('Constantia', 15, 'bold'), width=5, height=5, exportselection=False)
    listbox_3.pack(side=RIGHT, pady=40, padx=10)

    i = 0
    for _ in range(15):
        i += 5
        listbox_3.insert(END, i)

    label_of_sample = Label(new_window, text='TEXT',font=('Arial', 20, 'bold'), bg="white",relief='groove')
    label_of_sample.place(x=65, y=190, width=150, height=70)

    Check_button = Button(new_window, text='Check Font Style', command=check_font)
    Check_button.place(x=65, y=270)

    OK_Button = Button(new_window, text='OK', command=FontStyle, bg="#E6F4FC", 
                       fg="#0F2938", width=10, activebackground="#4BBCF8", 
                       activeforeground='White', bd=3, relief='ridge')
    OK_Button.place(x=310, y=300)

    Cancel_Button = Button(new_window, text='Cancel', command=Cancel,
                            activebackground="#DF0505", activeforeground="#FFFFFF",
                           width=10, bd=3, relief='ridge')
    Cancel_Button.place(x=400, y=300)
#===============================================================

def check_font():

    font_style_2 = 'bold'
    font_style='Arial'

    global listbox_2, listbox_1

    if listbox_1.curselection():
        font_style = listbox_1.get(listbox_1.curselection()[0])

    if listbox_2.curselection():
        font_style_2 = listbox_2.get(listbox_2.curselection()[0])

    label_of_sample.config(font=(font_style, 20, font_style_2))

#Cancel Button
#===============================================================
def Cancel():

    new_window.destroy()
#===============================================================


#Toogles underline, overstrike and normal
#===============================================================
def toogle():
    global underline_on, overstrike_on, normal_mode

    if x.get() == 'underline':
        underline_on = True
        underline = 'underline'
        text_area.config(font=(current_font, current_size, current_font_style + ' ' + underline))

    elif x.get() == 'overstrike':
        overstrike_on = True
        overstrike = 'overstrike'
        text_area.config(font=(current_font, current_size, current_font_style + ' ' + overstrike))

    elif x.get() == 'normal':
        normal_mode = True
        text_area.config(font=(current_font, current_size, current_font_style))
#===============================================================


#Edits Font style
#===============================================================
current_font='Ariel'
current_font_style='normal'
current_size=15
overstrike_on=''
normal_mode=''
underline_on=''


def FontStyle():

    global current_font, current_font_style, current_size, underline_on, overstrike_on, normal_mode


    if listbox_1.curselection():
        current_font = listbox_1.get(listbox_1.curselection()[0])

    if listbox_2.curselection():
        current_font_style = listbox_2.get(listbox_2.curselection()[0])

    if listbox_3.curselection():
        current_size = listbox_3.get(listbox_3.curselection()[0])

    if underline_on:
        underline_on = 'underline'
        text_area.config(font=(current_font, current_size, current_font_style + ' ' + underline_on))
    
    if overstrike_on:
        overstrike_on = 'overstrike'
        text_area.config(font=(current_font, current_size, current_font_style + ' ' + overstrike_on))

    if normal_mode:
        normal_mode = 'normal'
        text_area.config(font=(current_font, current_size, current_font_style + ' ' + normal_mode))

    if not normal_mode and not overstrike_on and not underline_on:
        text_area.config(font=(current_font, current_size, current_font_style))

    new_window.destroy()
#===============================================================


#Save files
#===============================================================
def save():
    global Current_file

    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ('Plain file', '.txt'),
                                        ('HTML file', '.html'),
                                        ('Python file', '.py'),
                                        ('All file', '.*')
                                        ])
    filetext = str(text_area.get(1.0, END))

    if file is None:
        return
    
    if file is not None:
        Current_file = file.name
        file_name = os.path.basename(Current_file)
        window.title(f'{file_name} - Meta Notepad')

    file.write(filetext)
    file.close()
#===============================================================


#Open files
#===============================================================
def openfile():
    global Current_file

    filepath = filedialog.askopenfilename(title='Open a File')
    if filepath:
        Current_file = filepath
        file_name = os.path.basename(Current_file)
        window.title(f'{file_name} - Meta Notepad')
    
    if not filepath:
        return

    with open (filepath, 'r') as f:
        content = f.read()

    text_area.delete(1.0, END)
    text_area.insert(END, content)
#===============================================================


#Creates New page
#===============================================================
def New_File():
    global current_font_style, current_font, current_size, Current_file

    Current_file = None
    window.title('untitled - Meta Notepad')

    text_area.delete(1.0, END)
    current_size = 15
    current_font = 'Arial'
    current_font_style = 'normal'
    text_area.config(bg='#FAF8CB', fg='Black', font=(current_font, current_size, current_font_style))
#===============================================================


#undo's
#===============================================================
def undo():
    try:
        text_area.edit_undo()
    except TclError:
        pass
#===============================================================


#Redo's
#===============================================================
def redo():
    try:
        text_area.edit_redo()
    except TclError:
        pass
#===============================================================


#Copy's
#===============================================================
def copy():
    try:
        selected = text_area.selection_get()
        window.clipboard_clear()
        window.clipboard_append(selected)
    except TclError:
        pass
#===============================================================


#Cut's
#===============================================================
def cut():
    try:
        selected = text_area.selection_get()
        window.clipboard_clear()
        window.clipboard_append(selected)
        text_area.delete('sel.first', 'sel.last')
    except TclError:
        pass
#===============================================================


#Paste's
#===============================================================
def paste():
    try:
        text_area.insert(INSERT, window.clipboard_get())

    except TclError:
        pass
#===============================================================


#Creates popup menu for mouse
#===============================================================
def context_popup(event):
    try:
        context_menu.tk_popup(event.x_root, event.y_root)
    finally:
        context_menu.grab_release()

#===============================================================


window = Tk()

window.geometry('700x500')

window.title('untitled -  Meta Notepad')

menubar = Menu(window)
window.config(menu=menubar)


#Highlights selected text
#===============================================================
def highlight_text():
    try:

        text_area.tag_remove('color', '1.0', 'end')

        text_area.tag_add('color', 'sel.first', 'sel.last')
        text_area.tag_config('color', background="#E07D7D", foreground="#DF0000")

    except:
        pass

#===============================================================


#Images
#===============================================================
New_Icon = PhotoImage(file='images/New_Icon.png')
Save_Icon = PhotoImage(file='images/Save_Icon.png')
Open_Icon = PhotoImage(file='images/Open_Icon.png')
Exit_Icon = PhotoImage(file='images/Exit_Icon.png')
Text_Color_Icon = PhotoImage(file='images/Text_Color_Icon.png')
Color_Wheel_Icon = PhotoImage(file='images/Color_Wheel_Icon.png')
Notepad_Icon = PhotoImage(file='images/Notepad_Icon.png')
Font_Icon = PhotoImage(file='images/Font_Icon.png')
Undo_Icon = PhotoImage(file='images/Undo_Icon.png')
Redo_Icon = PhotoImage(file='images/Redo_Icon.png')
#===============================================================

window.iconphoto(True, Notepad_Icon)

#Creates a file bar
#===============================================================
file_bar = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file_bar)
file_bar.add_command(label='New', command=New_File, accelerator='Ctrl+N', image=New_Icon, compound='left')
file_bar.add_separator()
file_bar.add_command(label='Open', command=openfile, accelerator='Ctrl+O', image=Open_Icon, compound=LEFT)
file_bar.add_command(label='Save', command=save, accelerator='Ctrl+S', image=Save_Icon, compound=LEFT)
file_bar.add_separator()
file_bar.add_command(label='Exit', command=quit, accelerator='Ctrl+Q', image=Exit_Icon, compound=LEFT)
#===============================================================


#Creates an Edit bar
#===============================================================
Edit_bar = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=Edit_bar)
Edit_bar.add_command(label='Undo', command=undo, image=Undo_Icon, compound=LEFT, accelerator='Ctrl+Z')
Edit_bar.add_command(label='redo', command=redo, image=Redo_Icon, compound=LEFT, accelerator='Ctrl+Y')
Edit_bar.add_separator()
Edit_bar.add_command(label='copy', command=copy, accelerator='Ctrl+C')
Edit_bar.add_command(label='cut', command=cut, accelerator='Ctrl+X')
Edit_bar.add_command(label='paste', command=paste, accelerator='Ctrl+V')
#===============================================================


#Creates a formate bar
#===============================================================
format_bar = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Format', menu=format_bar)
x=StringVar()
format_bar.add_radiobutton(label='Toogle Underline', variable=x, value='underline', command=toogle)
format_bar.add_radiobutton(label='Toogle Overstrike', variable=x, value='overstrike', command=toogle)
format_bar.add_radiobutton(label='Toogle Normal', variable=x, value='normal',command=toogle)
format_bar.add_command(label='Fonts', command=Lists, image=Font_Icon, compound=LEFT)
#===============================================================


#Color bar
#===============================================================
colormenubar = Menu(menubar, tearoff=0)
colormenubar.add_command(label='Change Background Color', command=color_wheel, accelerator='Alt+B', image=Color_Wheel_Icon, compound=LEFT)
colormenubar.add_command(label='Change Text Color', command=text_color_wheel, accelerator='Alt+T', image=Text_Color_Icon, compound=LEFT)
menubar.add_cascade(label='Color', menu=colormenubar)
#===============================================================


#Creates a text area
#===============================================================
text_area = Text(window, font=('Arial', 15, 'normal'), bg="#FFFDE7", undo=True)
text_area.pack(fill='both', expand=True)
#===============================================================


#Creates mouse clipboard menu
#===============================================================
context_menu = Menu(window, tearoff=0)
context_menu.add_command(label='Copy', command=copy)
context_menu.add_command(label='Cut', command=cut)
context_menu.add_command(label='Paste', command=paste)
#===============================================================


#Key binds
#===============================================================
window.bind('<Control-o>', lambda event: openfile())
window.bind('<Control-s>', lambda event: save())
window.bind('<Alt-b>', lambda event: color_wheel())
window.bind('<Alt-t>', lambda event: text_color_wheel())
window.bind('<Control-n>', lambda event: New_File())
window.bind('<Control-q>', quit)
window.bind('<Control-c>', lambda event: copy())
window.bind('<Control-v>', lambda event: paste())
window.bind('<Control-z>', lambda event: undo())
window.bind('<Control-x>', lambda event: cut())
window.bind('<Control-y>', lambda event: redo())
text_area.bind('<Button-3>', context_popup)
window.bind('<Alt-h>', lambda event: highlight_text())
#===============================================================


window.mainloop()
