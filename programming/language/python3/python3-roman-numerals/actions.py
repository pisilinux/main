#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get



WorkDir="roman-numerals-%s/python" % get.srcVERSION()

def build():
    python3modules.compile("--skip-dependency-check")

def install():
    python3modules.install()

    # pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "NEWS", "README")
