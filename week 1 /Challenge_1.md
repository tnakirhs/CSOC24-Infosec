**Challenge #1**
<pre>will complete 3,6,7 and 9 soon.</pre>

***1. Information***
<pre>We are given a file name 'cat.jpg', <b>file cat.jpg</b> confirms that the image is indeed jpg.
It is given to look at the details of the file. We can either use some website like aperisolve or use exiftool. 
<b>exiftool cat.jpg</b> provides variety of details about the file, 2 specific details ('Current IPTC Digest' and 'License') 
looks like encoded strings. Trying base64 since it looks familiar, or use ChatGPT or cyberchef reveals that the string 
corresponding to license is indeed base64. <b>echo [string] | base64 --decode</b> gives <i><b>flag</b></i></pre>

***2. Matryoshka doll***
<pre>The name of the challenge sometimes gives a hint regarding the approach. It is given that 'Matryoshka dolls are 
a set of wooden dolls of decreasing size placed one inside another'. We are given a file name 'dolls.jpg', using 
<b>file dolls.jpg</b> reveals that dolls.jpg is actually a png file. It can be implied from the name of the challenge 
that something is hidden in this file, maybe another file. <b>exiftool dolls.jpg</b> gives no suspicious details, 
now we need to check if the file contains any hidden files.
We can use aperisolve or <b>binwalk dolls.jpg</b>,confirming that the given file do contain some hidden files.
<b>binwalk -e dolls.jpg</b> extracts the hidden files.</prse> binwalk the image in base_images directory, repeat the steps 
again until you get a file name <b><i>flag.txt.</i></b></pre>

***3. tunn3l v1s10n***
<pre></pre>

***4. MacroHard WeakEdge***
<pre>A file name 'Forensics is fun.pptm' is given. <b>file 'Forensics is fun.pptm'</b>reveals that the file is a
Microsoft PowerPoint 2007+. After searching for a while i found that files can also be hidden inside a pptm file. 
We can use <b>unzip 'Forensics is fun.pptm'</b>, it containd a lot of xml and rels file. It also contains a 
file name hidden in slideMasters directory which contains the <i><b>flag</b></i>.</pre>

***5. Enhance!***
<pre>A file name 'drawing.flag.svg' is given, <b>file drawing.flag.svg</b> confirms that it is a svg, since nothing else is given
we can start by seeing the metadata of the image. Nothing looks significant in the metadata, also the file does not 
contain any hidden files. We can try <b>strings drawing.flag.svg</b> which can be used to access elements of the svg file. 
We can see that the 'text' element contains the <b><i>flag</i></b>.</pre>

***6. advanced-potion-making***
<pre></pre>

***7. File types***
<pre></pre>

***8. hideme***
<pre>A file name 'flag.png' is given. The name of the challenge is hideme, which means that some files could be hidden 
in the given file. We can use use <b>binwalk -e flag.png</b> to check, which reveals a folder 'secret' containing another 
file name 'flag.png', opening the file reveals the <i><b>flag</b></i>.</pre>

***9. MSB***
<pre></pre>

***10. extensions***
<pre>A file name 'flag.txt' is given. <b>cat flag.txt</b> gives non readable data which means that file might actually be 
of different type, <b>file flag.txt</b> reveals that the file is a png. Changing the extension to png reveals the <i><b>flag</b></i>.</pre>
