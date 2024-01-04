#Ask user if they want to use the default python executable (/bin/python)
read -p "Do you want to use the default python executable (/bin/python)?[y/n] " defpyexec
if [[ $defpyexec -eq "y" ]] ; then
   fullversion=""
else
   # Get version from user and determine the executable name
   re='^[0-9]+$'
   echo "What is your python version? (pythonX.Y)"
   read -p "Major version (X): " maversion
   if ! [[ $maversion =~ $re ]] ; then
      echo "Error: Input not a number" >&2; exit 1
   fi
   if [[ $maversion -lt 3 ]] ; then
      echo "Error: Major version too low. Expected >=3 got $maversion" >&2; exit 1
   fi
   read -p "Do you have multiple versions installed?[y/n] " mulversion
   if [[ $mulversion == "n" ]] ; then
      fullversion=$maversion
   elif [[ $mulversion == "y" ]] ; then
      read -p "Minor version (Y): " miversion
      if ! [[ $miversion =~ $re ]] ; then
         echo "Error: Input not a number" >&2; exit 1
      fi
      if [[ $maversion -lt 10 ]] ; then
         echo "Error: Minor version too low. Expected >=10 got $maversion" >&2; exit 1
      fi
      fullversion=$maversion"."$miversion
   fi
fi
# Version Checking
set +m
shopt -s lastpipe
python3 -c 'import platform; temp=platform.python_version().split(".");print(temp[0]);print(temp[1])' |
  while IFS= read -r line; do lines[i]="$line"; ((i++)); done
imav=${lines[0]}
imiv=${lines[1]}
if [[ $imav -ne 3 ]] ; then
   echo "Python executable's major version does not match. Expected 3 got $imav" >&2; exit 1
fi
if [[ $imiv -lt 10 ]] ; then
   echo "Python executable's minor version is too low. Expected >=10 got $imiv" >&2; exit 1
fi
set -m
shopt -u lastpipe
# Virtual environment setup
read -p "Put venv folder in the current directory?[y/n] " incd
dir="."
if [[ $incd -ne "y" ]] ; then
   read -p "What directory would you like it in? " dir
fi
python$fullversion -m venv $dir/Pymin-venv/
mkdir $dir/Pymin-venv/Pymin/
cp ./Pymin.py $dir/Pymin-venv/Pymin/Pymin.py
chmod +x $dir/Pymin-venv/Pymin/Pymin.py
source $dir/Pymin-venv/bin/activate
pip install --upgrade pip
pip install Mini-AMF tkhtmlview numpy Pillow as3lib
pip install -U Mini-AMF tkhtmlview numpy Pillow as3lib
deactivate
