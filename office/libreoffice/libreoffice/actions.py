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
    #shelltools.system('sed -i "s:mdds >= 0.12.0:mdds-1.0 >= 0.12.0:g" configure.ac')
    shelltools.chmod("%s/bin/unpack-sources" % OurWorkDir)
    shelltools.export("LO_PREFIX", "/usr")    
    shelltools.export("PYTHON", "python3.6")
    shelltools.cd(OurWorkDir)   
  
    shelltools.touch("autogen.lastrun")
    shelltools.system('sed -e "/distro-install-file-lists/d" -i Makefile.in')
    shelltools.system('./autogen.sh         \
                        --prefix=/usr      \
                        --sysconfdir=/etc               \
                        --with-vendor="Pisi Linux"         \
                        --with-lang="ALL"      \
                        --enable-gtk3         \
                        --with-help            \
                        --with-myspell-dicts  \
                        --with-alloc=system      \
                        --with-java                     \
                        --without-system-dicts          \
                        --without-fonts    \
                        --disable-postgresql-sdbc       \
                        --disable-firebird-sdbc     \
                        --disable-coinmp \
                        --disable-systray \
                        --without-system-hsqldb \
                        --enable-release-build=yes      \
                        --enable-python=system          \
                        --with-system-apr           \
                        --with-system-boost             \
                        --with-system-cairo             \
                        --with-system-clucene   \
                        --with-system-cppunit \
                        --with-system-curl              \
                        --with-system-expat             \
                        --with-system-graphite      \
                        --with-system-glew \
                        --with-system-glm \
                        --with-system-harfbuzz          \
                        --with-system-hunspell \
                        --with-system-icu               \
                        --with-system-jpeg              \
                        --with-system-lcms2             \
                        --with-system-libcdr \
                        --without-system-libcmis \
                        --with-system-libetonyek     \
                        --with-system-libmspub \
                        --with-system-libodfgen \
                        --with-system-libpagemaker \
                        --with-system-libpng            \
                        --with-system-librevenge \
                        --with-system-libvisio           \
                        --with-system-libwpd  \
                        --with-system-libwpg  \
                        --with-system-libwps  \
                        --with-system-libxml            \
                        --with-system-mdds            \
                        --with-system-liblangtag  \
                        --without-system-libstaroffice \
                        --without-system-libzmf \
                        --with-system-neon          \
                        --with-system-nss               \
                        --with-system-odbc          \
                        --with-system-openldap      \
                        --with-system-openssl           \
                        --without-system-orcus \
                        --with-system-poppler           \
                        --with-system-postgresql    \
                        --with-system-redland  \
                        --with-system-serf          \
                        --without-system-ucpp \
                        --with-system-zlib              \
                        --with-system-libetonyek \
                        --enable-scripting-beanshell    \
                        --enable-scripting-javascript   \
                        --disable-odk                   \
                        --enable-ext-wiki-publisher     \
                        --enable-ext-nlpsolver          \
                        --with-jdk-home=/usr/lib/jvm/java-7-openjdk \
                        --with-external-tar=external/tarballs \
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
