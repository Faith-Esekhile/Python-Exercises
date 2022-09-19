'''import tkinter

class MYGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.label1=tkinter.Label(self.main_window,text="hello world")
        self.label2=tkinter.Label(self.main_window,text="this is my gui")
        self.label1.pack(side="left")
        self.label2.pack(side="left")
        tkinter.mainloop()
my_gui=MYGUI()'''


'''import tkinter

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        self.label1=tkinter.Label(self.top_frame,text="winken")
        self.label2=tkinter.Label(self.top_frame,text="blinken")
        self.label3=tkinter.Label(self.top_frame,text="nod")

        self.label1.pack(side="top")
        self.label2.pack(side="top")
        self.label3.pack(side="top")

        self.label4=tkinter.Label(self.bottom_frame,text="winken")
        self.label5=tkinter.Label(self.bottom_frame,text="blinken")
        self.label6=tkinter.Label(self.bottom_frame,text="nod")

        self.label4.pack(side="left")
        self.label5.pack(side="left")
        self.label6.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

my_gui=MyGUI()'''

'''import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.my_button=tkinter.Button(self.main_window,text="click me!",command=self.do_something)
        self.my_button.pack()
        
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("response","thanks for clicking the button")

my_gui=MyGUI()'''

'''import tkinter
import tkinter.messagebox
class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.my_button=tkinter.Button(self.main_window,text="click me",command=self.do_something)
        self.quit_button =tkinter.Button(self.main_window,text="quit",command=self.main_window.destroy)
        self.my_button.pack()
        self.quit_button.pack()
        tkinter.mainloop()
    def do_something(self):
        tkinter.messagebox.showinfo("response","thanks for clicking the button")
my_gui=MyGUI()'''

'''import tkinter
import tkinter.messagebox
class kiloConverterGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)

        self.prompt_label=tkinter.Label(self.top_frame,text="Enter a distance in kilometer:")
        self.kilo_entry=tkinter.Entry(self.top_frame,width=10)

        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        self.calc_button=tkinter.Button(self.bottom_frame,text='convert',command=self.convert)
        self.quit_button=tkinter.Button(self.bottom_frame,text="quit",comman=self.main_window.destroy)
        
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        kilo=float(self.kilo_entry.get())
        miles=kilo*0.6214

        tkinter.messagebox.showinfo("results",str(kilo)+"kilometers is equal to"+str(miles)+"miles")
kilo_conv=kiloConverterGUI()'''

'''import tkinter
class TestAvg:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.test1_frame=tkinter.Frame(self.main_window)
        self.test2_frame=tkinter.Frame(self.main_window)
        self.test3_frame=tkinter.Frame(self.main_window)
        self.avg_frame=tkinter.Frame(self.main_window)
        self.button_frame=tkinter.Frame(self.main_window)

        self.test1_label=tkinter.Label(self.test1_frame,text="enter the score for test1:")
        self.test1_entry=tkinter.Entry(self.test1_frame,width=10)

        self.test1_label.pack(side="left")
        self.test1_entry.pack(side="left")

        self.test2_label=tkinter.Label(self.test2_frame,text="enter the score for test 2:")
        self.test2_entry=tkinter.Entry(self.test2_frame,width=10)

        self.test2_label.pack(side="left")
        self.test2_entry.pack(side="left")

        self.test3_label=tkinter.Label(self.test3_frame,text="enter the score for test 3:")
        self.test3_entry=tkinter.Entry(self.test3_frame,width=10)

        self.test3_label.pack(side="left")
        self.test3_entry.pack(side="left")

        self.result_label=tkinter.Label(self.avg_frame,text="average")
        self.avg=tkinter.StringVar()
        self.avg_label=tkinter.Label(self.avg_frame,textvariable=self.avg)

        self.result_label.pack(side="left")
        self.avg_label.pack(side="left")

        self.calc_button=tkinter.Button(self.button_frame,text="average",command=self.calc_avg)
        self.quit_button=tkinter.Button(self.button_frame,text="quit",command=self.main_window.destroy)

        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def calc_avg(self):
        self.test1=float(self.test1_entry.get())
        self.test2=float(self.test2_entry.get())
        self.test3=float(self.test3_entry.get())

        self.average=(self.test1+self.test2+self.test3) / 3.0
        self.avg.set(self.average)

test_avg=TestAvg() '''

'''import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        self.radio_var=tkinter.IntVar()
        self.radio_var.set(1)
        self.rb1=tkinter.Radiobutton(self.top_frame,text="option1",variable=self.radio_var,value=1)
        self.rb2=tkinter.Radiobutton(self.top_frame,text="option 2",variable=self.radio_var,value=2)
        self.rb3=tkinter.Radiobutton(self.top_frame,text="option 3",variable=self.radio_var,value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_button=tkinter.Button(self.bottom_frame,text="ok",command=self.show_choice)
        self.quit_button=tkinter.Button(self.bottom_frame,text="quit",command=self.main_window.destroy)

        self.ok_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo("selection","you selected option" + str(self.radio_var.get()))

my_gui=MyGUI()'''


import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)

        self.cb_var1=tkinter.IntVar()
        self.cb_var2=tkinter.IntVar()
        self.cb_var3=tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1=tkinter.Checkbutton(self.top_frame,text="option 1",variable=self.cb_var1)
        self.cb2=tkinter.Checkbutton(self.top_frame,text="option 2",variable=self.cb_var2)
        self.cb3=tkinter.Checkbutton(self.top_frame,text="option 3",variable=self.cb_var3)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.ok_button=tkinter.Button(self.bottom_frame,text='ok',command=self.show_choice)
        self.quit_button=tkinter.Button(self.bottom_frame,text="Quit",command=self.main_window.destroy)

        self.ok_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        self.message="you selected:\n" 

        if self.cb_var1.get()==1:
            self.message=self.message+"1\n"
        if self.cb_var2.get()==1:
            self.message=self.message+"2\n" 
        if self.cb_var3.get()==1:
            self.message=self.message +"3\n" 
        
        tkinter.messagebox.showinfo("selection",self.message)


my_gui=MyGUI()
