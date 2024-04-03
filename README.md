---

# Course Availability Notifier

## Overview

The **Course Availability Notifier** is a Python program designed for personal use by students. It monitors course availability at the University of Oregon and sends email notifications when a desired course becomes available. By automating this process, you no longer need to manually check the course website for seat availability.

### Features

- Monitors course availability for specified classes.
- Sends an email notification when a seat becomes available.
- Intended for courses without an official waitlist.
- Compatible with any class with a crn such as lectures, labs, discussions, etc.

## Coming Soon...
- Support for Summer term notifications.
- Monitor several courses at the same time.

## Prerequisites

Before using the program, ensure you have the following:

1. **Python**: Make sure you have Python installed on your system.
2. **Gmail Account**: You'll need a Gmail account to send notifications.
3. **Course URL**: Locate the course you want to monitor on [classes.uoregon.edu](https://classes.uoregon.edu/). Obtain the full URL for that course.
    - Example: (https://duckweb.uoregon.edu/duckweb/hwskdhnt.p_viewdetl?term=202303&crn=33411) 

## Instructions

1. **Edit Email Configurations**:
    - Open the Python file (`course_availability_notifier.py`).
    - Locate the following variables starting at line 17:
        - `sending_address`: Your Gmail address used for sending notifications.
            - **IMPORTANT**: Must be a Gmail account.
        - `sending_password`: Password for the Gmail account sending notifications.
            - **NOTE**: This password is used to log in and send emails. Consider using a secondary or burner account.
        - `receiving_address`: Email address where you want to receive notifications.
            - UO student email is recommended, but any valid email address will work.
    - **CAUTION**: Account information is not checked, so ensure its accuracy before proceeding.

2. **Run the Program**:
    - Method 1 (Terminal/Command Prompt)
      - Open a terminal or command prompt.
      - Navigate to the directory containing `course_availability_notifier.py`.
      - Run the program using the command: `python course_availability_notifier.py`.
      - When prompted, enter the full URL of the course you want to monitor.
    - Method 2 (IDE capable of running Python files)
      - Launch your Preferred IDE (e.g., Visual Studio Code, PyCharm, IDLE, etc).
      - Open the directory containing `course_availability_notifier.py`.
      - Configure your IDE to ensure it recognizes Python and has the necessary interpreter set up.
      - Run the Program
        - Different IDE have different methods but generally, you should be able to right-click `course_availability_notifier.py` and choose an option such as "Run" or "Run Python File".
      - When prompted, enter the full URL of the course you want to monitor.

4. **Keep the Program Running**:
    - For continuous monitoring, keep your computer running and prevent it from going to sleep.
    - To stop the program, force close the console:
        - Windows/Linux: Press `Ctrl+C`.
        - Mac: Press `Command+C`.

## Customizing the Code

### 1. Threshold for Seat Availability
You can customize the threshold for seat availability by modifying the following line in your course_availability_notifier.py file:

**line 124**

    if availability > 0:

Change the 0 to any desired number to receive notifications only when the available seats exceed that threshold.
For example, if you want a notification only when 3 seats become available, the code would be `if availability > 3:`

### 2. Frequency of Checks
The program by default checks for seat availability every 300 seconds (5 minutes). You can adjust this interval by changing the value in the following line:

**line 129**

    time.sleep(300)

Change the 300 to the desired monitoring frequency (in seconds).
- To check more frequently, decrease the number (e.g., `time.sleep(60)` for 1-minute intervals).
- To check less frequently, increase the number (e.g., `time.sleep(600)` for 10-minute intervals).

## Disclaimer

Use this program responsibly and at your own risk. Ensure that your Gmail account information is secure. 

This program is unofficial and is not affiliated with the University of Oregon in any way.

---
