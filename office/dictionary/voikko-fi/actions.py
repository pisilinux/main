#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, get

def build():
	autotools.make("vvfst")

def install():
	autotools.make("DESTDIR=%s/usr/share/voikko vvfst-install" % get.installDIR())
