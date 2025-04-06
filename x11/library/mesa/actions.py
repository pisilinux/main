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
               -Ddri-drivers-path=%s/xorg/modules/dri \
               -Db_ndebug=true \
               -Dplatforms=x11,wayland \
               -Dgallium-extra-hud=true \
               -Dgallium-vdpau=enabled \
               -Dgallium-va=enabled \
               -Dgallium-xa=enabled \
               -Dgallium-nine=true \
               -Dvulkan-layers=device-select,intel-nullhw,overlay \
               -Dvideo-codecs=all \
               -Dshared-glapi=enabled \
               -Dgles1=enabled \
               -Dgles2=enabled \
               -Dopengl=true \
               -Dgbm=enabled \
               -Dglx=dri \
               -Degl=enabled \
               -Dglvnd=enabled \
               -Dllvm=enabled \
               -Dvalgrind=enabled \
               -Dlibunwind=disabled \
               -Dbuild-tests=false \
               -Dosmesa=true \
              " % (libdir)

    if get.buildTYPE() == "emul32":
        # shelltools.export("LDFLAGS", "%s -L/usr/lib32"  % get.LDFLAGS())
        # shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        options += " -Dlmsensors=disabled --native-file crossfile.ini -Dzstd=disabled \
                     -Dvulkan-drivers=amd,intel,intel_hasvk,swrast,virtio \
                     -Dgallium-drivers=r300,r600,nouveau,radeonsi,svga,iris,llvmpipe,softpipe,virgl,crocus,i915,zink \
                   "
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
        options += " -Dgallium-opencl=icd -Dlmsensors=enabled -Dzstd=enabled \
                             -Dgallium-rusticl=true \
                             -Drust_std=2021 \
                             -Dvulkan-layers=screenshot,vram-report-limit \
                             -Dvulkan-drivers=amd,gfxstream,intel,intel_hasvk,nouveau,swrast,virtio,microsoft-experimental \
                             -Dgallium-drivers=r300,r600,nouveau,radeonsi,svga,iris,llvmpipe,softpipe,virgl,crocus,i915,zink,d3d12"
    
    #pisitools.ldflags.add("-fuse-ld=lld")
    mesontools.configure(options)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.insinto("/usr/share/pixmaps", "docs/favicon.svg", "mesa.svg")

    pisitools.dohtml("docs/*")
