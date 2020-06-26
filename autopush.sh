status=`git diff`
echo $status
if [ ! -n $para1 ]; then  
  echo "IS NULL"  
else  
  echo "NOT NULL"  
fi    