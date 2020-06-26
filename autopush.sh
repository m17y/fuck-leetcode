status=`git diff`
echo $status
if [ ! -n $status ]; then  
  echo "IS NULL"  
else  
  echo "NOT NULL"  
fi    