# Write a function that takes an IP address and returns the domain name using PTR DNS records.

# Example
# get_domain("8.8.8.8") ➞ "dns.google"

# get_domain("8.8.4.4") ➞ "dns.google"
# Notes
# You may want to import socket.
# Don't cheat and just print the domain name, you need to make a real DNS request.
# Return as a string.

import socket

def get_domain(ip_address):
    host  = socket.gethostbyaddr(ip_address)
    return host[0]

if __name__ == "__main__":
    print(get_domain("8.8.4.4"))