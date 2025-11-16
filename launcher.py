from customtkinter import *
class ConnectWindow(CTk):
    def __init__(self):
        super().__init__()
        
        self.name = None
        self.host = None
        self.port = None
        
        self.title('launcher')
        self.geometry('300x400')
        
        CTkLabel(self, text='connect', font=('Courier', 28, 'bold')).pack(pady=15,padx=20,anchor='w')
        
        self.name_entry = CTkEntry(self, placeholder_text='name', height=50)
        self.name_entry.pack(padx=20, anchor='w', fill='x')
        
        self.host_entry = CTkEntry(self, placeholder_text='host name', height=50)
        self.host_entry.pack(padx=20,pady=15,anchor='w', fill='x')
        
        self.port_entry = CTkEntry(self, placeholder_text='port', height=50)
        self.port_entry.pack(padx=20, anchor='w', fill='x')
        
        CTkButton(self, text='join', command=self.open_game, height=50).pack(padx=20, pady=15, fill='x')
    def open_game(self):
        self.name = self.name_entry.get()
        self.host = self.host_entry.get()
        self.port = int(self.port_entry.get())
        self.destroy()
        