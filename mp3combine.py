"""
mp3combine.py

Takes a list of mp3 files and combines them into one file.

Jacob Mulford: 3/30/2015
"""

usage = """
Usage: python mp3combine.py <list of mp3 files> <outputfile>

Example: python mp3combine.py file1.mp3 file2.mp3 file3.mp3 out.mp3

This will combine file1.mp3, file2.mp3, and file3.mp3 into a single file
and saves that as out.mp3
"""

from echonest.remix import audio

def main(mp3_list, outfilename):
    collects = []

    for mp3 in mp3_list:
        audiofile = audio.LocalAudioFile(mp3)
        segs = audiofile.analysis.segments
        for seg in segs:
            collects.append(seg.render())
            
    out = audio.assemble(collects, numChannels=2)
    out.encode(outfilename)

if __name__ == '__main__':
    import sys
    mp3_list = []
    for i in range(1,len(sys.argv)-1):
        try:
            mp3_list.append(sys.argv[i])
        except:
            print usage
            sys.exit(-1)
    try:
        outfilename = sys.argv[len(sys.argv)-1]
    except:
        print usage
        sys.exit(-1)
    main(mp3_list, outfilename)
   
