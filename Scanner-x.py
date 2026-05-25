import requests
import time
import pyfiglet
logo = pyfiglet.figlet_format("Scanner")
print(logo)
user = input("INTER THE WEB NAME : ")
time.sleep(1)
url = user
fake_mask = {"User-Agent": "Mozilla/5.0"}
try:
	box = requests.get(url, headers=fake_mask)
	print("Services is :", box.status_code)
	no = input("Do you want to see the site index (yes,no) : ")
	if no == "yes":
		print(box.text[:100])
	else:
		print("ok")
except:
	print("\nError: Invalid URLor Not Internet Connection!")	
time.sleep(4)

target_url = input("INTER WEB FOR SCAN : ")
fake_mask = {"User-Agent": "Mozilla/5.0"}
try:
	rad = requests.get(target_url, 	headers=fake_mask)
	server_info = rad.headers
	print("\n--- Starting Scan For Witing 🔍 ---")
	time.sleep(2.3)
	print ("Services is : ", server_info.get("Server"))
	print ("Data Response : ", server_info.get("Date"))
except:
	print("\nError: Invalid URL or Not Internet Connection!")		

