#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools, shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


WorkDir = '.'


def setup():
    shelltools.move('Apache License.txt', 'LICENSE')
    shelltools.chmod('*.ttf', 0o644)


def install():
    pisitools.insinto('/usr/share/fonts/TTF/', '*.ttf')
    pisitools.dodoc('LICENSE')
