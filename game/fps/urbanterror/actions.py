#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#
# For ioquake sources svn://svn.icculus.org/quake3/trunk
# For bunch of updates http://www.www0.org/urt/
#
# Tarball is created with ioquake revision 1807, copying files of
# http://www.www0.org/urt/ioq3-1807-urt-251210-git.tar.lzma
# and applying ioq3-1807-urt-251210-git.patch in ioq3
#

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "-"))
arch = get.ARCH().replace("i686", "i386")

builddir = "build/release-linux-%s" % arch
datadir = "/usr/share/urbanterror"

cflags = "%s -I/usr/include/freetype2" % get.CFLAGS()

WorkDir = "ioq3-for-UrbanTerror-4-release-%s" % get.srcVERSION()

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    for i in ["code/SDL12", "code/libs/win32"]:
        if shelltools.isDirectory(i):
            shelltools.unlinkDir(i)

def build():
    autotools.make('CC="%s" \
                    ARCH="%s" \
                    OPTIMIZE="%s" \
                    DEFAULT_BASEDIR="%s" \
                    BUILD_SERVER=1 \
                    BUILD_CLIENT_SMP=1 \
                    USE_SDL=1 \
                    BUILD_CLIENT=1 \
                    USE_OPENAL=1 \
                    USE_CURL=1 \
                    USE_CODEC_VORBIS=1 \
                    USE_VOIP=1 \
                    USE_INTERNAL_SPEEX=0 \
                    USE_INTERNAL_ZLIB=0 \
                    USE_LOCAL_HEADERS=0 \
                    release' % (get.CC(), arch, cflags, datadir))
                    #BUILD_GAME_QVM=0 \


def install():
    pisitools.dobin("%s/Quake3-UrT.%s" % (builddir, arch))
    pisitools.dobin("%s/Quake3-UrT-smp.%s" % (builddir, arch))
    pisitools.dobin("%s/Quake3-UrT-Ded.%s" % (builddir, arch))

    pisitools.rename("/usr/bin/Quake3-UrT.%s" % arch, "urbanterror")
    pisitools.rename("/usr/bin/Quake3-UrT-smp.%s" % arch, "urbanterror-smp")
    pisitools.rename("/usr/bin/Quake3-UrT-Ded.%s" % arch, "urbanterror-server")
    
    pisitools.dodoc("ChangeLog", "*.txt", "README")

    shelltools.cd("UrbanTerror43/q3ut4")
    for files in ["*.pk3", "*.cfg", "mapcycle_example.txt"]:
        pisitools.insinto("%s/baseut4" %datadir, files)
    pisitools.dodoc("readme43.txt")
    

    

