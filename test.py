import pyrealpro
from ABC_to_iReal.ABC_to_iReal import ABCTune
import unittest
from pyRealParser import Tune, convert_iReal_url
import urllib
from difflib import ndiff

abc=ABCTune(fileDir="abc/Amaranth Waltz.abc")
print(abc)

for section in abc.sections:
    print(section, abc.sections[section])

ATrain='irealb://Take%20The%20%27A%27%20Train%20%28Avner%20Winatra%29=Strahorn%20Billy==Medium%20Up=C==1r34LbKcu7yXC%7B%5D4C%2FG%20%20G%2FCZLbG%2FC%20G%2FCLZbG%2FC%20G%2FCZLbG%2FCC%2FGb%204Ti%2A%7CKQyX6LZ%20x%20%7B%7D%20%20x%20ZL%20x%20ZL%20clKQyXn1NZL%20x%20ZL%2AAN2C%20lcKQQyX%7D%20D9b5XC%7CQyX6C1N%7CQyX7%7CGQyX7%5EFZL%20lcKQyb6%20D6ZL%20lc7%5EF%2C7ZN2C6G%20%207%5EFZL%20lcKQy7X%5EFB%2A%5B%5D%20%20lcKQyX7%2C%7CE%2DL%20QyXL%20lcKE%2D7%2C%7CA%2A%5B%5D%209b7G%207G%7CQXy7%5EFZL%20lcKQyX7DC6XyQ%2C7%2DD%2CZD9b5XyQKcl%20LZF%5E7XyQ%7CG7XyQ%7CC6XyQKcl%20%20Z%20=Jazz%2DMedium%20Up%20Swing=140=30'
ATrain_original="irealb://Take%20The%20A%20Train%20%28C%29%3DEllington%20-%20Strayhorn%3D%3DMedium%20Swing%3DC%3D%3D1r34LbKcu71NZL%204C%5EXy7GZL%207-D%7CQyXx%7CyQX11%237%5ED%7CQyXx%7CQ%20LZC%5E4TA*%5B%7CQyXx%5BN2x%201%237%5ED%7CQyXx%7CQyX%7CxQyXx%7CQyX%5EFB*ZL1XyQ%7C%7DQyXx%207GZLQ%7CG7XQyXx%7CQyX11%237%5EDQ%7CyXx%7CQyX%5ECA*%7CQy%7CD-7%20yX7-D%2CQ%2CLZC%5EXyQ%7CxXyQZ%20%20%5BQC%5E%20LZx%20%20Z%20%3DJazz-Medium%20Swing%3D100%3D3"

#Fuchsia Swing Song, imported directly from Ireal forum
Fuchsia="irealb://Fuchsia%20Swing%20Song=Rivers%20Sam==Up%20Tempo%20Swing=Eb==1r34LbKcu7bB%7CQy%5E7%28Fh%287%5EBZL%20lcKQyX7b%5EE%7CQyX7bB%7CQyX%297Fh7%29XB44T%5B7%2DF%7CQEb%5E7X%7CQyX7%2DG%7CQyX7%2Db%7CAQyX7hAZL%20lcKQyGb7Xy%7CQyX7XyQ%7CBb7b9XyQ%7CEb%5E7XyQKcl%20%20Z%20=Jazz%2DUp%20Tempo%20Swing=285=8==="

#Fuchsia Swing Song, imported into IrealPro, then exported. 
Fuchsia_imported="irealb://Fuchsia%20Swing%20Song%3DRivers%20Sam%3D%3DUp%20Tempo%20Swing%3DEb%3D3%3D1r34LbKcu7bB%7CQy%5E7(Fh(7%5EBZL%20lcKQyX7b%5EE%7CQyX7bB%7CQyX)7Fh7)XB44T%5B7-F%7CQEb%5E7X%7CQyX7-G%7CQyX7-b%7CAQyX7hAZL%20lcKQyGb7Xy%7CQyX7XyQ%7CBb7b9XyQ%7CEb%5E7XyQKcl%20%20Z%20%3DJazz-Up%20Tempo%20Swing%3D285%3D8"

#def convert_iReal_url(url):
#    url.decode("ascii")
#    #url=url.replace("%3D","=")
#    #url=url.replace("irealb://","irealb://\n")
    
   # return url
"""
def convert_iReal_url(url):
    "" Removes encoding added to iReal tunes exported from the app.
    ""
    
    url=url.replace("irealb://","irealb://")
    url=url.replace("%3D","=")
    #url = urllib.parse.quote(url)
    url = urllib.parse.unquote(url)
    
    url=url.replace(" ","%20")
    #url=url.replace("^","%7C")
    url=url.replace("=1=","==")
    url=url.replace("=2=","==")
    url=url.replace("=3=","==")
    url=url.replace("=4=","==")
    url=url.replace("=5=","==")
    url=url.replace("=6=","==")
    url=url.replace("=7=","==")
    url=url.replace("=8=","==")
    url=url.replace("=9=","==")
    for letter in "^|()[]{}":
        print(letter,urllib.parse.quote(letter))
        url=url.replace(letter,urllib.parse.quote(letter))
    url=url.replace("/","%2F")
    url=url.replace("-","%2D")
    url=url+"==="
    return url
"""
print()
print(Fuchsia)
print()
print(convert_iReal_url(Fuchsia_imported))
print()

Fuchsia_converted=convert_iReal_url(Fuchsia_imported)

def compare(original,exported_before_conversion):
    exported=convert_iReal_url(exported_before_conversion)
    for i,char in enumerate(original):
        try:
            assert(original[i]==exported[i])
        except AssertionError:
            print(original[i-8:i+8],"\n",exported[i-8:i+8])
            break
compare(Fuchsia,Fuchsia_imported)

ThisIsForAlbert=         "irealb://This%20is%20for%20Albert=Shorter%20Wayne==Medium%20Up%20Swing=G==1r34LbKcu77%2DCZL4G%5E7XG%2F7%2DD%7CQyXG%2F7%2DAQ%7CyXG%2F11%237%5EbA%7CQy%20G7b94TA%2A%7BZL%20lcBb%5E7%20us7bDB%2A%5B%7DQyXtl7aD%7CQyX7%5EbAZL7bEsXyQKZL7F%20%5B%5DQyX1%2FC%23XQyX7%2DA%7CQyXtla7%7CEQyX7%2DBZL%20lcKQy%7CD7%2391%237%5EGL7F%207XyQ%7CAb7G%20G%2F7%2DD%7CQyXG7%2F%2DA%7CQyXG%2F11%237%5Eb9LZC%2D7%5EGA%2AZBb%5E7%20Eb7LZAb%5E7XyQ%7CD7altXyQZ%20==0=9==="
ThisIsForAlbert_imported="irealb://This%20is%20for%20Albert%3DShorter%20Wayne%3D%3DMedium%20Up%20Swing%3DG%3D7%3D1r34LbKcu77-CZL4G%5E7XG%2F7-D%7CQyXG%2F7-AQ%7CyXG%2F11%237%5EbA%7CQy%20G7b94TA*%7BZL%20lcBb%5E7%20us7bDB*%5B%7DQyXtl7aD%7CQyX7%5EbAZL7bEsXyQKZL7F%20%5B%5DQyX1%2FC%23XQyX7-A%7CQyXtla7%7CEQyX7-BZL%20lcKQy%7CD7%2391%237%5EGL7F%207XyQ%7CAb7G%20G%2F7-D%7CQyXG7%2F-A%7CQyXG%2F11%237%5Eb9LZC-7%5EGA*ZBb%5E7%20Eb7LZAb%5E7XyQ%7CD7altXyQZ%20%3DJazz-Medium%20Up%20Swing%3D160%3D9"

compare(ThisIsForAlbert,ThisIsForAlbert_imported)
compare(ATrain_original,ATrain)


#diffs=(ndiff(Fuchsia,convert_iReal_url(Fuchsia_imported)))

#print("".join(diffs))

Fuchsia_Tune=Tune.parse_ireal_url(Fuchsia_converted)
#print()
print(ATrain,"\n")
print(convert_iReal_url(ATrain),"\n")

ATrain_tune=Tune.parse_ireal_url(ATrain)



print(ATrain_tune)
#print(Fuchsia)