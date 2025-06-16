import tkinter as tk
calculator=""
def add_to_calculator(symbol):
    global calculator
    calculator +=str(symbol)
    Text_result.delete(1.0,"end")
    Text_result.insert(1.0,calculator)

def evaluate_calculator():
    global calculator
    try:
        calculator=str(eval(calculator))
        Text_result.delete(1.0,"end")
        Text_result.insert(1.0,calculator)


    except:
        clear_field()
        Text_result.insert(1.0,"Error")

def clear_field():
    global calculator
    calculator=""
    Text_result.delete(1.0,"end")

w = tk.Tk()
w.geometry("300x275")
w.title("My calculator")

Text_result=tk.Text(w,height=2,width=16,font=("Ärial",18))
Text_result.grid(columnspan=5)
btn_1=tk.Button(w,text="1",command=lambda: add_to_calculator("1"),width=5,font=("Arial",12))
btn_1.grid(row=2,column=0,)
btn_2=tk.Button(w,text="2",command=lambda: add_to_calculator("2"),width=5,font=("Arial",12))
btn_2.grid(row=2,column=1)
btn_3=tk.Button(w,text="3",command=lambda: add_to_calculator("3"),width=5,font=("Arial",12))
btn_3.grid(row=2,column=2)
btn_4=tk.Button(w,text="4",command=lambda: add_to_calculator("4"),width=5,font=("Arial",12))
btn_4.grid(row=3,column=0)
btn_5=tk.Button(w,text="5",command=lambda: add_to_calculator("5"),width=5,font=("Arial",12))
btn_5.grid(row=3,column=1)
btn_6=tk.Button(w,text="6",command=lambda: add_to_calculator("6"),width=5,font=("Arial",12))
btn_6.grid(row=3,column=2)
btn_7=tk.Button(w,text="7",command=lambda: add_to_calculator("7"),width=5,font=("Arial",12))
btn_7.grid(row=4,column=0)
btn_8=tk.Button(w,text="8",command=lambda: add_to_calculator("8"),width=5,font=("Arial",12))
btn_8.grid(row=4,column=1)
btn_9=tk.Button(w,text="9",command=lambda: add_to_calculator("9"),width=5,font=("Arial",12))
btn_9.grid(row=4,column=2)
btn_0=tk.Button(w,text="0",command=lambda: add_to_calculator("0"),width=5,font=("Arial",12))
btn_0.grid(row=5,column=0)
btn_plus=tk.Button(w,text="+",command=lambda: add_to_calculator("+"),width=5,font=("Arial",12))
btn_plus.grid(row=2,column=3)
btn_minus=tk.Button(w,text="-",command=lambda: add_to_calculator("-"),width=5,font=("Arial",12))
btn_minus.grid(row=3,column=3)
btn_mul=tk.Button(w,text="*",command=lambda: add_to_calculator("*"),width=5,font=("Arial",12))
btn_mul.grid(row=4,column=3)
btn_div=tk.Button(w,text="/",command=lambda: add_to_calculator("/"),width=5,font=("Arial",12))
btn_div.grid(row=5,column=3)
btn_clr=tk.Button(w,text="clr",command=clear_field,width=5,font=("Arial",12))
btn_clr.grid(row=6,column=1,columnspan=2)
btn_equals=tk.Button(w,text="=",command=evaluate_calculator,width=5,font=("Arial",12))
btn_equals.grid(row=6,column=3,columnspan=2)



w.mainloop()
                    