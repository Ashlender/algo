# https://leetcode.com/problems/valid-phone-numbers/description/

#!bin/bash
cat file.txt | grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$'