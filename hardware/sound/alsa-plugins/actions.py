#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

i = ''.join([
    ' -Wno-deprecated-declarations',
    ' -Wno-restrict',
    ' -Wno-stringop-truncation',
    ' -Wno-unused-result '
    ])

t = "99-pulseaudio-default.conf"

def setup():
	pisitools.cflags.add(i)
	autotools.configure("--enable-maemo-plugin --disable-static --with-speex=lib")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.insinto("/usr/share/alsa/alsa.conf.d", "pulse/%s.example" % t, "%s" % t)
	pisitools.dosym("/usr/share/alsa/alsa.conf.d/%s" % t, "/etc/alsa/conf.d/%s" % t)
	pisitools.remove("/etc/alsa/conf.d/98-maemo.conf")
	pisitools.dosym("/usr/share/alsa/alsa.conf.d/98-maemo.conf", "/etc/alsa/conf.d/98-maemo.conf")

	pisitools.dodoc("COPYING", "COPYING.GPL", "doc/*.txt", "doc/README*")

