from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = []

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    originial_data = pandas.read_csv("data/french_words.csv")
    to_learn = originial_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient= "records")


#################################### next card ######################################
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(card_background, image = img)
    flip_timer = window.after(3000, flip_card)

def right_word():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_card()

####################### Flip Card ######################################################
def flip_card():
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(card_word, text=current_card["English"], fill = "white")
    canvas.itemconfig(card_background,image= card_back_img )

######################################## UI SetUp ######################################
window = Tk()
window.config(padx= 50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer = window.after(3000, flip_card)

canvas = Canvas(height = 526, width= 800)
img = PhotoImage(file = "images/card_front.png")
card_back_img = PhotoImage(file= "images/card_back.png")
card_background = canvas.create_image(400, 263, image = img )
card_title = canvas.create_text(400, 150, text= "", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row= 0,  column=0, columnspan= 2)

wrong_btn_img = PhotoImage(file= "images/wrong.png")
wrong_btn = Button(image= wrong_btn_img, bg= BACKGROUND_COLOR, highlightthickness= 0, command= next_card)
wrong_btn.grid(row=1, column=0)

right_btn_img = PhotoImage(file= "images/right.png")
right_btn = Button(image= right_btn_img, bg= BACKGROUND_COLOR, highlightthickness= 0, command = right_word)
right_btn.grid(row=1, column=1)

next_card()



window.mainloop()

