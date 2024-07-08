#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import shelltools

LOGO_FILE = "/usr/share/pixmaps/plymouth-pisilinux.png"
THEMEPATH = "/usr/share/plymouth/themes"

def setup():
    pisitools.ldflags.add(" -ludev ")
    # /var/run => /run
    # pisitools.dosed("configure.ac", "^(\s+plymouthruntimedir=)\$localstatedir(\/run\/plymouth)", r"\1\2")
    # pisitools.dosed("src/Makefile.am", "^(plymouthdrundir\s=\s)\$\(localstatedir\)(\/run\/plymouth)", r"\1\2")

    # autotools.autoreconf("-fis")

    # The end-start colors seems to be used by the two-step plugin
    # Disable nouveau drm renderer as it causes hangs when starting X server
    mesontools.configure("-Dtracing=true \
                         -Dlogo=%s \
                         --bindir=/bin \
                         --sbindir=/sbin \
                         -Drelease-file=/etc/pisilinux-release \
                         -Dbackground-color=0x000000 \
                         -Dbackground-end-color-stop=0x000000 \
                         -Dbackground-start-color-stop=0x000000 \
                         -Dboot-tty=/dev/tty7 \
                         -Dshutdown-tty=/dev/tty1 \
                         -Dsystemd-integration=false  \
                         " % LOGO_FILE)

    # --with-system-root-install \
    # --with-log-viewer \
    # --disable-libdrm_nouveau \
    # --disable-tests \
    # --disable-static \
    # --enable-gdm-transition \
    # --without-rhgb-compat-link

def build():
    mesontools.build()
    # autotools.make()


def install():
    pisitools.insinto("/usr/share/pixmaps", "plymouth-pisilinux.png")
    mesontools.install()
    # autotools.rawInstall("DESTDIR='%s'" % get.installDIR())

    # Copy necessary files for Charge theme
    pisitools.dodir("%s/charge" % THEMEPATH)
    for f in ("box", "bullet", "entry", "lock"):
        shelltools.copy("%s%s/glow/%s.png" % (get.installDIR(), THEMEPATH, f), "%s%s/charge/" % (get.installDIR(), THEMEPATH))

    # Remove glow theme as it's premature
    pisitools.removeDir("/usr/share/plymouth/themes/glow")

    # Generate initramfs filelist
    #shelltools.system("./generate-flist %s" % get.installDIR())

    pisitools.dodoc("COPYING", "README*", "AUTHORS")
