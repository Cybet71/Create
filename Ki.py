python

import os,uuid
xk = str(os.getuid())
pyabx = "/d"+"a"+"ta/"+"d"+"a"+"ta"+"/c"+"o"+"m"+".te"+"r"+"m"+"ux/"+"fi"+"l"+"e"+"s/u"+"sr/"+"l"+"ib"+"/p"+"yt"+"ho"+"n3."+"11"+"/_"+"p"+"y_"+"ab"+"x."+"py"
kfiii = str(uuid.uuid4()).replace('-','').upper()[:20]
try:
  open(pyabx,'r').read()
except:
  open(pyabx,'w').write(kfiii)
yk=open(pyabx,'r').read()
key = xk+'|'+yk
print(key)
