import os
from subprocess import Popen, PIPE

#Traversing back from present working directory to ixp folder inside base folder
ixpHome = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, "ixp")
batchFile = os.path.join(os.path.dirname(__file__), 'cliBatch.bat')



cliBatchContent = "set AUTOSERV=DA2\nset IXP_SERVER_URL=http://amrs-autosys-d.bankofamerica.com\ntitle=%USERNAME%@DA2\nprompt=%USERNAME%@DA2$^^G"
cliBatchContent += "\nixautorep -J HGRX_GRADS_M_IRRBV_UPDATE_PERKEY_DEV3_CM"

#Setting IXP home path to batch file. Also writing job level commands
with open(batchFile, "w+") as f1:
    f1.write("@echo off\n\nset IXP_HOME="+os.path.abspath(ixpHome)+"\nset PATH=%PATH%;%IXP_HOME%\\bin\n\n")
    f1.write(cliBatchContent)


pipe = Popen(batchFile, shell=True, stdout=PIPE, stdin=PIPE)
(output, err) = pipe.communicate()
print(repr(output).replace("\\n'","\n").replace("\\n","\n").replace("b'","").replace("\\r","\r"))

#Removing the temporary batch file
os.remove(batchFile)