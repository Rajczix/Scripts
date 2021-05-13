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

arp=`find $HOME -name ".arch"`
echo $arp

for i in `find . \! -name "." -prune -name "*.$1" -type f`
do
   nbe=`basename $i .$1`
   np=`basename $i`
   sp=`dirname $i`
   cp -p $sp/$np $arp/"$nbe"_arch.c
   
done

