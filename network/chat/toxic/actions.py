#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, get

j = ''.join([
    ' PREFIX=/usr',
    ' DISABLE_{SOUND,DESKTOP}_NOTIFY=0',
    ' DISABLE_{AV,VI,X11}=0',
    ' DISABLE_GAMES=1 '
    ])

def build():
	autotools.make(j)

def install():
	autotools.rawInstall("DESTDIR=%s PREFIX=/usr" % get.installDIR())
