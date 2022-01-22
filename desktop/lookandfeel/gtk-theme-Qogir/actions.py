#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def install():
    pisitools.dodir ("/usr/share/themes")
    shelltools.system("./install.sh --theme default --tweaks image square round --dest '%s/usr/share/themes'" % get.installDIR())
    pisitools.dodoc ("AUTHORS", "COPYING")	
	

