import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
import subprocess
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox


main_application = tk.Tk()
main_application.geometry('1100x700')
main_application.title(' NoteFlow ')

############################################## main menu ###################################################
main_menu = tk.Menu()

# file
file = tk.Menu(main_menu, tearoff=False)

# edit
edit = tk.Menu(main_menu, tearoff=False)

#view 
view = tk.Menu(main_menu, tearoff=False)

# -------------------------------------&&&&&&&& End main menu &&&&&&&&&&& ----------------------------------


# ------------------------------------- ########  Code Function ###### ------------------------------------#

def code(event=None):
    class code:
        def __init__(self, root):
            self.root = root
            self.root.title("CodeingCraft")

            self.root.geometry("1200x750+0+0")

            self.path_name=''
            self.color_theme=StringVar()
            self.color_theme.set('Light blue')

            #================== File Menu =========================#
            Mymenu=Menu(self.root, bg="#36394F" , fg="#ffffff")
            Filemenu=Menu(Mymenu, tearoff=False, bg="#36394F" , fg="#ffffff")
            Filemenu.add_command(label='New File  ', compound=LEFT, accelerator="Ctrl+N", command=self.new_file)
            Filemenu.add_command(label='Open File  ', compound=LEFT, accelerator="Ctrl+O", command=self.open_file)
            Filemenu.add_separator()
            Filemenu.add_command(label='Save  ', compound=LEFT, accelerator="Ctrl+S", command=self.save_file)
            Filemenu.add_command(label='Save As  ', compound=LEFT, accelerator="Ctrl+w", command=self.save_as_file)
            Filemenu.add_separator()
            Filemenu.add_command(label='Exit  ', compound=LEFT, accelerator="Ctrl+Q", command=self.exit_function)

            # =========================== Edit ===========================================#
            edit = Menu(Mymenu, tearoff=False, bg="#36394F" , fg="#ffffff")
            edit.add_command(label='Copy', compound=LEFT, accelerator='Ctrl+C', command=lambda: self.txt_editor.event_generate("<Control c>"))
            edit.add_command(label='Paste', compound=LEFT, accelerator='Ctrl+V', command=lambda: self.txt_editor.event_generate("<Control v>"))
            edit.add_separator()
            edit.add_command(label='Find & Replace', compound=LEFT, accelerator='Ctrl+F', command=self.find_func)
            edit.add_command(label='Run', compound=LEFT, accelerator='Ctrl+R', command=self.run)
            edit.add_separator()
            edit.add_command(label='Cut', compound=LEFT, accelerator='Ctrl+X', command=lambda: self.txt_editor.event_generate("<Control x>"))
            edit.add_command(label='Clear All', compound=LEFT, accelerator='Ctrl+Alt+X', command=lambda: self.txt_editor.delete(1.0, END))

            ############################### Tool Bar #######################################
            Mymenu.add_cascade(label="File", menu=Filemenu)
            Mymenu.add_separator()
            Mymenu.add_cascade(label="Edit", menu=edit)
            Mymenu.add_separator()
            Mymenu.add_cascade(label="Clear", command=self.clear_all)
            Mymenu.add_separator()
            Mymenu.add_cascade(label="Find & Replace", command=self.find_func)
            Mymenu.add_separator()
            Mymenu.add_cascade(label="Run File", command=self.run)
            self.root.config(menu=Mymenu)

            #============================= Input Frame ===============================================#
            self.font_size1 = 18

            EditorFrame=Frame(self.root, bg="#191B29")
            EditorFrame.place(x=0, y=0, relwidth=1, height=500)

            scroll = Scrollbar(EditorFrame, orient=VERTICAL)
            scroll.pack(side=RIGHT, fill=Y)
            self.txt_editor=Text(EditorFrame, bg="#191B29", fg="#2440FB", font=("time new roman", self.font_size1), yscrollcommand=scroll.set)
            self.txt_editor.pack(fill=BOTH, expand=1)
            scroll.config(command=self.txt_editor.yview)
            #################################### End Of Input Frame ###################################

            self.font_size = 15

            #################################### Output Frame ##################################
            outputFrame = Frame(self.root, bg="white")
            outputFrame.place(x=0, y=500, relwidth=1, height=400)

            scroll1 = Scrollbar(outputFrame, orient=VERTICAL)
            scroll1.pack(side=RIGHT, fill=Y)
            self.txt_output = Text(outputFrame, bg = "#36394F", fg = "#5DE2E7", font=("Segoe UI Symbol", self.font_size), yscrollcommand=scroll1.set)
            self.txt_output.pack(fill=BOTH, expand=1)
            scroll1.config(command=self.txt_output.yview)
            ################################# End Of Output Frame ###################################3333

            # ==================== Sutcut Bind Key ===========================================
            self.root.bind('<Control-plus>', self.font_size_inc)
            self.root.bind('<Control-minus>', self.font_size_dec)
            self.root.bind('<Control-0>', self.font_size_rel)
            self.root.bind('<Control-s>', self.save_file)
            self.root.bind('<Control-w>', self.save_as_file)
            self.root.bind('<Control-r>', self.run)
            self.root.bind('<Control-f>', self.find_func)
            self.root.bind('<Control-x>', self.clear_all)
            self.root.bind('<Control-n>', self.new_file)
            self.root.bind('<Control-q>', self.exit_function)
            self.root.bind('<Control-o>', self.open_file)

        # ========================== Zoom =========================================

        #******************* Zoom In ***********************************
        def font_size_inc(self, event=None):
            self.font_size1 += 1
            self.txt_editor.config(font=('times new romen', self.font_size1))

        #************************ Zoom Out ******************************
        def font_size_dec(self, event=None):
            self.font_size1 -= 1
            self.txt_editor.config(font=('times new romen', self.font_size1))

        #*********************** Zoom Rel *****************************
        def font_size_rel(self, event=None):
            self.font_size1 = 18
            self.txt_editor.config(font=('times new romen', self.font_size1))


        ################################ find functionality #########################
        def find_func(self, event=None):
            def find():
                word = find_input.get()
                self.txt_editor.tag_remove('match', '1.0', END)
                matches = 0
                if word:
                    start_pos = '1.0'
                    while True:
                        start_pos = self.txt_editor.search(word, start_pos, stopindex=END)
                        if not start_pos:
                            break
                        end_pos = f'{start_pos}+{len(word)}c'
                        self.txt_editor.tag_add('match', start_pos, end_pos)
                        matches += 1
                        start_pos = end_pos
                        self.txt_editor.tag_config('match', foreground='red', background='yellow')

            def replace():
                word = find_input.get()
                replace_text = replace_input.get()
                content = self.txt_editor.get(1.0, END)
                new_content = content.replace(word, replace_text)
                self.txt_editor.delete(1.0, END)
                self.txt_editor.insert(1.0, new_content)

            find_dialogue = Toplevel()
            find_dialogue.geometry('450x250+500+200')
            find_dialogue.title('Find')
            find_dialogue.resizable(0, 0)

            ## frame
            find_frame = LabelFrame(find_dialogue, text='Find/Replace')
            find_frame.pack(pady=20)

            ## labels
            text_find_label = Label(find_frame, text='Find : ')
            text_replace_label = Label(find_frame, text='Replace')

            ## entry
            find_input = Entry(find_frame, width=30)
            replace_input = Entry(find_frame, width=30)

            ## button
            find_button = Button(find_frame, text='Find', cursor='hand2', command=find)
            replace_button = Button(find_frame, text='Replace', cursor='hand2', command=replace)

            ## label grid
            text_find_label.grid(row=0, column=0, padx=4, pady=4)
            text_replace_label.grid(row=1, column=0, padx=4, pady=4)

            ## entry grid
            find_input.grid(row=0, column=1, padx=4, pady=4)
            replace_input.grid(row=1, column=1, padx=4, pady=4)

            ## button grid
            find_button.grid(row=2, column=0, padx=8, pady=4)
            replace_button.grid(row=2, column=1, padx=8, pady=4)

            find_dialogue.mainloop()

            #======================================================================#
        
        
        #==================== Run Function ===============================================#
        def run(self, event=None):
            if self.path_name == '':
                messagebox.showerror('Error', 'Please save the file to run the code', parent=self.root)
            else:
                fp = open(self.path_name, 'w')
                fp.write(self.txt_editor.get('1.0', END))
                fp.close()
                command = f'python {self.path_name}'
                run_file = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                output, error = run_file.communicate()

                # Insert path name followed by a space
                self.txt_output.insert(END, self.path_name + '  ~/ ' + '\n')

                # Insert output followed by a newline
                self.txt_output.insert(END, output.decode('utf-8') + '\n')

                # Insert error followed by a newline
                self.txt_output.insert(END, error.decode('utf-8'))


        # ================= Clear All Function ==========================================
        def clear_all(self, event=None):
            self.txt_editor.delete('1.0', END)
            self.txt_output.delete('1.0', END)

        # +++++++++++++++++++++++++++++++ Exit Function ++++++++++++++++++++++++++++++++++++
        def exit_function(self, event=None):
            url = ''
            text_changed = True
            try:
                if text_changed:
                    mbox = messagebox.askyesnocancel('Warning', 'Do you want to save this code ?')
                    if mbox is True:
                        if url:
                            content = self.txt_editor.get(1.0, END)
                            with open(url, 'w', encoding='utf-8') as fw:
                                fw.write(content)
                                self.root.destroy()
                        else:
                            content2 = str(self.txt_editor.get(1.0, END))
                            url = filedialog.asksaveasfile(mode='w', defaultextension='.py',
                                                        filetypes=(('python', '*.py'), ('All files', '*.*')))
                            url.write(content2)
                            url.close()
                            self.root.destroy()
                    elif mbox is False:
                        self.root.destroy()
                else:
                    self.root.destroy()
            except:
                return

        # -------------------------------- New File ---------------------------------
        def new_file(self, event=None):
            self.path_name=''
            self.txt_editor.delete('1.0', END)
            self.txt_output.delete('1.0', END)

        ################################# Save File ############################
        def save_file(self, event=None):
            if self.path_name=='':
                self.save_as_file()
            else:
                fp=open(self.path_name,'w')
                fp.write(self.txt_editor.get('1.0', END))
                fp.close()

        ############################## Open FIle Function ##########################
        def open_file(self, event=None):
            path=filedialog.askopenfilename(filetypes=[('Python', '*.py')], defaultextension=('*.*'))
            if path!='':
                self.path_name=path
                fp=open(self.path_name, "r")
                data=fp.read()
                self.txt_editor.delete('1.0', END)
                self.txt_editor.insert('1.0', data)
                fp.close()

        ################################## Save As File Function #####################
        def save_as_file(self, event=None):
            path=filedialog.asksaveasfilename(filetypes=[('python File', '*.py')], defaultextension=('.py'))
            if path!='':
                self.path_name=path
                fp=open(self.path_name, "w")
                fp.write(self.txt_editor.get('1.0', END))
                fp.close()

    root = Tk()
    obj = code(root)
    root.mainloop()
# ------------------------------------- ########  End Of Code Function ###### ------------------------------------#


# ------------------------------------- ########  Translator Function ###### ------------------------------------#

def translator(event=None):
    root = Tk()
    root.title('LangTranslate')
    root.resizable(False, False)
    root.configure(bg='#078984')
    root.geometry("880x300")

    def translate_it():
        # Delete Any Previous Translations
        translated_text.delete(1.0, END)

        try:
            # Get Languages From Dictionary Keys
            # Get the From Langauage Key
            for key, value in languages.items():
                if (value == original_combo.get()):
                    from_language_key = key

            # Get the To Language Key
            for key, value in languages.items():
                if (value == translated_combo.get()):
                    to_language_key = key

            # Turn Original Text into a TextBlob
            words = textblob.TextBlob(original_text.get(1.0, END))

            # Translate Text
            words = words.translate(from_lang=from_language_key , to=to_language_key)

            # Output translated text to screen
            translated_text.insert(1.0, words)

        except Exception as e:
            messagebox.showerror("Translator", e)




    def clear():
        # Clear the text boxes
        original_text.delete(1.0, END)
        translated_text.delete(1.0, END)

    #language_list = (1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,16,1,1,1,1,1,1,1,1,1,1,1,1,1)

    # Grab Language List From GoogleTrans
    languages = googletrans.LANGUAGES

    # Convert to list
    language_list = list(languages.values())




    # Text Boxes
    original_text = Text(root, bg="#36394F" , fg="#ffffff", height=10, width=40)
    original_text.grid(row=0, column=0, pady=20, padx=10)

    translate_button = Button(root, text="Translate!", font=("Helvetica", 24), cursor='hand2', command=translate_it)
    translate_button.grid(row=0, column=1, padx=10)

    translated_text = Text(root, bg="#36394F" , fg="#ffffff", height=10, width=40)
    translated_text.grid(row=0, column=2, pady=20, padx=10)

    # Combo boxes
    original_combo = ttk.Combobox(root, width=50, value=language_list)
    original_combo.current(21)
    original_combo.grid(row=1, column=0)
    original_combo.set('english')

    translated_combo = ttk.Combobox(root, width=50, value=language_list)
    translated_combo.current(26)
    translated_combo.grid(row=1, column=2)
    translated_combo.set("hindi")

    # Clear button
    clear_button = Button(root, text="Clear", cursor='hand2', command=clear)
    clear_button.grid(row=2, column=1)

    root.mainloop()

# ------------------------------------- ######## End Of Translator Function ###### ------------------------------------#


################################################ cascade ###########################################################

main_menu.add_cascade(label='File', menu=file)
main_menu.add_separator()
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_separator()
main_menu.add_cascade(label='View', menu=view)
main_menu.add_separator()
main_menu.add_cascade(label='CodeingCraft', command=code)
main_menu.add_separator()
main_menu.add_cascade(label='LangTranslate', command=translator)

################################################ End Of Cascade ###########################################################




############################################## toolbar  ###################################################


tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

######### font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)

########## size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(8, 81))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

######### bold button
bold_icon = tk.PhotoImage(file='icons2/bold button.png')
bold_btn = ttk.Button(tool_bar, cursor='hand2', image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

######## italic button
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar, cursor='hand2', image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

######## underline button
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar, cursor='hand2', image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

######## font color button
font_color_icon = tk.PhotoImage(file='icons2/color.png')
font_color_btn = ttk.Button(tool_bar, cursor='hand2', image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

######## align left
align_left_icon = tk.PhotoImage(file='icons2/left.png')
align_left_btn = ttk.Button(tool_bar, cursor='hand2', image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

####### align center
align_center_icon = tk.PhotoImage(file='icons2/canter.png')
align_center_btn = ttk.Button(tool_bar, cursor='hand2', image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

####### align right
align_right_icon = tk.PhotoImage(file='icons2/right.png')
align_right_btn = ttk.Button(tool_bar, cursor='hand2', image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

# -------------------------------------&&&&&&&& End toolbar  &&&&&&&&&&& ----------------------------------


############################################## text editor ###################################################


############## Text Area
text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


# font family and font size functionality
current_font_family = 'Arial'
current_font_size = 12

#############Change Font
def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


############# Change Font Size
def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)


######################################## buttons functionality

# bold button functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


bold_btn.configure(command=change_bold)


# italic functionlaity
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


italic_btn.configure(command=change_italic)


# underline functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


underline_btn.configure(command=change_underline)


## font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)


### align functionality

def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')


align_left_btn.configure(command=align_left)


## center
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')


align_center_btn.configure(command=align_center)


## right
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')


align_right_btn.configure(command=align_right)

text_editor.configure(font=('Arial', 12))
# -------------------------------------&&&&&&&& End text editor &&&&&&&&&&& ----------------------------------




##############################################  status bar ###################################################

status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False


def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)


text_editor.bind('<<Modified>>', changed)

# -------------------------------------&&&&&&&& End  status bar &&&&&&&&&&& ----------------------------------


############################################## main menu functinality ###################################################

## variable
url = ''


## new functionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)


## file commands
file_img = PhotoImage(file='icons2/new_file.png')
file.add_command(label='New File', compound=tk.LEFT, image=file_img, accelerator='Ctrl+N', command=new_file)
file.add_separator()

## open functionality

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File',
                                    filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

open_img = PhotoImage(file='icons2/open_file.png')
file.add_command(label='Open', compound=tk.LEFT, image=open_img, accelerator='Ctrl+O', command=open_file)
file.add_separator()

## save file

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                        filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return

save_img = PhotoImage(file='icons2/save_file.png')
file.add_command(label='Save', compound=tk.LEFT, image=save_img, accelerator='Ctrl+S', command=save_file)
file.add_separator()

## save as functionality
def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                    filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return

saveas_img = PhotoImage(file='icons2/saveAs_file.png')
file.add_command(label='Save As', compound=tk.LEFT, image=saveas_img, accelerator='Ctrl+Alt+E', command=save_as)
file.add_separator()

## exit functionality

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

exit_img = PhotoImage(file='icons2/exit.png')
file.add_command(label='Exit', compound=tk.LEFT, image=exit_img, accelerator='Ctrl+Q', command=exit_func)


############ find functionality

def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0, 0)

    ## frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    ## entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button
    find_button = ttk.Button(find_frame, text='Find', cursor='hand2', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', cursor='hand2', command=replace)

    ## label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()


##################### edit commands
edit.add_command(label='Copy', compound=tk.LEFT, accelerator='Ctrl+C',
                command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', compound=tk.LEFT, accelerator='Ctrl+V',
                command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', compound=tk.LEFT, accelerator='Ctrl+X',
                command=lambda: text_editor.event_generate("<Control x>"))
edit.add_separator()
edit.add_command(label='Code', compound=tk.LEFT, accelerator='Ctrl+W',
                command= code)
edit.add_command(label='Translator', compound=tk.LEFT, accelerator='Ctrl+T',
                command= translator)
edit.add_separator()
edit.add_command(label='Clear All', compound=tk.LEFT, accelerator='Ctrl+Alt+X',
                command=lambda: text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', compound=tk.LEFT, accelerator='Ctrl+F', command=find_func)

## view check button

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

################# Hide ToolBar
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True

################# Hide StatusBar
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


view.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=0, variable=show_toolbar,
                    compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar', onvalue=1, offvalue=False, variable=show_statusbar,
                    compound=tk.LEFT, command=hide_statusbar)


# -------------------------------------&&&&&&&& End main menu  functinality  &&&&&&&&&&& ----------------------------------

main_application.config(menu=main_menu)

#### bind shortcut keys
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-w>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)
main_application.bind("<Control-t>", translator)
main_application.bind("<Control-w>", code)

main_application.mainloop()