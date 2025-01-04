#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


# ObjDir = "build"
MOZAPPDIR= "/usr/lib/thunderbird"
shelltools.export("SHELL", "/bin/sh")
shelltools.export("PYTHON", "/usr/bin/python3")
# shelltools.export("MACH_USE_SYSTEM_PYTHON", "1")
shelltools.system("export MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=none")
shelltools.export("MOZBUILD_STATE_PATH", "mozbuild")

locales = "be ca  da  de  el  en-GB en-US  es-AR  es-ES  fi  fr  hr  hu  it  lt nl  pl  pt-BR  pt-PT  ro  ru  sr  sv-SE  tr  uk".split()
xpidir = "%s/xpi" % get.workDIR()
arch = get.ARCH()
ver = ".".join(get.srcVERSION().split(".")[:3])

def setup():    
    pisitools.dosed(".mozconfig", "##JOBCOUNT##", get.makeJOBS())

    # LOCALE
    shelltools.system("rm -rf langpack-tb/*/browser/defaults")
    if not shelltools.isDirectory(xpidir): shelltools.makedirs(xpidir)
    for locale in locales:
        shelltools.system("wget -c -P %s http://ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/%sesr/linux-%s/xpi/%s.xpi" % (xpidir, ver, arch, locale))

        shelltools.makedirs("langpack-tb")
        shelltools.system("cp %s/%s.xpi langpack-tb/langpack-%s@thunderbird.mozilla.org.xpi" % (xpidir, locale, locale))
        #shelltools.makedirs("langpack-tb/langpack-%s@thunderbird.mozilla.org" % locale)
        #shelltools.system("unzip -uo %s/%s.xpi -d langpack-tb/langpack-%s@thunderbird.mozilla.org" % (xpidir, locale, locale))

    # shelltools.makedirs(ObjDir)
    # shelltools.cd(ObjDir)
    shelltools.system("./mach configure")

def build():
    # shelltools.cd(ObjDir)
    shelltools.system("./mach build")
    shelltools.system("./mach buildsymbols")

def install():
    # shelltools.cd(ObjDir)
    shelltools.system("DESTDIR=%s ./mach install " % get.installDIR())

    # shelltools.cd("..")

    # Install fix language packs
    pisitools.insinto("/usr/lib/thunderbird/extensions", "langpack-tb/*")

    pisitools.insinto("/usr/share/metainfo", "comm/mail/branding/thunderbird/net.thunderbird.Thunderbird.appdata.xml")

    # Install icons
    pisitools.insinto("/usr/share/pixmaps", "comm/mail/branding/thunderbird/default256.png", "thunderbird.png")
    pisitools.insinto("%s/icons" % MOZAPPDIR, "comm/mail/branding/thunderbird/default16.png")

    for s in (16, 22, 24, 32, 48, 64, 128, 256):
        pisitools.insinto("/usr/share/icons/hicolor/%dx%d/apps" % (s,s), "comm/mail/branding/thunderbird/default%d.png" % s, "thunderbird.png")

    # We don't want the development stuff
    #pisitools.removeDir("/usr/lib/thunderbird-devel*")
    #pisitools.removeDir("/usr/share/idl")
    #pisitools.removeDir("/usr/include")

    # Install docs
    pisitools.dodoc("README*", "LICENSE")
