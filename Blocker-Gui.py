import pickle
import Blocker
from tkinter import *

class BlockerScreen:
    def __init__(self,master):
        self.master=master
        self.master.geometry('500x500')
        self.master.resizable(0,1)
        self.master.title('Website Blocker')

        self.heading=Label(self.master,text='Website Blocker',font=('Bodoni MT',23,'bold'))
        self.heading.pack()

        self.blocked_websites_listbox=Listbox(self.master,width=70)
        self.blocked_websites_listbox.pack(pady=20,ipadx=10)

        self.button_frame=LabelFrame(self.master,text="Functions",font=('Bodoni MT',15,'bold'),bd=5,relief=GROOVE)
        self.button_frame.pack(pady=10)

        self.add_website_button=Button(self.button_frame,text='Add Website',width=25)
        self.add_website_button.pack(side=LEFT,padx=10,pady=10)

        self.remove_website_button=Button(self.button_frame,text='Remove Website',width=25)
        self.remove_website_button.pack(side=LEFT,padx=10,pady=10)

        

        self.master.mainloop()



if __name__ == "__main__":
    root=Tk()
    app=BlockerScreen(root)