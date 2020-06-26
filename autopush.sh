status=`git diff`
echo $status
echo ${#status}
 if [ ${#status} -eq 0 ]; then  
  echo "IS NULL"  
else  
  echo "NOT NULL"  
fi    