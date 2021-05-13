sc=`find . -type d -name "$1"`
nsc=`dirname $sc`
if [ -z "$1" ]
then
  for i in `find . -type f`
  do
     sn=`basename $i`
     sp=`dirname $i`
     a=`printf "%s" $sn | tr "[A-Z]" "[a-z]"`
     b=`printf "%s" $a | tr -c "[:alpha]" "[_*]"`
     mv $sp/$sn $sp/$b
     done
else
    for x in `find $nsc -type f`
    do
    xn=`basename $x`
    xp=`dirname $i`
    a=`printf "%s" $xn | tr "[A-Z]" "[a-z]"`
    b=`printf "%s" $a | tr -c "[:alpha:]" "[_*]"`
    mv $xp/$xn $xp/$b
    done
fi
