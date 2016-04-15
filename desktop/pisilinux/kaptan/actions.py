# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
import glob

projectDir = "/usr/lib/kaptan/"

def install():
    for file in glob.glob1(".", "*"):
        shelltools.chmod(file, 0755)
        
    for file in glob.glob1("languages", "*"):
        shelltools.chmod("languages/"+file, 0755)
        
    for file in glob.glob1("kaptan", "*"):
        shelltools.chmod("kaptan/"+file, 0755)
        
    for file in glob.glob1("data", "*"):
        shelltools.chmod("data/"+file, 0755)
        
    for file in glob.glob1("data/images", "*"):
        shelltools.chmod("data/images/"+file, 0755)
        
    pisitools.insinto("/usr/share/pixmaps/", "data/images/kaptan-icon.png", "kaptan.png")
    pisitools.insinto(projectDir, "data/")
    pisitools.insinto(projectDir, "languages/")
    pisitools.insinto(projectDir, "kaptan/")
    pisitools.insinto(projectDir, "kaptan.py", "kaptan5.py")
    pisitools.insinto(projectDir, "rc_kaptan.py")
    pisitools.insinto("/usr/bin/", "script/kaptan")
    
    
    
