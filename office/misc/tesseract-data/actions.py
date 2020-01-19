#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def install():
    for f in ["tur*", "aze.*", "aze_*","eng*", "deu*", "fra*", "ita*", "jpn*", "rus*", "spa*"]:
        pisitools.insinto("/usr/share/tessdata", f)
    
    #shelltools.chmod(get.installDIR() + "/usr/share/tessdata/*")