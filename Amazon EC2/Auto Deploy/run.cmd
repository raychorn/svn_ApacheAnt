@echo off

REM (+++) Add the ability to force the creation of the imgile...

ant -Dsourcefile="J:\VirtualBox VMs\Ubuntu_Server_i386_11.04_(small)\Ubuntu_Server_i386_11.04_(small).vdi" -DvirtualBoxHome="C:\Program Files\Oracle\VirtualBox" -buildfile build.xml
