#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def build():
    autotools.make()


def install():
    pisitools.insinto("/usr/share/locale", "po-export/*")
    pisitools.insinto("/usr/share/locale", "usr/share/locale/*")

    pisitools.dodoc("README*", "COPYING")
