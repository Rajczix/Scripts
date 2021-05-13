cnt=`echo $1 | wc -c`
li=`expr $cnt - 1`

if [ -z "$1" ]
then
  echo Brak rozszerzenia pliku
  exit 0
else
  continue
fi

if [ `find $HOME -name ".arch" -type d` ]
then
   continue
else
   echo Tworzenie brakujacego folderu
   mkdir $HOME/.arch
fi

arp=`find $HOME -name ".arch" -type d`
#echo $arp

for i in `find . \! -name "." -prune -name "*."$1"" -type f`
do  
   a=`echo $i | sed 's/..//'`
   b=`echo $a | sed 's/\.[^.]*$//`    
   cp $i $arp/"$b"_arch."$1"  
done

