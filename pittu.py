
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import ttkthemes




class Menubar:
    def __init__(self, parent):
        font_specs=("ubantu",12)

        menubar= tk.Menu(parent.master,font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown=tk.Menu(menubar,font=font_specs,tearoff=0)

        file_dropdown.add_command(label="New File",
                                  accelerator='Ctrl+N',
                                  command=parent.new_file)
        file_dropdown.add_command(label="Open File",
                                accelerator='Ctrl+O',
                                  command=parent.open_file)
        file_dropdown.add_command(label="Save",
                                  accelerator='Ctrl+S',
                                  command=parent.save_file)
        file_dropdown.add_command(label="Save As",
                                 accelerator='Ctrl+Shift+S',
                                  command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit",
                                  command=parent.master.destroy)

        about_dropdown=tk.Menu(menubar,font=font_specs,tearoff=0)
        about_dropdown.add_command(label="Release Notes",
                                  command=self.show_release_msg)
        about_dropdown.add_separator()   
        about_dropdown.add_command(label="About",
                                  command=self.show_about_msg)                      
        menubar.add_cascade(label="File",menu=file_dropdown)
        menubar.add_cascade(label="About",menu=about_dropdown)
    
    def show_about_msg(self):
        box_title="About Pittu"
        box_msg="Simple Text Editer develop in Python"
        messagebox.showinfo(box_title,box_msg)
    def show_release_msg(self):
        box_title="Release Notes"
        box_msg="Simple Text Editer develop in Python"
        messagebox.showinfo(box_title,box_msg)

class Statusbar:
    def __init__(self,parent):

        font_specs=("ubantu",12)

        self.status=tk.StringVar()
        self.status.set("Pittu -0.1 Swapn Corp")
        
        lable =tk.Label(parent.textarea, textvariable=self.status,fg="black",
                        bg="lightgray", anchor="sw",font=font_specs)
        lable.pack(side=tk.BOTTOM,fill=tk.BOTH)
    
    def update_status(self, *args):
        if isinstance(args[0],bool):
            self.status.set("Your file has been saved")
        else:
            self.status.set("Pittu -0.1 Swapn Corp")

        


class Text:
    def __init__(self, master):
        master.title("Untitle - Pittu")
        master.geometry("1200x700")
        font_specs=("ubantu",180)
        self.master = master
        self.filename= None
        self.textarea= tk.Text(master,font=font_specs)
        self.scroll= tk.Scrollbar(master, command=self.textarea.yview )
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)
        self.menubar= Menubar(self)
        self.statusbar = Statusbar(self)
        self.bind_shortcuts()

        
#This is function for change name of file window
    def set_window_title(self,name=None):
        if name:
            self.master.title(name+"-Pittu")
        else:
            self.master.title("Untitle - Pittu")
 #Fuction for create new file
    def new_file(self, *args):
        self.textarea.delete(1.0,tk.END)
        self.filename=None
        self.set_window_title(self.filename)
        self.textarea.delete()

        #Function for craete existing file
    def open_file(self,*args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All files","*.*"),
                        ("Text files","*.txt"),
                        ("Python Script","*.py"),
                        ("Stylesheet","*.css"),
                        ("Webpage","*.html"),
                        ]
        )
        if self.filename:
            self.textarea.delete(1.0,tk.END)
            with open(self.filename,"r") as F:
                self.textarea.insert(1.0, F.read())
            self.set_window_title(self.filename)

#Function for save file in current diectory
    def save_file(self,*args):
        if self.filename:
            try:
                textarea_content=self.textarea.get(1.0,tk.END)
                with open(self.filename,"w") as f:
                    f.write(textarea_content)
                self.statusbar.update_status(True)
            except Exception as e:
                print(e)
        else:
            self.save_as()

        #Function for save file on particular directory
    def save_as(self,*args):
        try:
            new_file=filedialog.asksaveasfilename(
                initialfile="Untitle.txt",
                defaultextension=".txt",
                filetypes=[("All files","*.*"),
                            ("Text files","*.txt"),
                            ("Python Script","*.py"),
                            ("Stylesheet","*.css"),
                            ("Webpage","*.html"),
                            ]
            )
            textarea_content=self.textarea.get(1.0,tk.END)
            with open(new_file,"w") as f:
                f.write(textarea_content)
            self.filename=new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status(True)
        except Exception as e:
            print(e)

    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>',self.new_file)
        self.textarea.bind('<Control-o>',self.open_file)
        self.textarea.bind('<Control-s>',self.save_file)
        self.textarea.bind('<Control-S>',self.save_as)
        self.textarea.bind('<Key>',self.statusbar.update_status)
        

if __name__ == "__main__":
    master=tk.Tk()
    master.style = ttkthemes.ThemedStyle()
    master.style.theme_use('black')
    pt =Text(master)
    master.mainloop()
