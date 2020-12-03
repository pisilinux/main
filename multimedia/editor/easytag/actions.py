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
	--enable-man \
	--enable-mp3 \
	--enable-ogg \
	--enable-mp4 \
	--enable-opus \
	--enable-flac \
	--enable-speex \
	--enable-id3v23 \
	--enable-wavpack \
	\
	--disable-schemas-compile \
	--disable-nautilus-actions")

def build():
	autotools.make()

def check():
	pass
#	autotools.make("check")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "THANKS", "TODO")

