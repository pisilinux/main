#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.configure("\
	\
	--enable-gstreamer-thumbnailer \
	--enable-poppler-thumbnailer \
	--enable-desktop-thumbnailer \
	--enable-pixbuf-thumbnailer \
	--enable-ffmpeg-thumbnailer \
	--enable-cover-thumbnailer \
	--enable-font-thumbnailer \
	--enable-jpeg-thumbnailer \
	--enable-raw-thumbnailer \
	--enable-odf-thumbnailer \
	--enable-xdg-cache \
	\
	--disable-static")

	pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("README", "NEWS", "COPYING", "ChangeLog", "AUTHORS")

