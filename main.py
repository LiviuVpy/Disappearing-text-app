from tkinter import *
from tkinter import messagebox


total_timer = None
short_timer = None
typed_text = ""

game_on = False
timer_count_sec = None
current_typed_text = None


def count_timer_60(count):
    global total_timer, game_on, timer_count_sec
    count_sec = count 
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    timer_text_60.config(text=count_sec)
    total_timer = root.after(1000, count_timer_60, count-1)
    if int(count_sec) < 1:
        radio_state.set(0)
        root.after_cancel(total_timer)
        root.after_cancel(short_timer)
        messagebox.showinfo(title="Done!", message=f"You wrote: {len(current_typed_text.split())} words!")
        root.destroy()
        
def count_timer(count):
    global short_timer 
    count_sec = count 
    timer_text.config(text=count_sec, fg='green')
    short_timer = root.after(1000, count_timer, count-1)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        timer_text.config(text=count_sec)
    if int(count_sec) < 3:
        timer_text.config(fg='red')
    if int(count_sec) == 0:
        main_text.delete(0.0, END)
        root.after_cancel(short_timer)
        
def speed_write(event):
    global typed_text, timer_count_sec, game_on, short_timer, current_typed_text
    if timer_count_sec == None:
        messagebox.showwarning(title="Oops!", message="Please choose difficulty level!")
        main_text.configure(state='disabled')
        game_on = False
    if timer_count_sec:
        game_on = True
        if game_on:
            main_text.configure(state='normal')
            current_typed_text = main_text.get(0.0, 'end-1c')
            typed_text += event.char
            if len(typed_text) == 1:
                count_timer_60(60)
                count_timer(timer_count_sec)
            if current_typed_text != typed_text:
                root.after_cancel(short_timer)
                count_timer(timer_count_sec)

def set_timer():
    global timer_count_sec
    if radio_state.get() == 1:
        timer_count_sec = 5
        timer_text.config(text="05")
    elif radio_state.get() == 2:
        timer_count_sec = 7
        timer_text.config(text="07")
    elif radio_state.get() == 3:
        timer_count_sec = 10
        timer_text.config(text="10")


root = Tk()
root.title("Typing speed test")
root.config(padx=30, pady=20)
# root.minsize(width=600, height=400)

write_label = Label(root, text="Write below in a five seconds window.\nDon't stop writing for 1 minute!", font=("Arial", 11, "italic"), justify="left")
write_label.grid(row=0, column=0, sticky=W, padx=10, pady=10)

write_label = Label(root, text="Time:", font=("Arial", 20, "normal"))
write_label.grid(row=0, column=1, sticky=E, padx=10, pady=10)

timer_text_60 = Label(root, text="60", font=("Arial", 20, "normal"))
timer_text_60.grid(row=0, column=2, sticky=W, padx=10, pady=10)

write_label = Label(root, text="timer:", font=("Arial", 14, "normal"))
write_label.grid(row=0, column=3, sticky=E, padx=10, pady=10)

timer_text = Label(root, text="10", font=("Arial", 14, "normal"))
timer_text.grid(row=0, column=5, sticky=W, padx=10, pady=10)

description_text = Label(root, text="*hard: 5 sec\n medium: 7 sec\n easy:5 sec", font=("Arial", 9, "normal"), justify="left")
description_text.grid(row=4, column=0, sticky=W, padx=10, pady=10)

main_text = Text(root, height=10, width=80, font=("Arial", 13, "normal"))
main_text.grid(row=1, column=0, columnspan=6, rowspan=3, sticky=EW, padx=10, pady=10)
main_text.focus()
main_text.bind("<Key>", speed_write)

# buttons:
radio_state = IntVar()

hard_button = Radiobutton(text='Hard', value='1', variable=radio_state, command=set_timer)
hard_button.grid(column=6, row=1, sticky=W)

madium_button = Radiobutton(text='Medium', value='2', variable=radio_state, command=set_timer)
madium_button.grid(column=6, row=2, sticky=W)

easy_button = Radiobutton(text='Easy', value='3', variable=radio_state, command=set_timer)
easy_button.grid(column=6, row=3, sticky=W)


root.mainloop()
