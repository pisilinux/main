#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i 's/cicero //g' configure.ac")
    shelltools.system("sed -i 's/sd_cicero//g' src/modules/Makefile.am")
    
    autotools.autoreconf("-i")
    autotools.configure("--disable-static \
                         --enable-shared \
                         --without-flite \
                         --with-alsa \
                         --with-espeak \
                         --with-libao \
                         --with-pulse \
                         --with-baratinoo=no \
                         --with-kali=no \
                         --with-default-audio-method=alsa")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #autotools.install()

    # Conflicts with openTTS
    pisitools.remove("/usr/share/info/ssip.info")

    # Set executable bit
    shelltools.chmod("%s/usr/lib/python3.6/site-packages/speechd/_test.py" % get.installDIR(), 0755)

    # Create log directory, it should be world unreadable
    pisitools.dodir("/var/log/speech-dispatcher")
    shelltools.chmod("%s/var/log/speech-dispatcher" % get.installDIR(), 0700)

    pisitools.dodoc("AUTHORS", "COPYING*", "README*")
