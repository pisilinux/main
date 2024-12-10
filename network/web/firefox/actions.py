#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

import subprocess

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

#WorkDir = "mozilla-release-6b51784853e47e091d213d421a19cb623af718f0"
ObjDir = "objdir"
locales = "az bs ca  da  de  el  en-US en-GB  es-AR  es-CL  es-ES  fi  fr  hr  hu  it  lt nl  pl  pt-BR  pt-PT  ro  ru  sr  sv-SE  tr  uk".split()
xpidir = "%s/xpi" % get.workDIR()
arch = get.ARCH()
ver = ".".join(get.srcVERSION().split(".")[:3])

jobs = jobs = "-j"+ subprocess.check_output("nproc 2>/dev/null", shell=True).rstrip("\n")

shelltools.export("SHELL", "/bin/sh")
shelltools.export("PYTHON", "/usr/bin/python3")
# shelltools.export("MACH_USE_SYSTEM_PYTHON", "1")
shelltools.system("export MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE='system'")
shelltools.system("export MOZBUILD_STATE_PATH='mozbuild'")
shelltools.system("export MOZ_NOSPAM=1")

def setup():
	
    shelltools.system("echo 'Instrumenting Firefox for PGO'")
    shelltools.system("cp mozconfig-inst .mozconfig")
	
    # Google API key
    shelltools.echo("google_api_key", "AIzaSyBINKL31ZYd8W5byPuwTXYK6cEyoceGh6Y")
    pisitools.dosed(".mozconfig", "%%PWD%%", get.curDIR())
    pisitools.dosed(".mozconfig", "%%FILE%%", "google_api_key")
    pisitools.dosed(".mozconfig", "##JOBCOUNT##", jobs)

    # LOCALE
    shelltools.system("rm -rf langpack-ff/*/browser/defaults")
    if not shelltools.isDirectory(xpidir): shelltools.makedirs(xpidir)
    for locale in locales:
        shelltools.system("wget -c -P %s https://download-origin.cdn.mozilla.net/pub/firefox/releases/%s/linux-%s/xpi/%s.xpi" % (xpidir, ver, arch, locale))
        #shelltools.makedirs("langpack-ff/langpack-%s@firefox.mozilla.org" % locale)
        shelltools.makedirs("langpack-ff")
        #shelltools.system("unzip -uo %s/%s.xpi -d langpack-ff/langpack-%s@firefox.mozilla.org" % (xpidir, locale, locale))
        shelltools.system("cp %s/%s.xpi langpack-ff/langpack-%s@firefox.mozilla.org.xpi" % (xpidir, locale, locale))
        print "Replacing browser.properties for %s locale" % locale
        #shelltools.copy("browserconfig.properties", "langpack-ff/langpack-%s@firefox.mozilla.org/browser/chrome/%s/locale/branding/" % (locale, locale))
        shelltools.copy("browserconfig.properties", "browser/branding/official/locales/")

    #shelltools.makedirs(ObjDir)
    #shelltools.cd(ObjDir)

    #shelltools.system("../configure --prefix=/usr --libdir=/usr/lib --disable-strip --disable-install-strip")
    
    
def build():
    shelltools.system("echo 'Building instrumented browser'")
    #shelltools.cd(ObjDir)
    shelltools.system("./mach build")
    
    shelltools.system("echo 'Profiling instrumented browser...'")
    shelltools.system("./mach package")
    shelltools.system("LLVM_PROFDATA=llvm-profdata \
                       JARLOG_FILE='%s/jarlog' \
                       xvfb-run -s '-screen 0 1920x1080x24 -nolisten local' \
                       ./mach python3 build/pgo/profileserver.py" %get.curDIR())
    
    shelltools.system("echo 'Removing instrumented browser...'")    
    shelltools.system("./mach clobber")
    
    shelltools.system("echo 'Building optimized browser...'")  
    shelltools.system("rm .mozconfig")
    shelltools.system("cp mozconfig-opt .mozconfig")
    #shelltools.echo("google_api_key", "AIzaSyBINKL31ZYd8W5byPuwTXYK6cEyoceGh6Y")
    pisitools.dosed(".mozconfig", "%%PWD%%", get.curDIR())
    pisitools.dosed(".mozconfig", "%%FILE%%", "google_api_key")
    pisitools.dosed(".mozconfig", "##JOBCOUNT##", jobs)
    #shelltools.system("../configure --prefix=/usr --libdir=/usr/lib --disable-strip --disable-install-strip")
    shelltools.system("./mach build")

def install():
    #shelltools.cd(ObjDir)
    shelltools.system("DESTDIR=%s ./mach install " % get.installDIR())
    
    #shelltools.cd("..")

    # Install language packs
    pisitools.insinto("/usr/lib/firefox/browser/extensions", "./langpack-ff/*")

    # Create profile dir, we'll copy bookmarks.html in post-install script
    pisitools.dodir("/usr/lib/firefox/browser/defaults/profile")

    # Install branding icon
    pisitools.insinto("/usr/share/pixmaps", "browser/branding/official/default256.png", "firefox.png")

    for s in (16, 22, 24, 32, 48, 64, 128, 256):
        pisitools.insinto("/usr/share/icons/hicolor/%dx%d/apps" % (s,s), "browser/branding/official/default%d.png" % s, "firefox.png")

    pisitools.insinto("/usr/share/icons/hicolor/192x192/apps", "browser/branding/official/content/about-logo.png", "firefox.png")
    pisitools.insinto("/usr/share/icons/hicolor/384x384/apps", "browser/branding/official/content/about-logo@2x.png", "firefox.png")
    pisitools.insinto("/usr/share/icons/hicolor/scalable/apps", "browser/branding/official/content/about-logo.svg", "firefox.svg")
    
    # Install docs
    pisitools.dodoc("README*", "LICENSE")
