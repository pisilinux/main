# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools

def setup():
    options_cfg = ''.join([
                  '-DUSE_TBB=ON ',
                  '-DUSE_VTK=True ',
                  '-DINSTALL_VTK=False',
                  '-DUSE_GL2PS=ON ',
                  '-DUSE_FFMPEG=ON ',
                  '-DUSE_FREEIMAGE=OFF ',
                  '-DINSTALL_DIR_LIB=/usr/lib ',
                  '-DCMAKE_INSTALL_PREFIX=/usr',
                  '-D3RDPARTY_VTK_LIBRARY_DIR=/usr/lib',
                  '-D3RDPARTY_VTK_INCLUDE_DIR=/usr/include',
                  '-DINSTALL_DIR_CMAKE=/usr/lib/cmake/opencascade',
                  ])
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("%s" % options_cfg, sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("..")

    pisitools.dodoc("LICENSE*", "OCCT_LGPL*")
