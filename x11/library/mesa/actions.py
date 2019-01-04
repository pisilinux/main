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

    shelltools.system("sed -i 's|python2|python|g' \
                       meson.build \
                       src/meson.build")
    shelltools.system("sed -i 's|prog_python2|prog_python|g' \
                       src/util/xmlpool/meson.build \
                       src/util/meson.build \
                       src/mapi/glapi/gen/meson.build \
                       src/mapi/shared-glapi/meson.build \
                       src/mapi/es1api/meson.build \
                       src/mapi/es2api/meson.build \
                       src/compiler/meson.build \
                       src/compiler/spirv/meson.build \
                       src/compiler/nir/meson.build \
                       src/compiler/glsl/meson.build \
                       src/vulkan/util/meson.build \
                       src/amd/common/meson.build \
                       src/amd/vulkan/meson.build \
                       src/intel/genxml/meson.build \
                       src/intel/isl/meson.build \
                       src/intel/compiler/meson.build \
                       src/intel/vulkan/meson.build \
                       src/mesa/main/meson.build \
                       src/mesa/meson.build \
                       src/mesa/drivers/dri/i965/meson.build \
                       src/egl/meson.build \
                       src/gallium/auxiliary/meson.build \
                       src/gallium/drivers/r600/meson.build \
                       src/gallium/drivers/radeonsi/meson.build") 

    shelltools.makedirs("build")
    shelltools.cd("build")
    options = "meson --prefix=/usr \
                     --sysconfdir=/etc \
                     --buildtype=release \
                     -Ddri-drivers-path=lib/xorg/modules/dri \
                     -Db_ndebug=true \
                     -Dplatforms=x11,wayland,drm,surfaceless \
                     -Ddri3=true \
                     -Ddri-drivers=i915,i965,r100,r200,nouveau \
                     -Dgallium-drivers=r300,r600,nouveau,radeonsi,svga,swrast,virgl \
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
                     -Dtexture-float=true \
                     -Dosmesa=gallium \
                     -Dlmsensors=false \
                     -Dswr-arches=avx,avx2"
                     


    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
        shelltools.export("LLVM_CONFIG","/usr/bin/llvm-config-32")        
        options += " --prefix=/usr --libdir=lib32 \
                     -Ddri-drivers-path=lib32/xorg/modules/dri \
                     -Dclang-libdir-path=/usr/lib32 \
                     -Dgallium-opencl=disabled"

    elif get.ARCH() == "x86_64":
        options += " -Dclang-libdir-path=/usr/lib \
                     -Dgallium-omx=bellagio \
                     -Dgallium-opencl=disabled .."

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
    
