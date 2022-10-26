#!/bin/bash

declare -a SubArray=()
declare -a DirArray=()
declare -a IdkArray=()
count=0


#Formats the url
fixingSave(){
	result="${1}"
	modified=${result:2}
}

#Distributes different domains according to inscope rules
while read line;
do
	if echo $line | grep ^* >> /dev/null;
		then fixingSave "$line"; SubArray[${#SubArray[@]}]+=$modified
	elif echo $line | grep '*' >> /dev/null; 
		then IdkArray[${#IdkArray[@]}]+=$line
	else 
		DirArray[${#DirArray[@]}]=$line
	fi
done < $1

echo "========================================="
echo "========================================="
echo "======== Subdomain Enumeration =========="
echo "========================================="
echo "========================================="



# Subdomain Enumeration for *.domains
# Amass performs passive enumeration
# Subfinder performs passvie enumeration via online sources
# SubDomainzer searches .js files for subdomains
for value in ${SubArray[@]}
do
	amass enum -active -d $value >> output.lst
	subfinder -d $value -silent >> output.lst
	/opt/SubDomainizer/SubDomainizer.py -u nflxext.com | grep '.com' >> output.lst
	read -p 'Enter Y if you would like to perform bruteforce enumeration: ' continue_q
	if [ "$continue_q" = 'y' ] || [ "$continue_q" = 'Y' ]
	then echo "Starting Bruteforce Enumeration..."; amass enum -brute -max-depth 3 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -d $value >> output.lst
	fi
	sort -u output.lst > domains.txt
	rm output.lst
done



# Directory Enumeration for <domains>


# for value in ${DirArray[@]}
# do 
# 	echo $value
# done
