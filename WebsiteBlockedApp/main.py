from tkinter import *
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Website Blocking App")
Label(root, text ='Website Blocking App' , font ='Helvetica 15 bold').pack()
host_path ='C:\\Windows\\System32\\drivers\\etc\\hosts'
ip_address = 'Enter the local host ip adress'
Label(root, text ='Website Url Link:' , font ='Helvetica 10 bold').place(x=5 ,y=70)
Websites = Text(root,font = 'arial 10',height='2', width = '40')
Websites.place(x= 140,y = 60)

def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for web in Website:
            if web in file_content:
                Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + web + '\n')
                Label(root, text = "Blocked", font = 'Helvetica 10 bold').place(x=230,y =200)

block = Button(root, text = 'Block',font = 'Helvetica 10 bold',pady = 5,command = Blocker ,width = 6, bg = 'cornsilk1', activebackground = 'coral')
block.place(x = 230, y = 150)
root.mainloop()
