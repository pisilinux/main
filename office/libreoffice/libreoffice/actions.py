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

#for support all languages.
langall="en-US af am ar as ast be bg bn bn-IN bo br brx bs ca ca-valencia cs cy da de dgo dsb dz el en-GB en-ZA eo es et eu fa fi fr fy ga gd gl gu gug he hsb hi hr hu id is it ja ka kab kk km kmr-Latn kn ko kok ks lb lo lt lv mai mk ml mn mni mr my nb ne nl nn nr nso oc om or pa-IN pl pt pt-BR ro ru rw sa-IN sat sd sr-Latn si sid sk sl sq sr ss st sv sw-TZ ta te tg th tn tr ts tt ug uk uz ve vec vi xh zh-CN zh-TW zu"

#only Turkish and English.
lang="tr"

def setup():
    shelltools.chmod("%s/bin/unpack-sources" % OurWorkDir)
    shelltools.export("LO_PREFIX", "/usr")    
    shelltools.export("PYTHON", "python3.6")
    
    # http://site.icu-project.org/download/61#TOC-Migration-Issues
    shelltools.export("CPPFLAGS", "-DU_USING_ICU_NAMESPACE=1")
    shelltools.cd(OurWorkDir)   
  
    shelltools.touch("autogen.lastrun")
    shelltools.system('sed -e "/distro-install-file-lists/d" -i Makefile.in')
    shelltools.system('./autogen.sh         \
                        --prefix=/usr      \
                        --sysconfdir=/etc               \
                        --with-vendor="Pisi Linux"         \
                        --with-lang="%s"     \
                        --enable-qt5         \
                        --enable-gtk3   \
                        --disable-gtk    \
                        --with-help            \
                        --with-myspell-dicts  \
                        --with-java                     \
                        --without-system-dicts          \
                        --without-fonts    \
                        --disable-postgresql-sdbc       \
                        --disable-firebird-sdbc     \
                        --disable-coinmp \
                        --without-system-hsqldb \
                        --enable-release-build=yes      \
                        --enable-python=system          \
                        --with-system-apr           \
                        --without-system-boost             \
                        --with-system-cairo             \
                        --with-system-clucene   \
                        --with-system-cppunit \
                        --with-system-curl              \
                        --with-system-expat             \
                        --with-system-graphite      \
                        --with-system-glm \
                        --with-system-harfbuzz          \
                        --with-system-hunspell \
                        --with-system-icu               \
                        --with-system-jpeg              \
                        --with-jdk-home=/usr/lib/jvm/java \
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
                        --with-jdk-home=/usr/lib/jvm/java-8-openjdk \
                        --with-external-tar=external/tarballs \
                        --with-gdrive-client-id=457862564325.apps.googleusercontent.com \
                        --with-gdrive-client-secret=GYWrDtzyZQZ0_g5YoBCC6F0I \
                        --with-parallelism=%s' % (langall, get.makeJOBS().replace("-j","")))
#--disable-fetch-external \

def build():
    autotools.make("build-nocheck")

def install():
    autotools.rawInstall("DESTDIR=%s distro-pack-install" % get.installDIR())
    
    # cleanup gid_Module
    pisitools.remove("gid_Module*")
    
    # add application descriptions    
    pisitools.insinto("/usr/share/appdata/", "sysui/desktop/appstream-appdata/libreoffice-*.xml")
    
    # put configuration files into place
    pisitools.dosym("/usr/lib/libreoffice/program/bootstraprc", "/etc/libreoffice/bootstraprc")
    pisitools.dosym("/usr/lib/libreoffice/program/sofficerc", "/etc/libreoffice/sofficerc")
    pisitools.dosym("/usr/lib/libreoffice/share/psprint/psprint.conf", "/etc/libreoffice/psprint.conf")
    
    # make pyuno find its modules
    pisitools.dosym("/usr/lib/libreoffice/program/uno.py", "/usr/lib/python3.6/site-packages/uno.py")
    pisitools.dosym("/usr/lib/libreoffice/program/unohelper.py", "/usr/lib/python3.6/site-packages/unohelper.py")
    
    for pix in ["libreoffice-base.png", "libreoffice-calc.png", "libreoffice-draw.png", "libreoffice-impress.png", "libreoffice-main.png", "libreoffice-math.png", "libreoffice-startcenter.png", "libreoffice-writer.png"]:
        pisitools.dosym("/usr/share/icons/hicolor/32x32/apps/%s" % pix, "/usr/share/pixmaps/%s" %pix)
