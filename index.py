import smtplib
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading

# Function to send an email
def send_bulk_email(subject, body, recipient):
    # sender_email = enetr your mailing account here inside ''
    # app_password = enter your mailing account password here  inside '' 

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the Gmail SMTP server and send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            message_content = message.as_string()
            server.sendmail(sender_email, recipient, message_content)
            print(f"Email successfully sent to {recipient}")
    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")

# Function to read CSV and process email dispatch
def process_emails(file_path, email_subject, email_body, progress_bar, progress_label):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Read header row

            # Look for the email column dynamically
            email_column_index = None
            for idx, header in enumerate(headers):
                print(f"Checking header: {header}")  # Debugging each header
                if 'email' in header.lower():
                    email_column_index = idx
                    print(f"Found email column: {header}")
                    break  # Stop once we find the email column

            # If no email column is found, show an error
            if email_column_index is None:
                messagebox.showerror("Error", "No email column found in the CSV file.")
                return

            total_emails = sum(1 for row in reader)  # Count emails
            file.seek(0)  # Reset file pointer
            next(reader)  # Skip header again

            for idx, row in enumerate(reader):
                recipient_email = row[email_column_index]  # Get email from dynamic column
                send_bulk_email(email_subject, email_body, recipient_email)

                # Update progress
                progress = (idx + 1) / total_emails * 100
                progress_bar['value'] = progress
                progress_label.config(text=f"Sending: {int(progress)}%")
                window.update_idletasks()

        messagebox.showinfo("Success", "All emails have been sent!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        progress_bar['value'] = 100
        progress_label.config(text="Sending: 100%")

# Function to select a CSV file
def select_csv_file():
    file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file:
        file_path_var.set(file)

# Function to trigger email sending
def start_email_sending():
    file_path = file_path_var.get()
    subject = subject_var.get()
    body = message_body.get("1.0", "end-1c")

    if not file_path or not subject or not body:
        messagebox.showwarning("Input Error", "Please ensure all fields are filled.")
    else:
        email_thread = threading.Thread(target=process_emails, args=(file_path, subject, body, progress_bar, progress_label))
        email_thread.start()

# Create the main window
window = tk.Tk()
window.title("Mass Mail")
window.geometry('600x450')
window.config(bg="#f4f4f9")

# Styling
font = ('Helvetica', 12)
header_font = ('Helvetica', 14, 'bold')
button_style = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Helvetica', 12, 'bold'), 'width': 15}
entry_style = {'font': ('Helvetica', 12), 'width': 50}
progress_style = {'bg': '#990303'}

# Subject Label and Entry
subject_label = tk.Label(window, text="Subject:", font=header_font, bg="#f4f4f9")
subject_label.pack(pady=10)
subject_var = tk.StringVar()
subject_entry = tk.Entry(window, textvariable=subject_var, **entry_style)
subject_entry.pack(pady=5)

# Message Body Label and Text Box
message_label = tk.Label(window, text="Body:", font=header_font, bg="#f4f4f9")
message_label.pack(pady=10)
message_body = tk.Text(window, height=8, width=50, font=('Helvetica', 12), bd=2, relief="groove")
message_body.pack(pady=5)

# CSV File Selection
file_path_var = tk.StringVar()
file_path_label = tk.Label(window, text="CSV File:", font=header_font, bg="#f4f4f9")
file_path_label.pack(pady=10)
file_path_entry = tk.Entry(window, textvariable=file_path_var, **entry_style)
file_path_entry.pack(pady=5)
browse_button = tk.Button(window, text="Browse", command=select_csv_file, **button_style)
browse_button.pack(pady=5)

# Progress Bar and Label
progress_bar = ttk.Progressbar(window, length=300, mode='determinate', maximum=100)
progress_bar.pack(pady=20)
progress_label = tk.Label(window, text="Progress: 0%", font=('Helvetica', 12), bg="#f4f4f9")
progress_label.pack(pady=5)

# Send Email Button
send_button = tk.Button(window, text="Send Emails", command=start_email_sending, **button_style)
send_button.pack(pady=20)

# Run the GUI loop
window.mainloop()
