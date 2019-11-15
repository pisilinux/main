#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-%s-src" % (get.srcNAME(), get.srcVERSION())
DATADIR = "/usr/share/teeworlds"
NoStrip = [DATADIR]

def setup():
    #shelltools.unlinkDir("src/engine/external/")
    shelltools.cd("../bam-0.5.1")
    shelltools.chmod("make_unix.sh", 0755)
    shelltools.system("./make_unix.sh")

def build():
    shelltools.system('CFLAGS="%s" ../bam-0.5.1/bam conf=release' % get.CFLAGS())

def install():
    pisitools.dobin("build/x86_64/release/teeworlds")
    pisitools.dobin("build/x86_64/release/teeworlds_srv")
    pisitools.insinto("/usr/share/teeworlds/data", "build/x86_64/release/data/*")
    pisitools.rename("/usr/bin/teeworlds_srv", "teeworlds-server")

    pisitools.insinto(DATADIR, "data")

    pisitools.dodoc("*.txt")
