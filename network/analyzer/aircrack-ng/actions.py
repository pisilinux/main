#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def build():
    autotools.make("sqlite=true experimental=true pcre=true")

def install():
    autotools.install("sqlite=true experimental=true pcre=true")
    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE", "README", "VERSION")
