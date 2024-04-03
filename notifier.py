"""
Unofficial University of Oregon Course Availability Notifier
By: Michal Klopotowski
Last Updated April 2024

SUMMER TERMS NOT SUPPORTED (Fall, Winter, Spring ONLY)
For personal/private use ONLY
"""

import requests
from bs4 import BeautifulSoup
import time
import smtplib
import re
import datetime

"""
INSTRUCTIONS
Step 1: Edit email configurations
    sending_address is the email you will be sending the notification from
        IMPORTANT: THIS MUST BE A GMAIL ACCOUNT
    sending_password is the password to the gmail account of sending_address
        NOTE: Password is used to login to this account and send the email. 
              Secondary/Burner account recommended
              Use personal account information at your own risk
    recieving_address is the email address of the account you want to notify
        UO student email recommended but any email account will work
NOTE: Account information is NOT checked so please ensure this information before continuing. 

Step 2: Run this file and input course information when prompted.

NOTE: In order for this program to continuously check for available seats, you must have internet access, 
      keep your computer running, and prevent it from going to sleep. 
      
      Once the program is running, the only way to stop it is to force close the console. 
      Keybindings to force the program to stop:
          Windows/Linux: Ctrl+C    Mac: Command+C
"""

# Email configurations
sending_address = "sending_address@gmail.com"  # Replace with your email address
sending_password = "sending_password"  # Replace with your email password
receiving_address = "recieving_address@uoregon.edu"  # Replace with recipient's email address


def check_url(url: str) -> bool:
    """
    Use regex to check if user is inputting url corresponding to a valid upcoming term.
    Only returns true if checking within the date range of the desired term.
    """
    date = str(datetime.date.today())
    cur_year = date[:4]
    cur_month = int(date[5:7])
    # If within dates for fall registration
    if cur_month in range(5, 11) and re.search(f"(https://)|(duckweb).uoregon.edu/duckweb/hwskdhnt.p_viewdetl\?term={cur_year}01&crn=\d{'{5}'}", url):
        return True
    # If within dates for winter registration
    elif (cur_month in range(10, 13) or cur_month == 1) and re.search(f"(https://)|(duckweb).uoregon.edu/duckweb/hwskdhnt.p_viewdetl\?term={cur_year}02&crn=\d{'{5}'}", url):
        return True
    # If within dates for spring registration
    elif cur_month in range(2, 5) and re.search(f"(https://)|(duckweb).uoregon.edu/duckweb/hwskdhnt.p_viewdetl\?term={cur_year}03&crn=\d{'{5}'}", url):
        return True
    # Not currently supporting Summer classes...
    return False


def main():
    # User inputs URL
    url = input("Paste in the FULL classes.uoregon.edu url to the course you wish to be notified for.\n"
                "\t(Ex: https://duckweb.uoregon.edu/duckweb/hwskdhnt.p_viewdetl?term=202303&crn=32766 )\n").strip().lower()
    # Check if url is valid
    while not check_url(url):
        retry = input("Url is invalid or you're unable to currently register for this course.\n"
                      "Would you like to try another url? (y/n)\n").strip().lower()
        if retry == 'n':
            return
        elif retry != 'y':
            print(f"Error: Expecting y or n but got {retry}")
        else:
            url = input("Paste in the FULL classes.uoregon.edu url to the course you wish to be notified for.\n"
                        "\t(Ex: https://duckweb.uoregon.edu/duckweb/hwskdhnt.p_viewdetl?term=202303&crn=32766 )\n").strip().lower()

    # Obtain CRN from the URL
    crn = url[-5:]

    # Make a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Get the course title
    try:
        title = soup.find('td', attrs={'colspan': '6', 'class': 'dddead', 'width': '323'}).find('b').text.strip().replace("\xa0\xa0", "")
    except Exception as e:
        print("Error: Invalid URL or could not find course title. Please try again.")
        main()
        return

    # Set up the email message
    subject = f"{title} availability update"
    body = "The course availability has changed. Check the website at " + url

    # Create the email message
    message = f"Subject: {subject}\n\n{body}"

    # Function to scrape the webpage
    def check_availability():
        try:
            # Find the Avail header and extract the availability
            avail_header = soup.find("td", string=crn)
            avail_value = int(avail_header.find_next_sibling("td").text.strip())

            # Check if the availability has increased from 0
            if avail_value > 0:
                print("Availability increased to", avail_value)
            else:
                print(f"({time.asctime()}) No change in availability.")

            return avail_value

        except Exception as e:
            print("Error checking availability:", e)

    # Function to send the email
    def send_email():
        try:
            # Connect to the SMTP server
            server = smtplib.SMTP("smtp.gmail.com", port=587)
            server.starttls()
            server.login(sending_address, sending_password)

            # Send the email
            server.sendmail(sending_address, receiving_address, message)

            # Close the connection
            server.quit()
            print("Email sent successfully.")
        except Exception as e:
            print("Error sending email:", e)

    # Main program loop
    while True:
        availability = check_availability()

        # Check if the availability has increased from 0
        if availability > 0:
            send_email()
            return

        # Wait for 5 minutes before checking again
        time.sleep(300)


if __name__ == '__main__':
    main()
