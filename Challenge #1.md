**Challenge #1**     
https://overthewire.org/wargames/bandit

**level 0** - ***bandit0***     
<pre><b>ls ↵ readme</b>
<b>cat readme</b> ↵ *password* </pre> 
      
**level 1** - ***NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL***    
<pre><b>ls</b> ↵ - <i>The file name is "-"</i>
<b>cat -</b> <i>does not return anything, so instead we write the path of the file -</i>    
<b>cat /home/bandit1/-</b> or <b>cat ./-</b> ↵ *password* </pre>     
           
**level 2** - ***rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi***        
<pre><b>ls</b> ↵ <i>The name of the file is <b>spaces in this filename</b>, (" ") should be added to the file name. </i>
<b>cat "spaces in this filename"</b> ↵ *password*</pre>      
         
**level 3** - ***aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG***     
<pre><b>ls</b> ↵ inhere, <b>cd inhere</b>, <b>ls</b>     
<b>ls</b> <i>returns nothing, it might be because inhere contains hidden files.</i>    
<b>ls -a</b> <i>reveals a file .hidden</i>
<b>cat .hidden</b> ↵ *password*</pre> 
     
**level 4** - ***2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe***       
<pre><b>ls</b> ↵ inhere, <b>cd inhere</b>, <b>ls</b>    
<i>10 files -file00 to -file09 exists in inhere, though all directories can be individually checked in this case, 
it is not feasible instead since all files have similar name, a wildcard (*) can be used.</i>    
<b>cat ./-file*</b> or <b>nano ./-file*</b> <i>returns bunch of text in which only -file07 returns human-readable text</i> *password*</pre>    

**level 5** - ***lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR***    
<pre><b>ls</b> ↵ inhere, <b>cd inhere</b>, <b>ls</b>    
<i>ls returns 20 directories maybehere00-maybehere19. It is given that the file size is 1033.</i>    
<b>file -size 1033c</b> <i>gives ./maybehere07/.file2</i>    
<b>cat ./maybehere07/.file2</b> ↵ *password*</pre>   
         
**level 6** - ***P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU***    
<pre><b>ls</b> <i>returns nothing, it is given that the file is owned by user bandit7, owned by group bandit6 and 33 bytes in size.</i>    
<b>find  / -user bandit7 -group bandit6 -size 33c</b> ↵ <i>returns a file path</i> /var/lib/dpkg/info/bandit7.password    
<b>cat /var/lib/dpkg/info/bandit7.password</b> ↵ *password*</pre>   

**level 7** - ***z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S***    
<pre><i>It is given that the password for the next level is stored in the file data.txt next to the word millionth.
grep can used to find the word millionth.</i>   
<b>grep millionth data.txt</b> ↵ *password*</pre>

**level 8** - ***TESKZC0XvTetK0S9xNwm25STk5iWrBvP***    
<pre><b>ls</b> ↵ data.txt    
<i>We have to find the only line of text that occurs only once, we can use sort function with uniq function and -u flag.</i>   
<b>sort data.txt | uniq -u</b> ↵ *password*</b></pre>   
    
**level 9** - ***EN632PlfYiZbn3PhVK3XOGSlNInNE00t***    
<pre><i>It is given that the password for the next level is stored in the file data.txt in one of the few 
human-readable strings, preceded by several ‘=’ characters.    
We can use strings or grep function to find the password.</i>   
<b>grep -a "===" data.txt</b> ↵ <i>we can try a few = sign as no specific number is given, it gives a lot of 
unreadable text along with *password*, grep should be used with -a flag otherwise   
it will only return <b>grep: data.txt: binary file matches</b>.</i>    
<b>strings data.txt | grep ====</b> <i>also works the same way.</i></pre>   

**level 10** - ***G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s***    
<pre><b>ls</b> ↵ data.txt     
<i>data.txt contains base64 encoded data which can be decoded with the help of base64 function.</i>    
<b>base64 --decode data.txt</b> ↵ The password is *password*</pre>    
         
**level 11** - ***6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM***
<pre><b>ls</b> ↵ data.txt, <b>cat data.txt</b> ↵ Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
<i>The text appears to be scrambled, we can use translate function, it can be seen that T has been replaced by G and so on.</i>
<b>cat data.txt | tr a-zA-Z n-za-mN-ZA-M</b> ↵ The password is *password*</pre>

**level 12** - ***JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv***           
**level 13** - *** ***           
**level 14** - *** ***           
**level 15** - *** ***           
**level 16** - *** ***           
**level 17** - *** ***           
**level 18** - *** ***           
**level 19** - *** ***           
**level 20** - *** ***           
**level 21** - *** ***           
**level 22** - *** ***           
**level 23** - *** ***           
**level 24** - *** ***           
**level 25** - *** ***           
**level 26** - *** ***           
**level 27** - *** ***           
**level 28** - *** ***           
**level 29** - *** ***           
**level 30** - *** ***           
**level 31** - *** ***           
**level 32** - *** ***           
**level 33** - *** *** 
