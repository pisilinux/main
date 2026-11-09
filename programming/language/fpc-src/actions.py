#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def install():
    shelltools.system(
        'mkdir -p "%s/usr/lib/fpc/src" && '
        'cp -a fpcsrc/. "%s/usr/lib/fpc/src/"'
        % (get.installDIR(), get.installDIR())
    )