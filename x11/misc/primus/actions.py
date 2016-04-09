 
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.system("LIBDIR=lib make")
    shelltools.system("LIBDIR=lib32 CXX='g++ -m32' make")
    
   

def install():
    pisitools.insinto("/etc/bash_completion.d", "primus.bash-completion", "primusrun")
    pisitools.dobin("primusrun")
    
    pisitools.insinto("/usr/lib/primus", "lib/*")
    pisitools.insinto("/usr/lib32/primus", "lib32/*")
    
    pisitools.dodoc("LICENSE.txt","README.md", "technotes.md")
    pisitools.doman("primusrun.1")