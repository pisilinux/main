#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def install():
    pisitools.dodir("/usr/lib/prebootloader")
    pisitools.dolib("*.efi", "/usr/lib/prebootloader/")
