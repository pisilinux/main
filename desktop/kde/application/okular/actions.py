#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

def setup():
    kde5.configure("-DKDEPIM_NO_TEXTTOSPEECH=TRUE")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("AUTHORS", "COPYING*", "TODO")
