read k
read a b
VAR="NG"
 
for ((i = a; i <= $b; i++)); do
  if [ $(( i % k )) = 0 ]; then
    VAR="OK"
  fi
done
echo $VAR
