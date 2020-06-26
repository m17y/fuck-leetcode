#! /bin/sh 
source /etc/profile

the_day=$(date "+%Y-%m-%d %H:%M:%S")
status=`git status`
diff=`git diff`
echo ${the_day}
echo ${#status} #获取字符串长度
# 判断是否包含
if [[ $status =~ '干净的工作区' ]];then 
    echo "最新没有 新的文件更改"  
else
    echo "有文件有修改，开始提交文件"
    git add -A
    git commit -am ". ${the_day}"
    git push
    echo "提交文件结束"
fi    