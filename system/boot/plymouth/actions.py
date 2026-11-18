#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

LOGO_FILE = "/usr/share/pixmaps/plymouth-pisilinux.png"
THEMEPATH = "/usr/share/plymouth/themes"

def setup():
    # 26.x is meson-only. GTK stays enabled for the x11 renderer plugin and
    # docs stay enabled so the man pages shipped in pspec.xml still get built.
    mesontools.configure("-Dlogo=%s \
                          -Drelease-file=/etc/pisilinux-release \
                          -Dbackground-color=0x000000 \
                          -Dbackground-end-color-stop=0x000000 \
                          -Dbackground-start-color-stop=0x000000 \
                          -Dboot-tty=/dev/tty7 \
                          -Dshutdown-tty=/dev/tty1 \
                          -Dtracing=true \
                          -Dsystemd-integration=false" % LOGO_FILE)

def build():
    mesontools.build()

def install():
    mesontools.install()

    # meson installs the core libraries into /usr/lib; the package layout and
    # the initramfs file list expect them in /lib (as the old autotools build
    # with --with-system-root-install did).
    pisitools.domove("/usr/lib/libply.so*", "/lib")
    pisitools.domove("/usr/lib/libply-splash-core.so*", "/lib")

    # Copy necessary files for Charge theme
    pisitools.dodir("%s/charge" % THEMEPATH)
    for f in ("box", "bullet", "entry", "lock"):
        shelltools.copy("%s%s/glow/%s.png" % (get.installDIR(), THEMEPATH, f), "%s%s/charge/" % (get.installDIR(), THEMEPATH))

    # Remove glow theme as it's premature
    pisitools.removeDir("/usr/share/plymouth/themes/glow")

    # Generate initramfs filelist
    #shelltools.system("./generate-flist %s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "INSTALL", "README.md")
