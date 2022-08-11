from tkinter import *


window = Tk()


window.title('Simple interest')
window.geometry('700x400')
window.configure(bg='lightcyan')

principal_label = Label(window,text='please enter the principal:',fg='black',bg='white',bd='1',font=('Calibri',9))
principal_label.place(x=20,y=20)
principal_value = Entry(window,text='',bd=2,width=25)
principal_value.place(x=250,y=20)

rate_label = Label(window,text='please enter the rate:',fg='black',bg='white',bd='1',font=('Calibri',9))
rate_label.place(x=20,y=40)
rate_value = Entry(window,text='',bd=2,width=25)
rate_value.place(x=258,y=40)

time_label = Label(window,text='please enter the time:',fg='black',bg='white',bd='1',font=('Calibri',9))
time_label.place(x=20,y=40)
time_value = Entry(window,text='',bd=2,width=25)
time_value.place(x=268,y=60)

answer_frame = LabelFrame(window,text='answer on you calculation:',bg='white')
answer_frame.place(x=200,y=300)
#answer_label = Label()

def answer():
    p=int(principal_value.get())
    r=int(rate_value.get())
    t=int(time_value.get())
    i=p*r*t/100

calculate_button = Button(window,text='claculate',command=answer)
calculate_button.place(x=330,y=180)


    

window.mainloop()