from tkinter import *
import string
import random

def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_characters = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    if choice.get() == 1:
        passwordField.delete(0, 'end')  # Clear previous content
        passwordField.insert(0, ''.join(random.sample(small_alphabets, password_length)))

    elif choice.get() == 2:
        passwordField.delete(0, 'end')  # Clear previous content
        passwordField.insert(0, ''.join(random.sample(small_alphabets + capital_alphabets, password_length)))

    elif choice.get() == 3:
        passwordField.delete(0, 'end')  # Clear previous content
        passwordField.insert(0, ''.join(random.sample(all_characters, password_length)))

root = Tk()
root.config(bg='gray50')
choice = IntVar()
Font = ('arial', 18)
passwordLabel = Label(root, text='Password Generator', font=('arial', 20, 'bold'), bg='gray30', fg='white')
passwordLabel.grid(pady=20)

weakRadioButton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakRadioButton.grid(pady=5)

mediumRadioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumRadioButton.grid(pady=5)

strongRadioButton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strongRadioButton.grid(pady=5)

lengthLabel = Label(root, text='Password Length', font=Font, bg='gray30', fg='white')
lengthLabel.grid(pady=5)

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.grid(pady=5)

generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid()

root.mainloop()
