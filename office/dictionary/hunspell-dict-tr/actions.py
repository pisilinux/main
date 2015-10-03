#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import glob

WorkDir="."

def install():
    hunspell_tr = "/usr/lib/libreoffice/share/extensions/hunspell_tr"
    pisitools.dodir(hunspell_tr)
    hunspellfile = glob.glob("*.oxt")[0]
    shelltools.system("unzip %s -d %s/%s" % (hunspellfile, get.installDIR(), hunspell_tr))
    #for other applications
    pisitools.dosym("/usr/lib/libreoffice/share/extensions/hunspell_tr/dictionaries/tr-TR.aff","/usr/share/hunspell/tr-TR.aff")
    pisitools.dosym("/usr/lib/libreoffice/share/extensions/hunspell_tr/dictionaries/tr-TR.dic", "/usr/share/hunspell/tr-TR.dic")
