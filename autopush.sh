#! /bin/sh
## linux 下使用crontab 设置每5分钟提交一次
## */5 * * * * cd /Users/xk/.leetcode && bash autopush.sh >> /Users/xk/log/leetcode-autopush.log
source /etc/profile
the_day=$(date "+%Y-%m-%d %H:%M:%S")
status=`git status`
diff=`git diff`
echo ${the_day}
#获取字符串长度
echo ${#status}
# 判断是否包含
# yes
if [[ $status =~ '干净的工作区' ]];then 
    echo "最新没有 新的文件更改"  
else
    echo "有文件有修改，开始提交文件"
    git add -A
    git commit -am ". ${the_day}"
    git push -u origin master
    echo "提交文件结束"
fi