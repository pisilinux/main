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
               -Dplatforms=x11,wayland \
               -Ddri3=enabled \
               -Ddri-drivers=i915,i965,r100,r200,nouveau \
               -Dgallium-drivers=r300,r600,nouveau,radeonsi,svga,swr,iris,swrast,virgl,crocus,zink \
               -Dgallium-extra-hud=true \
               -Dgallium-vdpau=enabled \
               -Dgallium-xvmc=enabled \
               -Dgallium-va=enabled \
               -Dgallium-xa=enabled \
               -Dgallium-nine=true \
               -Dvulkan-drivers=amd,intel \
               -D vulkan-layers=device-select,intel-nullhw,overlay \
               -Dshared-glapi=enabled \
               -Dgles1=enabled \
               -Dgles2=enabled \
               -Dopengl=true \
               -Dgbm=enabled \
               -Dglx=dri \
               -Degl=enabled \
               -Dglvnd=true \
               -Dasm=true \
               -Dllvm=enabled \
               -Dvalgrind=enabled \
               -Dlibunwind=enabled \
               -Dbuild-tests=false \
               -Dosmesa=true \
               -Dswr-arches=avx,avx2 \
               -Dgallium-opencl=icd \
              " % ((libdir, ) * 2)

    if get.buildTYPE() == "emul32":
        options += " -Dlmsensors=disabled --native-file crossfile.ini -Dllvm_libdir=/usr/lib32 -Dzstd=disabled"
        #shelltools.export("CC", "clang -m32")
        #shelltools.export("CXX", "clang++ -m32")
        pisitools.cflags.add("-m32 ")
        pisitools.cxxflags.add("-m32")
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
        shelltools.export("LLVM_CONFIG","/usr/bin/llvm-config-32") 
    else:
        #shelltools.export("CC", "clang")
        #shelltools.export("CXX", "clang++")
        pisitools.cflags.add("-m64 ")
        pisitools.cxxflags.add("-m64")
        options += " -Dgallium-omx=bellagio -Dlmsensors=enabled -Dzstd=enabled"
    
    #pisitools.ldflags.add("-fuse-ld=lld")
    mesontools.configure(options)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dohtml("docs/*")
