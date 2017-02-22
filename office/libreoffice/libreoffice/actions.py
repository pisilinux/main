#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

shelltools.export("LC_ALL", "C")

pixmaps = "/usr/share/pixmaps/"
LoVersion = "%s" % get.srcVERSION()
OurWorkDir = "%s/libreoffice-%s" % (get.workDIR(), LoVersion)

# temporarily disable failing tests, don't run broken tests on i686
if get.buildTYPE() == "i686":
    shelltools.system('sed -i "/CppunitTest_sw_ooxmlexport7/d" sw/Module_sw.mk')
    shelltools.system('sed -i -e /CppunitTest_sd_import_tests/d sd/Module_sd.mk')

def setup():
    shelltools.system('sed -i "s:mdds >= 0.12.0:mdds-1.0 >= 0.12.0:g" configure.ac')
    shelltools.chmod("%s/bin/unpack-sources" % OurWorkDir)
    shelltools.export("LO_PREFIX", "/usr")    
    shelltools.export("PYTHON", "python3.6")
    shelltools.cd(OurWorkDir)   
  
    shelltools.touch("autogen.lastrun")
    shelltools.system('sed -e "/distro-install-file-lists/d" -i Makefile.in')
    #shelltools.system('sed -e "/ustrbuf/a #include <algorithm>" \
                              ###-i svl/source/misc/gridprinter.cxx')
    shelltools.system('./autogen.sh                     \
                        --prefix=/usr                   \
                        --sysconfdir=/etc               \
                        --with-vendor="Pisi Linux"         \
                        --with-lang="ALL"               \
                        --enable-gtk3                   \
                        --with-help                     \
                        --with-myspell-dicts            \
                        --with-alloc=system             \
                        --with-java                     \
                        --without-system-dicts          \
                        --disable-postgresql-sdbc       \
                        --enable-release-build=yes      \
                        --enable-python=system          \
                        --with-system-boost             \
                        --with-system-curl              \
                        --with-system-cairo             \
                        --with-system-expat             \
                        --with-system-harfbuzz          \
                        --with-system-icu               \
                        --with-system-jpeg              \
                        --with-system-lcms2             \
                        --with-system-libpng            \
                        --with-system-libxml            \
                        --with-system-nss               \
                        --with-system-openssl           \
                        --with-system-poppler           \
                        --with-system-zlib              \
                        --enable-scripting-beanshell    \
                        --enable-scripting-javascript   \
                        --disable-odk                   \
                        --enable-ext-wiki-publisher     \
                        --enable-ext-nlpsolver          \
                        --disable-firebird-sdbc         \
                        --with-jdk-home=/usr/lib/jvm/java-7-openjdk \
                        --with-gdrive-client-id=413772536636.apps.googleusercontent.com \
                        --with-gdrive-client-secret=0ZChLK6AxeA3Isu96MkwqDR4 \
                        --with-parallelism=%s' % (get.makeJOBS().replace("-j","")))

def build():
    autotools.make("build-nocheck")

def install():
    autotools.rawInstall("DESTDIR=%s distro-pack-install" % get.installDIR())
    
    pisitools.remove("gid_Module*")
    
    pisitools.insinto("/usr/share/appdata/", "sysui/desktop/appstream-appdata/libreoffice-*.xml")
    
    for pix in ["libreoffice-base.png", "libreoffice-calc.png", "libreoffice-draw.png", "libreoffice-impress.png", "libreoffice-main.png", "libreoffice-math.png", "libreoffice-startcenter.png", "libreoffice-writer.png"]:
        pisitools.dosym("/usr/share/icons/hicolor/32x32/apps/%s" % pix, "/usr/share/pixmaps/%s" %pix)
