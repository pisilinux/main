#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

arch = "x86_64" if get.ARCH() == "x86_64" else "i386"

#WorkDir = "source"

# this package is fragile to flags, you have been warned
#cflags = get.CFLAGS().replace("-fomit-frame-pointer", "")
#cxxflags = get.CXXFLAGS().replace("-fomit-frame-pointer", "")

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

#def build():
    #shelltools.cd("source/source")
    ##autotools.make("-C ../libsrcs/angelscript/angelSVN/sdk/angelscript/projects/gnuc")
    
    #shelltools.system("sed -i -e '/fs_basepath =/ s:\.:/usr/share/warsow:' qcommon/files.c")
    #shelltools.system("sed -i -e 's:q_jpeg_mem_src:_&:' ref_gl/r_image.c")
    
    #cmaketools.configure("-DQFUSION_GAME=Warsow")
    
    #autotools.make()

def install():
	
    #shelltools.cd("source/source")

    #pisitools.insinto("/usr/share/warsow", "build/warsow.%s" % arch, "warsow")
    #pisitools.insinto("/usr/share/warsow", "build/wsw_server.%s" % arch, "warsow-server")
    #pisitools.insinto("/usr/share/warsow", "build/wswtv_server.%s" % arch, "warsowtv-server")

    pisitools.dodir("/usr/share/warsow")
    #pisitools.insinto("/usr/share/warsow/", "build/basewsw")
    #pisitools.insinto("/usr/share/warsow/", "build/libs")
    
    #shelltools.cd("../../warsow_21")
    pisitools.insinto("/usr/share/warsow","libui_x86_64.so")
    pisitools.insinto("/usr/share/warsow","warsow.x86_64", "warsow")
    pisitools.insinto("/usr/share/warsow","wsw_server_x64.exe", "warsow-server")
    
    
    fixperms("basewsw")
    pisitools.insinto("/usr/share/warsow/basewsw", "basewsw/*")
    
    #shelltools.move("docs/license.txt", "docs/license-data.txt")
    pisitools.dodoc("docs/*", destDir="warsow")
