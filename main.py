from tkinter import *


timer_sixty = None
timer_five = None
typed_text = ""
five_sec_window = True
game_on = True

def count_timer_60(count):
    global timer_sixty, game_on
    count_sec = count 
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    timer_text_60.config(text=count_sec)
    timer_sixty = root.after(1000, count_timer_60, count-1)
    if int(count_sec) < 1:
        root.after_cancel(timer_sixty)
        main_text.configure(state='disabled')
        root.after_cancel(timer_five)
        game_on = False
        
def count_timer_5(count):
    global timer_five 
    count_sec = count 
    timer_text_5.config(text=count_sec, fg='green')
    timer_five = root.after(1000, count_timer_5, count-1)
    if count_sec < 3:
        timer_text_5.config(fg='red')
    if count_sec == 0:
        main_text.delete(0.0, END)
        root.after_cancel(timer_five)
        
def speed_write(event):
    global typed_text
    if game_on:
        current_typed_text = main_text.get(0.0, 'end-1c')
        typed_text += event.char
        if len(typed_text) == 1:
            count_timer_60(60)
            count_timer_5(5)
        if current_typed_text != typed_text:
                root.after_cancel(timer_five)
                count_timer_5(5)
    else:
        root.after_cancel(timer_five)


root = Tk()
root.title("Typing speed test")
root.config(padx=30, pady=30)
root.minsize(width=600, height=400)

write_label = Label(root, text="Write below in a five seconds window.\nDon't stop writing for 1 minute!", font=("Arial", 11, "italic"), justify="left")
write_label.grid(row=0, column=0, sticky=W, padx=10, pady=10)

main_text = Text(root, height=10, width=60, font=("Arial", 13, "normal"))
main_text.grid(row=1, column=0, columnspan=3, sticky=EW, padx=10, pady=10)
main_text.focus()
main_text.bind("<Key>", speed_write)

timer_text_60 = Label(root, text="60", font=("Arial", 20, "normal"))
timer_text_60.grid(row=0, column=1, sticky=W, padx=10, pady=10)

timer_text_5 = Label(root, text="5", font=("Arial", 14, "normal"))
timer_text_5.grid(row=0, column=2, sticky=W, padx=10, pady=10)

root.mainloop()