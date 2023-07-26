from tkinter import *
from cli_main import importmodel,predictValue


def calculate():
    # GET VAL:UES
    sepal_length = sepal_lenght_entry.get()
    sepal_width  = sepal_width_entry.get()
    petal_length = petal_lenght_entry.get()
    petal_width  = petal_width_entry.get()
    def floatvalues(sepal_length, sepal_width, petal_length, petal_width):
        try:
            sepal_length = float(sepal_length)
            sepal_width = float(sepal_width)
            petal_length = float(petal_length)
            petal_width = float(petal_width)
            return sepal_length, sepal_width, petal_length, petal_width
        except ValueError:
            return None,None,None,None

    # START MODEL
    sepal_length, sepal_width, petal_length, petal_width =floatvalues(sepal_length, sepal_width, petal_length, petal_width)
    if sepal_length == None or sepal_width == None or petal_length == None or petal_width == None:
        result_entry.delete(0,END)
        result_entry.insert(0,"Please ENTER numeric value ")
    elif sepal_length != 0 or sepal_width != 0 or petal_length != 0 or petal_width != 0:
        Classifier = importmodel()
        result = predictValue(Classifier, sepal_length,sepal_width, petal_length, petal_width)
        result_entry.delete(0,END)
        result_entry.insert(0,result)

    else:
        result_entry.delete(0,END)
        result_entry.insert(0,"Please ENTER at least one value ")
        ...

root = Tk()

root.title('IRIS Dataset')
root.geometry('450x480')
root.resizable(False,False)

# ['sepal length (cm)',
# 'sepal width (cm)',
# 'petal length (cm)',
# 'petal width (cm)']

text_font = ("Arial", 16, "bold")
# Label
sepal_lenght_label = Label(root, text="Sepal lenght : ", font=text_font)
sepal_lenght_label.place(x=0,y=0)

# ENTRY
global sepal_lenght_entry
sepal_lenght_entry = Entry(root)
sepal_lenght_entry.place(x=10,y=30,height=30,width=420)

# Label
sepal_width_label = Label(root, text="Sepal width : ", font=text_font)
sepal_width_label.place(x=0,y=70)

# ENTRY
global sepal_width_entry
sepal_width_entry = Entry(root)
sepal_width_entry.place(x=10,y=100,height=30,width=420)

# Label
petal_lenght_label = Label(root, text="Petal lenght : ", font=text_font)
petal_lenght_label.place(x=0,y=140)

# ENTRY
global petal_lenght_entry
petal_lenght_entry = Entry(root)
petal_lenght_entry.place(x=10,y=170,height=30,width=420)

# Label
petal_width_label = Label(root, text="Petal width : ", font=text_font)
petal_width_label.place(x=0,y=210)

# ENTRY
global petal_width_entry
petal_width_entry = Entry(root)
petal_width_entry.place(x=10,y=250,height=30,width=420)

# BUTTON
button_font = ("Arial", 14)
button = Button(text='Calculate' , command=calculate,font=button_font)
button.place(x=150, y=290 ,height=30,width=100)

# ENTRY result
global result_entry
result_entry = Entry(root)
result_entry.place(x=10,y=330,height=30,width=420)

root.mainloop()
