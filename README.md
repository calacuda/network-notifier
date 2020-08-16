# network-notifier:

notifies you when a new device connects to you're network using python3.

### description:

this is a script that runs on someting like a raspberry pi using screen.
every 20 min the script will find all the devices on the network and email
any email in "alert_emails.txt" if there are new devices.


### Installation:

1. install screen
2. setup a throwaway email with gmail.
3. set up gmail api credentials (https://developers.google.com/gmail/api/quickstart/python).
   click the blue, "enable the gmail api", button.
4. rename "credentials.json" to "client_secret.json"


~~~
$ git clone https://github.com/calacuda/network-notifier.git
$ mv /path/to/client_secret.json network-notifier/client_secret.json
$ cd network-notifier
~~~

edit the client_email.txt file to have one line with the throwaway email from earlier.
edit the alert_emails.txt to have one email per line. each of these emails will be emailed
when there is a new device on the network.

~~~
$ pip3 install -r requirments.txt 
$ python3 init.py

$ screen
$ python3 main.py
~~~
if you determinded and or adventurous, you can try to set up a system service.
