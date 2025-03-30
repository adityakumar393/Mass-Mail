Mass Mail
A simple GUI-based Python application to send bulk emails to recipients listed in a CSV file. The application uses Gmail's SMTP server and allows users to specify the email subject, body, and CSV file containing email addresses to send the email to. The status of the email sending process is displayed via a progress bar.

Features
Send bulk emails to multiple recipients.
GUI interface built with tkinter.
Progress bar to track email sending status.
CSV file input, where the email addresses are extracted automatically.
Handles SMTP connection securely using Gmail.

Installation
Clone this repository:
Open terminal
cd your folder name

How to Use
Run the script:
python index.py

GUI Instructions:

Subject: Enter the subject for the email.
Body: Enter the message body of the email.
CSV File: Select a CSV file that contains a column with email addresses. The program will automatically detect the email column.
Send Emails: Click the "Send Emails" button to begin the process. The progress bar will show the email sending status.
CSV File Format:

The CSV file should contain at least one column with email addresses. It can have other columns as well (e.g., name, phone number, etc.). The program will automatically detect the column containing emails.

Example CSV format:

Name, Email
Sample One, sampleone@example.com
Sample Two, sampletwo@example.com
Gmail SMTP Settings:

You will need to generate an app-specific password for your Gmail account (since direct use of your Gmail password isn't allowed).
Replace the placeholder password () in the script with your actual Gmail app password.
