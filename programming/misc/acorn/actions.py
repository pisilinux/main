#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    shelltools.system("npm install -g --prefix %s/usr" % get.installDIR())

    # Make a copy that changes symlinks to hard copies
    shelltools.system("rsync --archive --verbose --copy-links %s/usr/lib/node_modules/ %s/usr/lib/node_modules_cp/" % (get.installDIR(), get.installDIR()))

    # Remove and replace
    pisitools.removeDir("/usr/lib/node_modules/")
    shelltools.system("mv %s/usr/lib/node_modules_cp/ %s/usr/lib/node_modules/" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("LICENSE", "README*")