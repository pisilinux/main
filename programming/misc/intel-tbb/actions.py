#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="tbb%soss" % (get.srcVERSION().replace(".", ""))


def install():
    shelltools.system("./install.sh %s" % get.installDIR())

    pisitools.dodoc("README", "COPYING")
