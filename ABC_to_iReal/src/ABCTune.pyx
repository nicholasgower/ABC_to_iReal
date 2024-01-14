import pyrealpro
from pyrealpro import Measure, TimeSignature
from pyRealParser import Tune
import re
#from libcpp cimport bool
cdef class ABCTune:
    cdef str abc
    cdef object sections
    
    def __cinit__(self,file=None,fileDir=None,str text=None):
        #print("ABCTune Loaded")
        inputs=[file,fileDir,text]
        assert len(set(inputs))==2 #Assert that exactly one of file, fileDir, or text is defined
        
        if file:
            abc_new=file.read()
        elif fileDir:
            with open(fileDir,'r') as fileRead:
                abc_new=fileRead.read()
        elif text:
            abc_new=text
        self.abc=abc_new
        self.abc=self.abc.replace("\r\n","\n")
        self.sections={}
        for line in self.abc.split("\n"):
            letter=line[0]
            start=2
            if not line[1]==":":
                letter="notes"
                start=0
            if letter not in self.sections.keys():
                self.sections[letter]=[line[start:]]
            else:
                self.sections[letter].append(line[start:])
            
            
    def __str__(self):
        return self.abc
    cpdef str getChords(self):
        chord= re.compile('\"[A-Za-z1-9#]{1,}\"')
        cdef str measures, out
        
        measures="\n".join(self.sections["notes"])
        out=""
        cdef bint inCurly=False
        
        for char in measures:
            if char in ":|{}[]\n! ":
                out+=char
            
            elif char == '"':
                inQuote=not inQuote
                out+=char
            elif char in '{}':
                inQuote=not inQuote
                out+=char
            elif inQuote:
                out+=char
            elif char.isalpha():
                out+="z"
            elif char.isnumeric():
                out+=char
        return out
    def getChordMeasures(self):
        measures=self.getChords().split("|")
    def to_iReal(self):
        time_sig_str=self.sections["M"][0].split("/")
        time_sig=TimeSignature(beats=int(time_sig_str[0]),duration=int(time_sig_str[1]))
        
        
        out=pyrealpro.Song(
            title=self.sections["T"][0],
            key=self.sections["K"][0],
            style="Medium Swing",
            composer=self.sections["C"][0]
            )
        
        
        out.measures.append(Measure(chords="C7",barline_open="{"))
        out.measures.append(Measure(chords="D7",barline_open="}"))
        url=out.url()
        
        return url.replace("irealbook://","irealb://")
        
#def iReal_to_ABC(link):
#    pass        
    