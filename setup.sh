#!/bin/sh

declare personal_bin="/Users/$USER/bin"
declare cfg=".bash_profile"

eval pip3 install -r requirements.txt

[ -n $ZSH_VERSION ] && 
cfg=".zprofile"

[[ -d $personal_bin ]] || mkdir $personal_bin &&
echo export PATH="$personal_bin:\$PATH" >> /Users/$USER/$cfg

chmod +x ./mtg_query.py &&
cp ./mtg_query.py $personal_bin/mtgq