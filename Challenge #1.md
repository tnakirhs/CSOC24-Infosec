Challenge #1    
https://overthewire.org/wargames/bandit

**level0** - ***bandit0***     
<pre>ls ↵ readme
cat readme ↵ *password* </pre> 
      
**level1** - ***NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL***    
<pre>ls ↵ -      
The file name is "-"
cat - does not return anything, so instead we write the path of the file -    
cat /home/bandit1/- or cat ./- ↵ *password*</pre>     
           
**level2** - ***rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi***        
<pre>ls ↵ spaces in this filename
cat "spaces in this filename" ↵ *password*</pre>      
         
**level3** - ***aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG***     
<pre>ls ↵ inhere, cd inhere, ls     
ls returns nothing, it might be because inhere contains hidden files.     
ls -a reveals a file .hidden, cat .hidden ↵ *password*</pre> 
     
**level4** - ***2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe***       
<pre>ls ↵ inhere, cd inhere, ls  
10 files -file00 to -file09 exists in inhere    
Though all directories can be individually checked in this case, it is not feasible                                                       
instead since all files have similar name, a wildcard (*) can be used.    
cat ./-file* or nano ./-file* returns bunch of text in which only -file07 returns human-readable text - *password*</pre>    

**level5** - ***lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR***    
         ls ↵ inhere, cd inhere, ls    
         ls returns 20 directories maybehere00-maybehere19    
         It is given that the file size is 1033.    
         file -size 1033c gives ./maybehere07/.file2    
         cat ./maybehere07/.file2 ↵ *password*    
         
**level6** - ***P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU***    
         ls returns nothing, it is given that the file is owned by user bandit7 , owned by group bandit6 and 33 bytes in size.    
         find  / -user bandit7 -group bandit6 -size 33c ↵ returns a file path - /var/lib/dpkg/info/bandit7.password    
         cat /var/lib/dpkg/info/bandit7.password ↵ *password*    

**level7** - ***z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S***    
         It is given that the password for the next level is stored in the file data.txt next to the word millionth.    
         grep can used to find the word millionth.    
         grep millionth data.txt ↵ *password*    

**level8** - ***TESKZC0XvTetK0S9xNwm25STk5iWrBvP***    
         ls ↵ data.txt    
         We have to find the only line of text that occurs only once, we can use sort function with uniq function and -u flag    
         sort data.txt | uniq -u ↵ *password*    
    
**level9** - ***EN632PlfYiZbn3PhVK3XOGSlNInNE00t***    
         It is given that the password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by                 several ‘=’ characters.    
         We can use strings or grep function to find the password.    
         grep -a "===" data.txt ↵ gives a lot of unreadable text with *password*, grep should be used with -a flag otherwise   
         it will only return "grep: data.txt: binary file matches"    
         strings data.txt | grep ====== ↵ also works the same way.    

**level10** - ***G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s***    
         ls ↵ data.txt     
         data.txt contains base64 encoded data which can be decoded with the help of base64 function.    
         base64 --decode data.txt ↵ The password is *password*    
         
**level11** - ***6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM***  
         
**level12** - *** ***           
**level13** - *** ***           
**level14** - *** ***           
**level15** - *** ***           
**level16** - *** ***           
**level17** - *** ***           
**level18** - *** ***           
**level19** - *** ***           
**level20** - *** ***           
**level21** - *** ***           
**level22** - *** ***           
**level23** - *** ***           
**level24** - *** ***           
**level25** - *** ***           
**level26** - *** ***           
**level27** - *** ***           
**level28** - *** ***           
**level29** - *** ***           
**level30** - *** ***           
**level31** - *** ***           
**level32** - *** ***           
**level33** - *** ***           
