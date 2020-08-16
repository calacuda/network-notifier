# network-notifier:

notifies you when a new device connects to you're network using python3.

### description:

This is a script that runs on someting like a raspberry pi using screen.
Every 20 min the script will find all the devices on the network and email
any adn all emails in the "alert_emails.txt" file, if there are new devices.


### Installation:

NOTES:

If you'll notice in the code section bellow there is the command "python3 notify.py".
That is to set up the emailing capabilities, and to test the emailing engine. You'll need
set up ssh port forwarding on your local machine THEN and only then should you go to the
url that comand output tells you too. If you ssh into you raspberry pi the way I have it
set up in the instructions, you shouldn't have any problems. Good luck and happy hunting!

1. install screen
2. setup a throwaway email with gmail.
3. set up gmail api credentials (https://developers.google.com/gmail/api/quickstart/python).
   click the blue, "enable the gmail api", button.
4. rename "credentials.json" to "client_secret.json"


~~~
$ ssh -L 8080:localhost8080 your-raspberry-pi-user:raspberry-pi-IP-addr
$ git clone https://github.com/calacuda/network-notifier.git
$ mv /path/to/client_secret.json network-notifier/client_secret.json
$ cd network-notifier
~~~

Edit the client_email.txt file to have one line with the throwaway email from earlier.
Edit the alert_emails.txt to have one email per line. Each of these emails will be emailed
when there is a new device on the network.

~~~
$ pip3 install -r requirments.txt 
$ python3 init.py
$ python3 notify.py

$ screen
$ python3 main.py
~~~

If you determinded and or adventurous, you can even try to set up a system service. There's
an idea
