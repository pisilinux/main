#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", get.LDFLAGS())

    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DMOD_OPENCV=ON \
                          -DMOD_GLAXNIMATE=ON \
                          -DSWIG_PERL=ON \
                          -DCMAKE_INSTALL_MANDIR=/usr/share/man/man1 \
                          -DSWIG_PYTHON=ON", sourceDir="..")

    #autotools.configure("--enable-gpl \
                         #--enable-gpl3 \
                         #--disable-gtk2 \
                         #--qt-libdir=/usr/lib/ \
                         #--qt-includedir=/usr/include/qt5 \
                         #--avformat-vdpau \
                         #--avformat-swscale")

    # Enable bindings
    #shelltools.echo("%s/src/swig/config.mak" % get.curDIR(), "SUBDIRS = perl python")

def build():
    shelltools.cd("build")
    cmaketools.make()
    #cmaketools.make("-C src/swig")

    #autotools.make()
    #autotools.make("-C src/swig")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # We should manually install the bindings :(
    #pisitools.insinto("/usr/lib/%s/site-packages/" % get.curPYTHON(), "src/swig/python/mlt.py")
    #pisitools.dolib("src/swig/python/_mlt.so", "/usr/lib/%s/site-packages/" % get.curPYTHON())

    #pisitools.insinto("/usr/lib/perl5/vendor_perl/%s/" % get.curPERL(), "src/swig/perl/blib/lib/mlt.pm")
    #pisitools.dolib("src/swig/perl/blib/arch/auto/mlt/mlt.so", "/usr/lib/perl5/vendor_perl/%s/i686-linux-thread-multi/auto/mlt/" % get.curPERL())


    shelltools.cd("..")
    pisitools.dodoc("COPYING", "GPL*", "README*")
