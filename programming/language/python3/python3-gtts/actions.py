#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules

#WorkDir="gtts-%s" % get.srcVERSION()

def build():
    python3modules.compile()

def install():
    python3modules.install()
