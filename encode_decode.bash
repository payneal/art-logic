#!/bin/bash
while true
do
    echo "Enter E for encode, D for decode, or X for Exit enter X"
    read -p ": " answer

    case $answer in
    [eE]* ) echo "enter text to encode: "
            read -p ":" encode
            echo "you are encoding: $encode"
            va=$(python3 encoding.py $answer $encode)
            echo "$va"  
            echo " ";;
    [dD]* ) echo "numbers to decode: "
            read -p ":" decode
            echo "you are decoding: $decode"
            va=$(python3 encoding.py $answer $decode)
            echo "$va"  
            echo " ";;
    [xX]* ) exit;;
    *) echo "options are: E D and X for exit"
    esac
done

