commands = ["cmd -mac", "cmd -win", "cmd -b"]
commands_b = ["ping <website>", "whois <ip>"]

commands_mac = ["arp -a", "ifconfig en0"]
commands_win = ["sudo arp-scan -l", "ipconfig"]

for cmd in commands:
    print(cmd)

command = input()

if command == "cmd -mac":
    for mcmd in commands_mac:
        print(mcmd)

elif command == "cmd -win":
    for wcmd in commands_win:
        print(wcmd)

elif command == "cmd -b":
    for cmd in commands_b:
        print(cmd)
