file=/home/gurbanli/PycharmProjects/MsfvenomWeb/static/files/payloads.txt

for payload in $(cat $file);
do 
exec 1<>"${payload///}".txt
msfvenom -p $payload --list-options 2> /dev/null | grep Basic -A10 | sed -n '/^---/,/Description:/p' | sed '1d;$d' | sed \$d  | awk '{ print $1 }'
exec 1<&-
done
