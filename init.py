"""
init.py

initializes the json database
"""


import json
import scan


def get_whitelist(hosts):
    """
    gets which hosts the user whats to save to the white list.
    """
    i = 0
    for host in hosts:
        i += 1
        print(f"    {i} > {host.get('name')} - {host.get('ip')}")
    print("Please enter the numbers, seperated by a comma and a space, of the\n"
          "device you wish to add to the whitelist. Or enter the word [All] (recomended):")
    selection = input("> ")
    if selection.lower() == "all":
        whitelist = hosts
    else:
        whitelist = [hosts[int(i) - 1] for i in selection.split(", ")]
    return whitelist


def save_database(whitelist):
    """
    dumps the hosts to a json file.
    """
    print("Writing to file...")
    with open("database.json", "w") as database:
        for line in json.dumps(whitelist, indent=4):
            database.write(line)
    print("Done writning")

    
def main():
    """
    initializes the database
    """
    print("gathering hosts (this may take some time)...", end="\n\n")
    hosts = scan.get_hosts()
    whitelist = get_whitelist(hosts)
    save_database(whitelist)


if __name__ == "__main__":
    main()
