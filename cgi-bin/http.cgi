#!/data/data/com.termux/files/usr/bin/bash
## bentuk halaman HTML
echo "Content-type: text/html"
echo ''

## Parsing QueryString
QUERY=$QUERY_STRING
IFS="&"
set -- $QUERY
array=($@)
declare -A get_post
for i in "${array[@]}"
do
IFS="="
set -- $i
get_post[$1]=$2
done

## Condition
status=${get_post['test']}
if [ "$status" == "ok" ];then
 input=${get_post['input']}
 echo "$input" | sed "s/%20/ /g"
fi
