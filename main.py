from urllib.parse import urlparse

def ip_address_validator(ip):
     try:
         parsed_url = urlparse(ip) # Using urlparse to check if the IP address is correct
         print(f"{ip} is a valid IP address")
     except ValueError:
         print(f"ERROR: {ip} is not a valid IP address!")

ip_address = "http://154.16.192.204" # Example IP address
ip_address_validator(ip_address)

# We use a loop so that the script does not end immediately
while True:
     pass # This block will run forever
