# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import shelltools

libdir = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"

def setup():
    options = "--buildtype=release \
               -Dclang-libdir-path=%s \
               -Ddri-drivers-path=%s/xorg/modules/dri \
               -Db_ndebug=true \
               -Dplatforms=x11,wayland,drm,surfaceless \
               -Ddri3=true \
               -Ddri-drivers=i915,i965,r100,r200,nouveau \
               -Dgallium-drivers=r300,r600,nouveau,radeonsi,svga,swr,iris,swrast,virgl \
               -Dgallium-extra-hud=true \
               -Dgallium-vdpau=true \
               -Dgallium-xvmc=true \
               -Dgallium-va=false \
               -Dgallium-xa=true \
               -Dgallium-nine=true \
               -Dvulkan-drivers=amd,intel \
               -Dshared-glapi=true \
               -Dgles1=true \
               -Dgles2=true \
               -Dopengl=true \
               -Dgbm=true \
               -Dglx=dri \
               -Degl=true \
               -Dglvnd=true \
               -Dasm=true \
               -Dllvm=true \
               -Dvalgrind=false \
               -Dlibunwind=true \
               -Dbuild-tests=false \
               -Dosmesa=gallium \
               -Dswr-arches=avx,avx2 \
              " % ((libdir, ) * 2)

    if get.buildTYPE() == "emul32":
        options += " -Dlmsensors=false"
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
        shelltools.export("LLVM_CONFIG","/usr/bin/llvm-config-32") 
    else: options += " -Dgallium-opencl=icd -Dgallium-omx=bellagio -Dlmsensors=true"

    mesontools.configure(options)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dohtml("docs/*")
