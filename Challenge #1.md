Challenge #1
https://overthewire.org/wargames/bandit

level0 - "ssh bandit0@bandit.labs.overthewire.org -p 2220", password - "bandit0"
         ls -> readme , cat readme -> NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

level1 - "ssh bandit1@bandit.labs.overthewire.org -p 2220", password - "NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL"
         ls -> - 
         The file name is "-", cat - does not return anything, so instead we write the path of the file -
         cat /home/bandit1/- or cat ./- -> rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

level2 - "ssh bandit2@bandit.labs.overthewire.org -p 2220", password - "rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi"
         ls -> spaces in this filename, cat "spaces in this filename" -> aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

level3 - "ssh bandit3@bandit.labs.overthewire.org -p 2220", password - "aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG"
         ls -> inhere, cd inhere, ls
         ls returns nothing, it might be because inhere contains hidden files.
         ls -a reveals a file .hidden, cat .hidden -> 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

level4 - "ssh bandit4@bandit.labs.overthewire.org -p 2220", password - "2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe"
         ls -> inhere, cd inhere, ls
         10 files -file00 to -file09 exists in inhere
         Though all directories can be individually checked in this case, it is not feasible                                                   
         instead since all files have similar name, a wildcard (*) can be used.
         cat ./-file* or nano ./-file* returns bunch of text in which only -file07 returns human-readable text - lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

level5 - "ssh bandit5@bandit.labs.overthewire.org -p 2220", password - "lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR"
         ls -> inhere, cd inhere, ls
         ls returns 20 directories maybehere00-maybehere19
         It is given that the file size is 1033.
         file -size 1033c gives ./maybehere07/.file2
         cat ./maybehere07/.file2 -> P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
         
level6 - "ssh bandit6"@bandit.labs.overthewire.org -p 2220", password - "P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU"
         ls returns nothing, it is given that the file is owned by user bandit7 , owned by group bandit6 and 33 bytes in size.
         find  / -user bandit7 -group bandit6 -size 33c -> returns a file path - /var/lib/dpkg/info/bandit7.password
         cat /var/lib/dpkg/info/bandit7.password -> z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

level7 - "ssh bandit7"@bandit.labs.overthewire.org -p 2220", password - "z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S"
         It is given that the password for the next level is stored in the file data.txt next to the word millionth.
         grep can used to find the word millionth.
         grep millionth data.txt -> TESKZC0XvTetK0S9xNwm25STk5iWrBvP

level8 - "ssh bandit8"@bandit.labs.overthewire.org -p 2220", password - "TESKZC0XvTetK0S9xNwm25STk5iWrBvP"
         ls -> data.txt
         We have to find the only line of text that occurs only once, we can use sort function with uniq function and -u flag
         sort data.txt | uniq -u -> EN632PlfYiZbn3PhVK3XOGSlNInNE00t

level9 - "ssh bandit9"@bandit.labs.overthewire.org -p 2220", password - "EN632PlfYiZbn3PhVK3XOGSlNInNE00t"
         It is given that the password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by                 several ‘=’ characters.
         We can use strings or grep function to find the password.
         grep -a "===" data.txt -> gives a lot of unreadable text with G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s, grep should be used with -a flag otherwise 
         it will only return "grep: data.txt: binary file matches"
         strings data.txt | grep ====== -> also works the same way.

level10 - "ssh bandit10"@bandit.labs.overthewire.org -p 2220", password - "G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s"
         ls -> data.txt 
         data.txt contains base64 encoded data which can be decoded with the help of base64 function.
         base64 --decode data.txt -> The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
         
level11 - "ssh bandit11"@bandit.labs.overthewire.org -p 2220", password - "6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM"
level12 - "ssh bandit12"@bandit.labs.overthewire.org -p 2220", password - ""
level13 - "ssh bandit13"@bandit.labs.overthewire.org -p 2220", password - ""
level14 - "ssh bandit14"@bandit.labs.overthewire.org -p 2220", password - ""
level15 - "ssh bandit15"@bandit.labs.overthewire.org -p 2220", password - ""
level16 - "ssh bandit16"@bandit.labs.overthewire.org -p 2220", password - ""
level17 - "ssh bandit17"@bandit.labs.overthewire.org -p 2220", password - ""
level18 - "ssh bandit18"@bandit.labs.overthewire.org -p 2220", password - ""
level19 - "ssh bandit19"@bandit.labs.overthewire.org -p 2220", password - ""
level20 - "ssh bandit20"@bandit.labs.overthewire.org -p 2220", password - ""
level21 - "ssh bandit21"@bandit.labs.overthewire.org -p 2220", password - ""
level22 - "ssh bandit22"@bandit.labs.overthewire.org -p 2220", password - ""
level23 - "ssh bandit23"@bandit.labs.overthewire.org -p 2220", password - ""
level24 - "ssh bandit24"@bandit.labs.overthewire.org -p 2220", password - ""
level25 - "ssh bandit25"@bandit.labs.overthewire.org -p 2220", password - ""
level26 - "ssh bandit26"@bandit.labs.overthewire.org -p 2220", password - ""
level27 - "ssh bandit27"@bandit.labs.overthewire.org -p 2220", password - ""
level28 - "ssh bandit28"@bandit.labs.overthewire.org -p 2220", password - ""
level29 - "ssh bandit29"@bandit.labs.overthewire.org -p 2220", password - ""
level30 - "ssh bandit30"@bandit.labs.overthewire.org -p 2220", password - ""
level31 - "ssh bandit31"@bandit.labs.overthewire.org -p 2220", password - ""
level32 - "ssh bandit32"@bandit.labs.overthewire.org -p 2220", password - ""
level33 - "ssh bandit33"@bandit.labs.overthewire.org -p 2220", password - ""
