from tkinter import *
#from api_data import *


import requests
import json

url = 'https://openexchangerates.org/api/latest.json?app_id=9d08e0c8cdd845639ca8e3433aa9fcd0'

response = requests.get(url)
print(response.text)
d = json.loads(response.text)
rates = d['rates']
currencies1 = rates.keys()
currencies2 = currencies1


def converter():
    rate_from = float(rates[from_curr.get()])
    print(amt.get())
    print(rate_from)
    rate_to = float(rates[to_curr.get()])
    print(rate_to)
    usd_amt = amt.get()/rate_from
    final_amt = usd_amt * rate_to
    g = float("{0:.2f}".format(final_amt))
    print(g)
    answer = Label(bottomRight, text=str(g), font='calibri 20 bold', fg='dark blue')
    answer.place(x=100, y=100)


root = Tk()
root.title("Currency Converter")

#Grid.columnconfigure(root, 0, weight=1)
#Grid.rowconfigure(root, 0, weight=1)

topFrame = Frame(root)
topFrame.pack(fill=X)
bottomLeft = Frame(root, bg='white', padx=20, pady=40)
bottomLeft.pack(fill=BOTH, expand=1, anchor=S+W, side=LEFT)
bottomRight = Frame(root, relief=RIDGE, bd=10)
bottomRight.pack(fill=BOTH, expand=1, anchor=S+E, side=RIGHT)

heading = Label(topFrame, text="Welcome to Currency Converter!", font='calibri 20 italic', fg='black', bg='light green')
heading.pack(fill=BOTH)

convert_from = Label(bottomLeft, text="Convert from:", font='calibri 15 bold', bg='white')
convert_to = Label(bottomLeft, text="Convert to:", font='calibri 15 bold', bg='white')
enter_amt = Label(bottomLeft, text="Enter Amount", font='calibri 15 bold', bg='white')
convert = Button(bottomLeft, text='Convert', bg='light green', command=converter)

from_curr = StringVar()
to_curr = StringVar()
from_curr.set('USD')
to_curr.set('USD')

convert_from_menu = OptionMenu(bottomLeft, from_curr, *currencies1)
convert_to_menu = OptionMenu(bottomLeft, to_curr, *currencies2)

amt = IntVar()
entry_box = Entry(bottomLeft, textvariable=amt)

convert_from.grid(row=3, column=0, sticky=E, padx=20)
convert_to.grid(row=4, column=0, sticky=E, padx=20)
enter_amt.grid(row=6, column=0, sticky=E, padx=20)
entry_box.grid(row=6, column=1, sticky=E, padx=20)
convert.grid(row=10, columnspan=2, pady=20)
convert_from_menu.grid(row=3, column=1)
convert_to_menu.grid(row=4, column=1)

converted_amt = Label(bottomRight, text='Converted amount is:', font='calibri 20 bold', bg='white', fg='light green')
converted_amt.pack(fill=X)


root.mainloop()
