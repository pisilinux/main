#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, shelltools, pisitools, get

i = ''.join([
    '-Dalsadatadir=/usr/share/alsa-card-profile/mixer ',
    '-Dmodlibexecdir=/usr/lib/pulse/modules ',
    '-Dsystemd=disabled ',
    '-Dsystem_user=pulse ',
    '-Dsystem_group=pulse ',
    '-Dudevrulesdir=/lib/udev/rules.d ',

    ])

j = ''.join([
    '--libdir=/usr/lib32 ',
    '--libexecdir=/usr/lib32 ',
    '-Dasyncns=disabled ',
    '-Davahi=disabled ',
    '-Dsoxr=disabled ',
    '-Djack=disabled ',
    '-Dlirc=disabled ',
    '-Dfftw=disabled ',
    '-Dgtk=disabled ',
    '-Dx11=disabled ',
    '-Delogind=disabled ',
    '-Dbluez5=disabled ',
    '-Dtests=false ',
    ])

def setup():
	options = "%s" % i

	if get.buildTYPE() == "emul32":
		options += "%s %s" % (i, j)
		shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())
	mesontools.configure(options)

def build():
	mesontools.build()
	mesontools.build("doxygen")

def install():
	if get.buildTYPE() != "emul32":
		shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

	if get.buildTYPE() == "emul32":
		shelltools.cd("build/src")
		pisitools.insinto("/usr/lib32/cmake", "../*.cmake")
		pisitools.insinto("/usr/lib32/pkgconfig", "../*.pc")
		pisitools.dolib_so("libpulsecommon-16.0.so", "/usr/lib32/pulseaudio")
		pisitools.dolib_so("libpulsecommon-16.0.so", "/usr/lib32")
		pisitools.dolib_so("utils/libpulsedsp.so", "/usr/lib32/pulseaudio")
		shelltools.cd("pulse")
		for t in [
		"libpulse.so",
		"libpulse.so.0",
		"libpulse.so.0.24.2",
		"libpulse-simple.so",
		"libpulse-simple.so.0",
		"libpulse-simple.so.0.1.1",
		"libpulse-mainloop-glib.so",
		"libpulse-mainloop-glib.so.0",
		"libpulse-mainloop-glib.so.0.0.6",
		]:
			pisitools.insinto("/usr/lib32", t)

	shelltools.cd("%s/%s" % (get.workDIR(), get.srcDIR()))

	# Disable autospawn by default
	shelltools.system("sed -e '/autospawn/iautospawn= yes' -i '%s/etc/pulse/client.conf'" % get.installDIR())

	# Needed for service.py
	pisitools.dodir("/run/pulse")
	pisitools.dodir("/var/lib/pulse")

	pisitools.dodir("/etc/pulse/default.pa.d")

	pisitools.dodoc("NEWS", "README")
	pisitools.dohtml("build/doxygen/html/*")

