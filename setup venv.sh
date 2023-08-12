re='^[0-9]+$'
echo "What is your python version? (pythonX.Y)"
read -p "Major version (X): " maversion
if ! [[ $maversion =~ $re ]] ; then
   echo "error: Not a number" >&2; exit 1
fi
read -p "Minor version (Y): " miversion
if ! [[ $miversion =~ $re ]] ; then
   echo "error: Not a number" >&2; exit 1
fi
fullversion=$maversion"."$miversion
python$maversion -m venv ./Pymin-venv/
mkdir ./Pymin-venv/Pymin/
cp ./Pymin.py ./Pymin-venv/Pymin/Pymin.py
chmod +x ./Pymin-venv/Pymin/Pymin.py
source ./Pymin-venv/bin/activate
pip install Mini-AMF tkhtmlview numpy Pillow as3lib
deactivate
