echo "this will accept N number of parameters"
echo "List of parameters $*"
echo "Total Number of parameters $#"
echo "******************************************************"
echo "Listing each parameter"
for param in $* do
  echo "$param"
done
echo "Job Don"