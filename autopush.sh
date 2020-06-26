the_day=$(date "+%Y-%m-%d %H:%M:%S")
status=`git status`
diff = `git diff`
echo ${the_day}
#if [ ${#diff} -eq 0 ]; then  
if [[ $status =~ '尚未' ]];then
    echo "最新没有 新的文件更改"  
else

    echo "有文件有修改，开始提交文件"
    git add -A
    git commit -am ". ${the_day}"
    git push
    echo "提交文件结束"
fi    