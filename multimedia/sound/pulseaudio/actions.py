#!/usr/bin/python
<<<<<<< HEAD
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, shelltools, pisitools, get

i = ''.join([
    '-Dalsadatadir=/usr/share/alsa-card-profile/mixer ',
    '-Dmodlibexecdir=/usr/lib/pulse/modules ',
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
    '-Dbluez5=false ',
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
		pisitools.dolib_so("libpulsecommon-14.2.so", "/usr/lib32/pulseaudio")
		pisitools.dolib_so("libpulsecommon-14.2.so", "/usr/lib32")
		pisitools.dolib_so("utils/libpulsedsp.so", "/usr/lib32/pulseaudio")
		shelltools.cd("pulse")
		for t in [
		"libpulse.so",
		"libpulse.so.0",
		"libpulse.so.0.23.0",
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

	pisitools.dodoc("NEWS", "README")
	pisitools.dohtml("build/doxygen/html/*")

=======
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

# FIXME: libpulsedsp.la should be added, but it doesn't build on our system
emul32_libs = "libpulsecommon-%s.la \
               libpulse.la \
               libpulse-simple.la \
               libpulse-mainloop-glib.la \
              " % get.srcVERSION()

def setup():
    options = "--prefix=/usr         \
               --sysconfdir=/etc     \
               --localstatedir=/var  \
               --libexecdir=/usr/libexec \
               --disable-dependency-tracking \
               --disable-static \
               --enable-bluez5 \
               --disable-rpath \
               --with-systemduserunitdir=no \
               --disable-oss-output \
               --enable-largefile \
               --disable-gconf \
               --with-speex \
               --with-system-user=pulse \
               --with-system-group=pulse \
               --with-access-group=pulse-access \
               --with-database=tdb \
               --disable-systemd-daemon \
               --disable-systemd-login \
               --disable-systemd-journal \
               --with-alsa-data-dir=/usr/share/alsa-card-profile/mixer \
               --with-module-dir=/usr/lib/pulse/modules \
               --with-udev-rules-dir=/lib/udev/rules.d"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --libexecdir=/usr/lib32 \
                     --disable-gconf \
                     --disable-gtk2 \
                     --disable-asyncns \
                     --disable-lirc \
                     --disable-x11 \
                     --disable-bluez4 \
                     --disable-oss-output \
                     --disable-oss-wrapper \
                     --disable-solaris \
                     --disable-manpages \
                     --disable-samplerate \
                     --disable-default-build-tests"

    shelltools.echo(".tarball-version", get.srcVERSION())
    #shelltools.system("NOCONFIGURE=1 ./bootstrap.sh")
    autotools.configure(options)

    pisitools.dosed("libtool", "CC(\s-shared\s)", r"CC -Wl,-O1,--as-needed\1")

def build():
    if get.buildTYPE() == "emul32":
        autotools.make("-C src %s" % emul32_libs)
        return

    autotools.make()

    #generate html docs
    autotools.make("doxygen")

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("-C src \
                              lib_LTLIBRARIES=\"%s\" \
                              DESTDIR=%s" % (emul32_libs, get.installDIR()),
                             "install-libLTLIBRARIES")
        autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-pkgconfigDATA")
        return

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Disable autospawn by default
    shelltools.system("sed -e '/autospawn/iautospawn= yes' -i '%s/etc/pulse/client.conf'" % get.installDIR())
    # Speed up pulseaudio shutdown
    # Lower resample quality, saves CPU
    shelltools.system("sed -e '/exit-idle-time/iexit-idle-time=0' \
                       -e '/resample-method/iresample-method=speex-float-0' \
                       -i '%s/etc/pulse/daemon.conf'" % get.installDIR())

    # Needed for service.py
    pisitools.dodir("/run/pulse")
    pisitools.dodir("/var/lib/pulse")

    # HAL is no longer supported by default
    pisitools.removeDir("/etc/dbus-1")

    pisitools.dodoc("README", "LICENSE", "GPL", "LGPL")
    pisitools.dohtml("doxygen/html/*")
>>>>>>> parent of 608f883d2... sil
