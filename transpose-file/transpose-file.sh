declare -a transposed
IFS=$'\n'
for line in `cat file.txt`
do
    i=0
    #echo ">>>> $line"
    IFS=$' '
    for word in $line
    do
	#echo "$i    ${transposed[$i]} $word"
	transposed[$i]="${transposed[$i]} $word"
	((i=i+1))
    done
done
for t in ${!transposed[*]}
do
    echo ${transposed[$t]}
done

