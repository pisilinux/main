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
    
    pisitools.cflags.add("-fcommon")
    #autotools.autoreconf("-i")
    autotools.configure("--disable-static \
                         --enable-shared \
                         --without-flite \
                         --without-espeak \
                         --with-espeak-ng \
                         --with-espeak \
                         --with-alsa \
                         --with-libao \
                         --with-pulse \
                         --with-ibmtts=no \
                         --with-baratinoo=no \
                         --with-kali=no \
                         --with-voxin=no \
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
    shelltools.chmod("%s/usr/lib/python3.11/site-packages/speechd/_test.py" % get.installDIR(), 0755)

    # Create log directory, it should be world unreadable
    pisitools.dodir("/var/log/speech-dispatcher")
    shelltools.chmod("%s/var/log/speech-dispatcher" % get.installDIR(), 0700)
    
    shelltools.system("""sed -e 's/# AudioOutputMethod "pulse"/AudioOutputMethod "pulse,alsa"/' -i %s/etc/speech-dispatcher/speechd.conf""" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README*")
