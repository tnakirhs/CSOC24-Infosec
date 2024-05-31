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
         Though all directories can be individually checked in this case, it is not feasible instead                                               
         since all files have similar name, a wildcard (*) can be used.
         cat ./-file* or nano ./-file*
         
        
      
