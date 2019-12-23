#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    pisitools.rename("/usr/bin/mid3cp","mid3cp-py3")
    pisitools.rename("/usr/bin/mid3v2","mid3v2-py3")
    pisitools.rename("/usr/bin/moggsplit","moggsplit-py3")
    pisitools.rename("/usr/bin/mid3iconv","mid3iconv-py3")
    pisitools.rename("/usr/bin/mutagen-pony","mutagen-pony-py3")
    pisitools.rename("/usr/bin/mutagen-inspect","mutagen-inspect-py3")
    pisitools.rename("/usr/share/man/man1/mid3cp.1","mid3cp-py3.1")
    pisitools.rename("/usr/share/man/man1/mid3v2.1","mid3v2-py3.1")
    pisitools.rename("/usr/share/man/man1/mid3iconv.1","mid3iconv-py3.1")
    pisitools.rename("/usr/share/man/man1/moggsplit.1","moggsplit-py3.1")
    pisitools.rename("/usr/share/man/man1/mutagen-pony.1","mutagen-pony-py3.1")
    pisitools.rename("/usr/share/man/man1/mutagen-inspect.1","mutagen-inspect-py3.1")