# https://www.hackerrank.com/challenges/ip-address-validation

import re

ip4 = r"^(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})$"
ip6 = r"^([0-9a-f]{1,4}):([0-9a-f]{1,4}):([0-9a-f]{1,4}):([0-9a-f]{1,4}):([0-9a-f]{1,4}):([0-9a-f]{1,4}):([0-9a-f]{1,4}):([0-9a-f]{1,4})$"

n = int(input())

for i in range(n):
    ip4_flag = True
    ip6_flag = False
    string = input()
    if re.match(ip4, string):
        m = re.match(ip4, string)
        for j in range(1, 5):
            if not(0 <= int(m.group(j)) <= 255):
                ip4_flag = False
    else:
        ip4_flag = False
    if re.match(ip6, string):
        ip6_flag = True
    if ip4_flag:
        print("IPv4")
    elif ip6_flag:
        print("IPv6")
    else:
        print("Neither")
