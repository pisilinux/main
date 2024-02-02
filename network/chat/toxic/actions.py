#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, get

j = ''.join([
    ' PREFIX=/usr',
    ' DISABLE_DESKTOP_NOTIFY=0',
    ' DISABLE_SOUND_NOTIFY=1',
    ' DISABLE_AV=0',
    ' DISABLE_X11=0',
    ' DISABLE_GAMES=0 '
    ])

def build():
	autotools.make(j)

def install():
	autotools.rawInstall("DESTDIR=%s PREFIX=/usr" % get.installDIR())
