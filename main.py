from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    num= [str(i) for i in range(0,9)]
    word= [chr(i) for i in range(ord('a'),ord('z')+1)]
    wordc= [chr(i) for i in range(ord('A'),ord('Z')+1)]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    # password = [
    #     random.choice(num),
    #     random.choice(word),
    #     random.choice(symbols),
    #     random.choice(wordc)
    # ]*2
    password
    nNum=[random.choice(num) for item in range(2)]
    nword= [random.choice(word) for item in range(2)]
    nwordc= [random.choice(wordc) for item in range(2)]
    nsymbols = [random.choice(symbols) for item in range(2)]
    password = password + nNum + nword + nwordc + nsymbols
    
    random.shuffle(password)  # Shuffle the list in place
    password = ''.join(password)  # Join the list into a string
    
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok= messagebox.askokcancel(title= website, message=f"There are the details \nemail: {email}"
                                      f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            new_data = {
                "website": [website],
                "email": [email],
                "password": [password]
            }
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")

            # Add the new data to the DataFrame
            new_df = pd.DataFrame(new_data)
            
            try:
                existing_df = pd.read_csv("data.csv")
                updated_df = pd.concat([existing_df, new_df], ignore_index=True)
            except FileNotFoundError:
                updated_df = new_df

            updated_df.to_csv("data.csv", index=False)
            
            # Clearing the fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)


        



# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)  
window.minsize(width=200, height=200)

Canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
Canvas.create_image(100, 100, image=logo_img)
Canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="EW",columnspan=2, pady=5)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, sticky="EW", pady=5,columnspan=2)
email_entry.insert(0, "ZJpjV@example.com")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1,columnspan=2, sticky="EW", pady=5)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36 , command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")



window.mainloop()