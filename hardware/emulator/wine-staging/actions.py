# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "wine-%s" % get.srcVERSION()

def setup():
    shelltools.system("install=wine.keyring")
    # For 32bit machines:
    #   * It get compiled with the normal options below. The emul32 are ignored
    #     on 32bit machines. Nothing is added to options variable.
    #
    # For 64bit machines:
    #   * First we compile for 64bit with the option --enable-win64. These build
    #     files are stored in the normal "work" dir
    #   * In the second run (for emul32 buildType), the 32bit part is compiled
    #     with the spesific libdir and the --with-wine64 options that is pointing
    #     to the 64bit files that was compiled in the first step (files in the work)
    #
    # More info can be obtained here: http://wiki.winehq.org/Wine64
    #shelltools.export("CPPFLAGS", "-U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0")
    #shelltools.system("make -C ./wine-staging-%s/patches DESTDIR=$(pwd) install" %get.srcVERSION())    
    #pisitools.flags.add("-fno-omit-frame-pointer")
    #shelltools.system("sed -i 's|OpenCL/opencl.h|CL/opencl.h|g'  configure*")
    
    shelltools.cd("wine-staging-%s" %get.srcVERSION())
    shelltools.system("./patches/patchinstall.sh DESTDIR=.. --all")
    shelltools.cd("..")
		
    
    autotools.autoreconf("-vif")
    options = "--without-capi \
               --without-oss \
               --without-opencl \
               --without-gstreamer \
               --without-hal \
               --with-dbus \
               --with-opengl \
               --with-alsa \
               --with-x \
               "

    if get.buildTYPE() == "emul32":
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig") 
        options += " --with-wine64=%s/work/wine-%s/build-wine \
                     --libdir=/usr/lib32 \
                   " % (get.pkgDIR(), get.srcVERSION())
                   
        shelltools.system("mkdir build-wine")
        shelltools.cd("build-wine")
        shelltools.system(". ../configure %s" %options)
        
    elif get.ARCH() == "x86_64":
        options += " --enable-win64 \
                     --libdir=/usr/lib \
                     "
        shelltools.system("mkdir build-wine")
        shelltools.cd("build-wine")
        shelltools.system(". ../configure %s" %options)



def build():
    shelltools.cd("build-wine")
    autotools.make()

def install():
    # We need especially specify libdir and dlldir prefixes. Otherwise the
    # 32bit parts overwrite the 64bit files under /usr/lib
    
    shelltools.cd("build-wine")

    if get.buildTYPE() == "emul32":
        autotools.install("UPDATE_DESKTOP_DATABASE=/bin/true libdir=%s/usr/lib32 dlldir=%s/usr/lib32/wine" % (get.installDIR(), get.installDIR()))
    else:
        autotools.install("UPDATE_DESKTOP_DATABASE=/bin/true libdir=%s/usr/lib dlldir=%s/usr/lib/wine" % (get.installDIR(), get.installDIR()))
        
    shelltools.cd("..")

    pisitools.dodoc("ANNOUNCE", "AUTHORS", "COPYING.LIB", "LICENSE*", "README", "documentation/README.*")
