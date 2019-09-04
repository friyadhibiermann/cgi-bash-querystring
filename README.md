# cgi bash fungsi script
<pre>
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
</pre>
# cgi-bash-querystring screenshoot
<img height="500" width="300" src="ss.PNG"></img>
