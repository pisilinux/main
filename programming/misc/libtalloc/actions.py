#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

libdir = "lib32" if get.buildTYPE() == "emul32" else "lib"
jobs = get.makeJOBS().replace("-j", "")

def setup():
    options = "--sysconfdir=/etc/samba \
               --builtin-libraries=replace \
               --bundled-libraries=NONE \
               --disable-rpath \
               --disable-rpath-install \
               --disable-silent-rules \
               --enable-talloc-compat1"
               
                
    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                   "
                   
    elif get.ARCH() == "x86_64":
        options += " --extra-python=/usr/bin/python \
                   "
                   
    autotools.configure(options)

def build():
    autotools.make("JOBS=%s" % jobs)

def install():
    autotools.rawInstall("DESTDIR=%s JOBS=%s" % (get.installDIR(), jobs))
    
    if get.buildTYPE() == "emul32":
        return

    #pisitools.removeDir("/usr/share/swig")

    #pisitools.remove("/usr/lib*/*.a")
    #pisitools.remove("/usr/lib*/libtalloc-compat1-%s.so" % get.srcVERSION())

    # Create symlinks for so file
    #pisitools.dosym("libtalloc.so.%s" % get.srcVERSION(), "/usr/%s/libtalloc.so.%s" % (libdir, get.srcVERSION().split(".")[0]))
    #pisitools.dosym("libtalloc.so.%s" % get.srcVERSION(), "/usr/%s/libtalloc.so" % libdir)

    pisitools.dodoc("NEWS")
