#!/bin/bash
#Problem Change Word Containing Bad to Good and remove new lines.

echo "-----------------------------------------Original Text-------------------------------------"
cat 3littlepigs_story.txt
echo
echo "-------------------------------------------end----------------------------------------------"
echo
echo
echo "--------------------Exercise GREP and SED: find and change word bad to good-----------------"
grep bad 3littlepigs_story.txt | sed -e 's/bad/good/g'
echo "-------------------------------------------end----------------------------------------------"
echo 
echo "-----------------Exercise AWK: change word bad to good and Remove nextline------------------"
awk '{gsub(/bad/,"good"); print}' 3littlepigs_story.txt | tr '\n' ' ' < 3littlepigs_story.txt
echo
echo "-------------------------------------------end----------------------------------------------"
