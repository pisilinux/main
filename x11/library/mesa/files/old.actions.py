# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


Libdir = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"

def setup():
    autotools.autoreconf("-vif")

# --enable-sysfs option provides better hardware information support with "lspci"
# --enable-32-bit option is not present anymore. Although build fails in emul32. With --disable-asm option, not fail. Needs to be tested.

    options ="\
              --with-dri-driverdir=/usr/lib/xorg/modules/dri \
              --with-gallium-drivers=r300,r600,radeonsi,nouveau,svga,swrast,virgl \
              --with-dri-drivers=i915,i965,r200,radeon,nouveau,swrast \
              --with-platforms=x11,drm,wayland \
              --enable-xa \
              --enable-dri \
              --enable-egl \
              --enable-gbm \
              --enable-glx \
              --enable-dri3 \
              --enable-gles1 \
              --enable-gles2 \
              --enable-vdpau \
              --enable-osmesa \
              --enable-xvmc \
              --enable-glx-tls \
              --enable-llvm \
              --enable-nine \
              --enable-libunwind \
              --enable-llvm-shared-libs \
              --enable-shared-glapi \
              --enable-texture-float \
            "

    if get.buildTYPE() == "emul32":
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
        shelltools.export("LLVM_CONFIG","/usr/bin/llvm-config-32")        
        options += " --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
                            --with-clang-libdir=/usr/lib32 \
                            --disable-asm "

    elif get.ARCH() == "x86_64":
        options += " --with-clang-libdir=/usr/lib \
                            --enable-omx-bellagio \
                            --enable-opencl-icd "

    autotools.configure(options)
    pisitools.dosed("libtool","( -shared )", " -Wl,--as-needed\\1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("%s/libGL.so.1.2.0" % Libdir, "%s/mesa" % Libdir)
    pisitools.dosym("libGL.so.1.2.0", "%s/libGL.so.1.2" % Libdir)

    if get.buildTYPE() == "emul32":
        #pisitools.remove("/usr/lib32/pkgconfig/wayland-egl.pc")
        #pisitools.remove("/usr/lib32/libwayland-egl.so*")
        return

    #pisitools.dodoc("docs/COPYING")
    pisitools.dohtml("docs/*")
    
    #pisitools.remove("/usr/lib/libwayland-egl.so*")
    #pisitools.remove("/usr/lib/pkgconfig/wayland-egl.pc")
    
