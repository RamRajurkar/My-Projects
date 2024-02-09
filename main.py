import smtplib
import random
import tkinter as tk
from tkinter import messagebox
import pymongo
import datetime


if __name__ == "__main__":
    # 1. create a connection to MongoDB, with the host as 'localhost' and port
    # Create a connection to the database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['Emails_Database']
    collection = db['Emails_Data_Collection']

OTP = random.randint(100000, 999999)

def send_otp_email(sender_email, sender_password, recipient_email):
    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  
    # Email content
    subject = 'Mail Sender'
    body = f'Your OTP is: {OTP}'

    # Create email message
    message = f'Subject: {subject}\n\n{body}'

    try:
    # Login to the SMTP server
        global server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, recipient_email, message)

        print('OTP sent successfully!')
    except Exception as e:
        print(f'Error sending OTP: {str(e)}')
    finally:
    # Disconnect from the SMTP server
        server.quit()

sender_email = 'your-gmail@gmail.com' #Enter your valid email address
sender_password = 'your-gmail-password' #Enter your email password

# Check otp is valid or not
def check_otp():
   global otp 
   otp = entry_otp.get()
   try:
      if OTP == int(otp):
        messagebox.showinfo("Success!","Account Created Successfully !")
      else:
        messagebox.showerror("Invalid OTP","Please Enter Correct OTP.")
   except Exception as e:
        print(f'Error sending OTP: {str(e)}')

def validate_int(new_value, entry_widget):
    try:
        if new_value:
            int(new_value)
        return True
    except ValueError:
        return False
   
def create_account():
    global username
    username = entry_username.get()

    if not username or not gmail_id:
        messagebox.showerror("Error", "Please enter all required information")
        return
    if(check_otp()):
        messagebox.showinfo("Success", f"Account created for {username} with Gmail ID: {gmail_id}")

def on_enter_key_press(event):
    button_signup.invoke()

# Create the main window
root = tk.Tk()
root.title("Account Sign Up")

def send_otp():
    global gmail_id
    gmail_id = entry_gmail_id.get()
    send_otp_email(sender_email, sender_password, gmail_id)

# Configure window size and background color
root.geometry("400x300")
root.configure(bg="#2c3e50")  # Set background color to a shade of gray-blue

# Create and place styled widgets
label_username = tk.Label(root, text="Username:", bg="#2c3e50", fg="white", font=("Helvetica", 12))
label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry_username = tk.Entry(root, font=("Helvetica", 12))
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_gmail_id = tk.Label(root, text="Gmail ID:", bg="#2c3e50", fg="white", font=("Helvetica", 12))
label_gmail_id.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

entry_gmail_id = tk.Entry(root, font=("Helvetica", 12))
entry_gmail_id.grid(row=1, column=1, padx=10, pady=10)

button_send_otp = tk.Button(root, text="Send OTP", command=send_otp, bg="#3498db", fg="white", font=("Helvetica", 14, "bold"))
button_send_otp.grid(row=2, column=0, columnspan=2, pady=15)

label_otp = tk.Label(root, text="Enter OTP:", bg="#2c3e50", fg="white", font=("Helvetica", 12))
label_otp.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

# Entry for OTP (Accepts only integers)
entry_otp = tk.Entry(root, font=("Helvetica", 12))
entry_otp.grid(row=3, column=1, padx=10, pady=10)
entry_otp['validate'] = 'key'
entry_otp['validatecommand'] = (entry_otp.register(validate_int), '%P', '%W')

button_signup = tk.Button(root, text="Sign Up", command=create_account, bg="#3498db", fg="white", font=("Helvetica", 14, "bold"))
button_signup.grid(row=4, column=0, columnspan=2, pady=15)

root.bind('<Return>', on_enter_key_press)

# Start the main event loop
root.mainloop()


current_datetime = datetime.datetime.now()

curr_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

email_dict = {"username" : username , "email_id" : gmail_id , "otp" : OTP, "date-time" : curr_datetime}
collection.insert_one(email_dict)
