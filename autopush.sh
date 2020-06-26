the_day=`date -d $1 '+%Y%m%d'`
status=`git diff`
echo $status
echo ${#status}
if [ ${#status} -eq 0 ]; then  
    echo "最新没有 新的文件更改"  
else  
    git add -A
    git commit - am '${the_day}'
    git push
fi    