#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr sysconfdir=/etc" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README*")
