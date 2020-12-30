from sys import argv

script_name, hours, wage_rate, bounty = argv

print((int(hours) * int(wage_rate)) + int(bounty))
