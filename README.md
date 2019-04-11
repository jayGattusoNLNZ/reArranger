# reArranger
This is a tool that creates a replica of a given file structure in a new location. All the files are empty/zero copies. It is a useful and fast way of making a very portable copy of a file system to help arrangement planning and other analysis

Reqs: Python 3.x

Usage is very simple for either mode:

(1) From your ide - just change the input_folder and output_folder vars to reflect your desired locations

(2) From your command line - example: c:> python reArranger.py "input\folder\path" "output\folder\path"

Has a couple of protections to prevent you from overwriting the original, but no warranties... test first. 


I wrote this little tool because I was working on a very large collection that needed lots of delicate operations on the file structure. The collection was 100k + files, and >4Tb. It was took time consuming / costly to keep making copies that I could play around with to get the arrangement right. 

Using this approach, which is a close approximation of the broadcast world online/offline processing approach  I am able to work on the file system as is the files are real - doing moves, deletes, renames etc without damaging the master and without the time penalty of copying repeatedly.  
