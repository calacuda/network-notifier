"""
main.py

for running a periodic scan to see if any new devices have connected to the
network.

By: Calacuda | MIT Licence
"""


import scan
import notify
import time


def periodic_scan(wait_time):
    """
    does a periodic scan of the network if any new device connects it will
    send out an email to all the emails in 'alert_emails.txt'.

    wait_time = the number of minuets between scans.
    """
    try:
        open("database.json", "r")
    except FileNotFoundError:
        print("please run the init.py script to create the database. then come back")
        exit()
    while True:
        new_devices = scan.get_hosts()
        if new_devices:
            # names = "\n > ".join(new_devices)
            notify.send_message(new_devices)
        time.wait(wait_time * 60)


if __name__ == "__main__":
    periodic_scan(20)
