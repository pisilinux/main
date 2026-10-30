#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

def setup():
    srcdir = get.srcDIR()
    pnpm_home = os.path.join(srcdir, ".pnpm")

    shelltools.system('curl -fsSL https://get.pnpm.io | env PNPM_HOME="{0}" sh -'.format(pnpm_home))

    pnpm = os.path.join(pnpm_home, "bin", "pnpm")

    shelltools.system('"{0}" install --frozen-lockfile'.format(pnpm))
    shelltools.system('"{0}" run download-helper-binaries'.format(pnpm))

def build():
    srcdir = get.srcDIR()
    pnpm_home = os.path.join(srcdir, ".pnpm")
    pnpm_bin = os.path.join(pnpm_home, "bin")
    pnpm = os.path.join(pnpm_bin, "pnpm")

    shelltools.export("PATH", "{0}:{1}".format(pnpm_bin, os.environ.get("PATH", "")))
    shelltools.system('"{0}" dist:linux tar.xz'.format(pnpm))

def install():
    dest = get.installDIR()
    srcdir = os.getcwd()
    heroicdir = "/usr/share/heroic"
    distdir = os.path.join(srcdir, "dist", "linux-unpacked")
    bindir = os.path.join(distdir, "resources", "app.asar.unpacked", "build", "bin", "x64", "linux")

    pisitools.dodir(heroicdir)
    pisitools.dodir("/usr/bin")
    shelltools.system('cp -a "{0}/." "{1}{2}/"'.format(distdir, dest, heroicdir))
    pisitools.dosym("{0}/heroic".format(heroicdir), "/usr/bin/heroic-run")

    if os.path.isdir(bindir):
        for binfile in os.listdir(bindir):
            source = os.path.join(bindir, binfile)
            if os.path.isfile(source):
                pisitools.dosym(
                    "{0}/resources/app.asar.unpacked/build/bin/x64/linux/{1}".format(heroicdir, binfile),
                    "/usr/bin/{0}".format(binfile)
                )

    pisitools.insinto(
        "/usr/share/icons/hicolor/512x512/apps",
        os.path.join(distdir, "resources", "app.asar.unpacked", "build", "icon.png"),
        "com.heroicgameslauncher.hgl.png"
    )

    desktop = os.path.join(srcdir, "flatpak", "com.heroicgameslauncher.hgl.desktop")
    shelltools.system("sed -i 's/StartupWMClass.*/StartupWMClass=heroic/' '{0}'".format(desktop))
    pisitools.insinto("/usr/share/applications", desktop)
    pisitools.dodoc("COPYING", "README*", "Support*")