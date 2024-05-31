Challenge #1
https://overthewire.org/wargames/bandit

level0 - "ssh bandit0@bandit.labs.overthewire.org -p 2220", password - "bandit0"
         ls -> readme -> cat readme -> NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

level1 - "ssh bandit1@bandit.labs.overthewire.org -p 2220", password - "NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL"
         ls -> - 
         The file name is "-", cat - does not return anything, so instead we write the path of the file -
         cat /home/bandit1/- or cat ./- -> rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

level2 - "ssh bandit2@bandit.labs.overthewire.org -p 2220", password - "rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi"
        
      
