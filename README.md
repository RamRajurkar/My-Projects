### Account Creation with Email Verification

This Python program enables users to create accounts with email verification through OTP. It provides a simple GUI interface for users to enter their desired username and Gmail ID. Upon entering the details and clicking "Send OTP," an OTP email is sent to the provided Gmail ID. After entering the correct OTP and clicking "Sign Up," the user account is created.

#### Prerequisites:
- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- pymongo library (`pip install pymongo`)
- Access to Gmail account for SMTP email sending
- MongoDB server running locally or remotely

#### Instructions:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/your_username/otp-email-verification.git
   ```
2. Navigate to the project directory.
   ```bash
   cd otp-email-verification
   ```
3. Install dependencies.
   ```bash
   pip install pymongo
   ```
4. Configure the Gmail account credentials and MongoDB connection details in the `main.py` file.
   ```python
   sender_email = 'your_email@gmail.com'
   sender_password = 'your_password'
   ```

   ```python
   # Create a connection to MongoDB
   client = pymongo.MongoClient("mongodb://localhost:27017/")
   db = client['Emails_Database']
   collection = db['Emails_Data_Collection']
   ```
5. Run the program.
   ```bash
   python main.py
   ```
6. Enter the username and Gmail ID, then click "Send OTP."
7. Check your Gmail inbox for the OTP email and enter the received OTP in the provided field.
8. Click "Sign Up" to create your account.

#### Features:
- Simple GUI for user interaction.
- OTP email verification for account creation.
- MongoDB integration for storing user details and OTP information.
- Error handling for invalid inputs and SMTP server errors.

### Additional Notes:

- Make sure to replace your valid email address and password from which you want to send email and create a passkey of your password from account manager and enable two step authentication for security.
- Make sure to enable "Less Secure Apps" in your Gmail account settings to allow SMTP access.
- Ensure that MongoDB is installed and running, or update the connection details to use a remote MongoDB server.
- For security reasons, avoid hardcoding sensitive information directly into the script. Instead, consider using environment variables or configuration files.