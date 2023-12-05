#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file `http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get


def setup():
    shelltools.system("rm -rf CMakeCache.txt")
    shelltools.cd("..")
    shelltools.makedirs("cmake-make")
    shelltools.cd("cmake-make") 
    shelltools.system("cmake ../blender-%s \
                      -DCMAKE_INSTALL_PREFIX=/usr \
                      -DFREETYPE_INCLUDE_DIRS=/usr/include/freetype2 \
                      -DCMAKE_BUILD_TYPE=Release \
                      -DCMAKE_SKIP_RPATH=ON \
                      -DWITH_JACK=ON \
                      -DUSD_ROOT_DIR=/usr \
                      -DLLVM_VERSION=16 \
                      -DWITH_JACK_DYNLOAD=ON \
                      -DWITH_IMAGE_OPENEXR=ON \
                      -DWITH_OPENCOLORIO=ON \
                      -DWITH_OPENIMAGEIO=ON \
                      -DWITH_OPENIMAGEDENOISE=ON \
                      -DWITH_FFTW3=ON\
                      -DWITH_PLAYER=ON \
                      -DWITH_CODEC_FFMPEG=ON \
                      -DWITH_INSTALL_PORTABLE=OFF \
                      -DWITH_GAMEENGINE=ON \
                      -DWITH_PYTHON_INSTALL=OFF \
                      -DWITH_MOD_OCEANSIM=ON \
                      -DPYTHON_VERSION=3.11 \
                      -DPYTHON_LIBPATH=/usr/lib \
                      -DPYTHON_LIBRARY=python3.11 \
                      -DPYTHON_INCLUDE_DIRS=/usr/include/python3.11 \
                      -DPYTHON_NUMPY_INCLUDE_DIRS=/usr/lib/python3.11/site-packages/numpy/core/include \
                      -DWITH_CYCLES_EMBREE=OFF \
                      -DWITH_CODEC_SNDFILE=ON " % get.srcVERSION())

def build():
    shelltools.cd("../cmake-make")
    cmaketools.make()

def install():
    shelltools.cd("../cmake-make/")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/bin/blender", "/usr/bin", "blender-bin")

