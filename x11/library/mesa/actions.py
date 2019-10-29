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
    #autotools.autoreconf("-vif")

# --enable-sysfs option provides better hardware information support with "lspci"
# --enable-32-bit option is not present anymore. Although build fails in emul32. With --disable-asm option, not fail. Needs to be tested.


    shelltools.makedirs("build")
    shelltools.cd("build")
    options = "meson --prefix=/usr \
                     --sysconfdir=/etc \
                     --buildtype=release \
                     -Ddri-drivers-path=/usr/lib/xorg/modules/dri \
                     -Db_ndebug=true \
                     -Dplatforms=x11,wayland,drm,surfaceless \
                     -Ddri3=true \
                     -Ddri-drivers=i915,i965,r100,r200,nouveau \
                     -Dgallium-drivers=r300,r600,nouveau,radeonsi,svga,swrast,swr,virgl,iris \
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
                     -Dglvnd=false \
                     -Dasm=true \
                     -Dllvm=true \
                     -Dvalgrind=false \
                     -Dlibunwind=true \
                     -Dbuild-tests=false \
                     -Dosmesa=gallium \
                     -Dlmsensors=false \
                     -Dswr-arches=avx,avx2"
                     


    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
        shelltools.export("LLVM_CONFIG","/usr/bin/llvm-config-32")        
        options += " --libdir=lib32 \
                     -Ddri-drivers-path=/usr/lib32/xorg/modules/dri \
                     -Dclang-libdir-path=/usr/lib32 \
                     -Dgallium-opencl=disabled"

    elif get.ARCH() == "x86_64":
        options += " -Dclang-libdir-path=/usr/lib \
                     -Dgallium-omx=bellagio \
                     -Dgallium-opencl=icd .."

    shelltools.system(options)
    #pisitools.dosed("libtool","( -shared )", " -Wl,--as-needed\\1")

def build():
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    pisitools.domove("%s/libGL.so.1.2.0" % Libdir, "%s/mesa" % Libdir)
    pisitools.dosym("libGL.so.1.2.0", "%s/libGL.so.1.2" % Libdir)

    if get.buildTYPE() == "emul32":
        #pisitools.remove("/usr/lib32/pkgconfig/wayland-egl.pc")
        #pisitools.remove("/usr/lib32/libwayland-egl.so*")
        return
    
    shelltools.cd("..")

    #pisitools.dodoc("docs/COPYING")
    pisitools.dohtml("docs/*")
    
    #pisitools.remove("/usr/lib/libwayland-egl.so*")
    #pisitools.remove("/usr/lib/pkgconfig/wayland-egl.pc")
    
