import os
import subprocess as sp
sp.getoutput('yum update>f1')
f1=sp.getoutput('cat f1|tail -n +7')
f2="No packages marked for update"
if(f1==f2):
 print("Already updated!!")
