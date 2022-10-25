import tkinter

# Window
window = tkinter.Tk()
window.title("Miles to kms converter")
# Size
window.minsize(width=400, height=150)


# Get input
input_ = tkinter.Entry(width=10)
input_.place(x=150, y=20)

# Text1
label1 = tkinter.Label(text="miles ")
label1.place(x=300, y=20)

# button


def convert_to_kms():
    value = float(input_.get())*1.60934
    label2.config(text=f"is equal to        {'%.3f'%value}          kms")
# Event listener


button = tkinter.Button(text="Convert", command=convert_to_kms)
button.place(x=120, y=100)
# Text2
label2 = tkinter.Label(text="is equal to                  kms")
label2.place(x=75, y=70)


window.mainloop()
