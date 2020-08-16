"""
whitelist.py

used to add a device to the database.
"""


import json
import scan
import init


def main():
    with open("database.json", "r") as database:
        hosts = json.loads(database.read())
    print("Scanning or new devices...")
    # hosts = scan.get_hosts(hosts)
    hosts += init.get_whitelist(scan.get_hosts(hosts))
    with open("database.json", "w") as database:
        for line in json.dumps(hosts, indent=4):
            database.write(line)
    print("Database updated!")


if __name__ == "__main__":
    main()
