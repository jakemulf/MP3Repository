#Problem to solve

This script takes a list of mp3 files and combines them into one file.  Despite the simplicity of this program, a lot of previous problems were solved in terms of efficiency of combining mp3 files.

#Inspiration

This code is part of an ongoing project that I am working on which attempts to take several mp3 files and combines them into one file with transitions between the songs at a logical point in terms of pitch and timbre.

#mp3combine.py

A simple script that combines a list of mp3 files into one.

Usage: python mp3combine.py list_of_mp3_files outputfile

Dependencies: echonest.remix.audio

###Process

mp3combine.py begins by initializing an empty list of audio quantum.

For each of the mp3 files, the segments are extracted as audio quantum using echonest.remix.audio and added to the list.

Once all the songs have been added to the list, the list is used to write to a single audio file.

###Importance

This is probably the simplest and easiest part of my project.  Despite this simplicity, a few key features for the overall project were learned in writing this code.

A much faster way of writing to an mp3 file with music that was not changed was discovered.  Previously written code in this project accomplished this task by shifting the audio quantum by a ratio of 1.0, resulting in no change.  Although there was no change in the audio quantum, this process was very time consuming.  The original call (seg.render()) could simply be added to the list of audio quantum.

Previously written programs for this project were done with a set number of arguments.  This became an issue with this part of the project.  Figuring out how to use an arbitrary amount of command line arguments instead of a set number is key for the remaining portion of this project, and this was very easy to discover on a simple program instead of something more compelx.
