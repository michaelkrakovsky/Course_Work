#!/bin/bash

read -p "First Value: " one
read -p "First Value: " two
read -p "First Value: " three

if [ $one -eq $two ]
then
    if [ $two -eq $three ]
    then
        echo "EQUILATERAL"
    else
        echo "ISOSCELES"
    fi
elif [ $one -eq $three ]
then
    echo "ISOSCELES"
elif [ $two -eq $three ]
then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi