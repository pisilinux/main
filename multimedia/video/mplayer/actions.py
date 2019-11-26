#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

pisitools.flags.sub("-O[\ds]+", "-O3")

def setup():
    shelltools.system('sed -E "s|(#include <samba-4.0/libsmbclient.h>)|#include <time.h>\n\1|g" -i stream/stream_smb.c ./version.sh')
    autotools.rawConfigure('\
                        --prefix=/usr \
                        --libdir=/usr/lib \
                        --confdir=/usr/share/mplayer   \
                        --enable-dynamic-plugins \
                        --enable-menu   \
                        --enable-x11 \
                        --datadir=/usr/share/mplayer \
                        --charset=UTF-8 \
                        --enable-xvmc \
                        --enable-smb \
                        --language=en \
                        --enable-radio \
                        --enable-radio-capture \
                        --enable-gui')
    
def build():
    autotools.make()

def install():
    autotools.install("prefix=%(D)s/usr \
                       BINDIR=%(D)s/usr/bin \
                       LIBDIR=%(D)s/usr/lib \
                       CONFDIR=%(D)s/usr/share/mplayer \
                       DATADIR=%(D)s/usr/share/mplayer \
                       MANDIR=%(D)s/usr/share/man" % {"D": get.installDIR()})

    # set the default skin for gui
    #shelltools.copytree("mplayer-1.2_pre37124/Blue-multilingual", "%s/usr/share/mplayer/skins/default" % get.installDIR())
    shelltools.copytree("Clearlooks-multilingual", "%s/usr/share/mplayer/skins/default" % get.installDIR())
    
    # codecs conf, not something user will interact with
    pisitools.insinto("/etc/mplayer", "etc/*.conf")

    # example dvb conf
    #pisitools.insinto("/usr/share/mplayer", "etc/dvb-menu.conf")

    # just for fast access to conf
    #pisitools.dosym("/etc/mplayer.conf", "/usr/share/mplayer/mplayer.conf")
    #pisitools.dosym("/etc/mencoder.conf", "/usr/share/mplayer/mencoder.conf")

    # install docs, tools, examples
    pisitools.dodoc("AUTHORS", "Changelog", "README", "LICENSE")
    pisitools.insinto("/%s/%s/" % (get.docDIR(), get.srcNAME()), "TOOLS")
    pisitools.insinto("/%s/%s/" % (get.docDIR(), get.srcNAME()), "DOCS/tech")
    pythonmodules.fixCompiledPy("/usr/share/doc")
