#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

pisitools.cxxflags.add("-std=gnu++11")

ver = get.srcVERSION()

def setup():
    
    loader_opts = "-DCMAKE_INSTALL_SYSCONFDIR=/etc \
                   -DCMAKE_INSTALL_DATADIR=/share \
                   -DCMAKE_SKIP_RPATH=True \
                   -DBUILD_TESTS=OFF \
                   -DBUILD_WSI_XCB_SUPPORT=On \
                   -DBUILD_WSI_XLIB_SUPPORT=On \
                   -DBUILD_WSI_WAYLAND_SUPPORT=On \
                   -DBUILD_SHARED_LIBS=ON \
                   -DVULKAN_HEADERS_INSTALL_DIR='/usr' \
                 "
    validation_opts = " -DCMAKE_INSTALL_SYSCONFDIR=/etc \
                        -DCMAKE_INSTALL_DATADIR=/share \
                        -DCMAKE_SKIP_RPATH=True \
                        -DCMAKE_INSTALL_INCLUDEDIR='/usr/include' \
                        -DBUILD_TESTS=OFF \
                        -DBUILD_WSI_XCB_SUPPORT=On \
                        -DBUILD_WSI_XLIB_SUPPORT=On \
                        -DBUILD_WSI_WAYLAND_SUPPORT=On \
                        -DBUILD_SHARED_LIBS=ON \
                        -DBUILD_LAYER_SUPPORT_FILES=ON \
                        -DSPIRV_TOOLS_INSTALL_DIR='/usr' \
                        -DUSE_ROBIN_HOOD_HASHING=OFF \
                        -DGLSLANG_INSTALL_DIR=/usr \
                      "
                      
    if get.buildTYPE() == "_emul32":
        shelltools.export("ASFLAGS", "--32")
        shelltools.export("CFLAGS", "-m32")
        shelltools.export("CXXFLAGS", "-m32")
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        
        shelltools.cd("%s/Vulkan-Loader-%s" %(get.workDIR(), ver))
        shelltools.makedirs("build")
        shelltools.cd("build")
        
        loader_opts += "-DCMAKE_INSTALL_LIBDIR=lib32 \
                        -DCMAKE_ASM_FLAGS='--32' \
                       "
                       
        cmaketools.configure(loader_opts, sourceDir="..")
        
        shelltools.cd("%s/Vulkan-ValidationLayers-%s" %(get.workDIR(), ver))
        shelltools.makedirs("build")
        shelltools.cd("build")
        #shelltools.system("../scripts/update_deps.py")
        validation_opts += "-DCMAKE_INSTALL_LIBDIR=lib32 \
                            -DSPIRV_TOOLS_LIB='/usr/lib32' \
                            -DSPIRV_TOOLS_OPT_LIB='/usr/lib32' \
                            -DCMAKE_ASM_FLAGS='--32' \
                           "
                           
        cmaketools.configure(validation_opts, sourceDir="..")
        
    else:
        shelltools.cd("%s/Vulkan-Loader-%s" %(get.workDIR(), ver))
        shelltools.makedirs("build")
        shelltools.cd("build")
        
        loader_opts += "-DCMAKE_INSTALL_LIBDIR=lib \
                        -DSPIRV_HEADERS_INSTALL_DIR='/usr/include/spirv' \
                       "
                       
        cmaketools.configure(loader_opts, sourceDir="..")
        
        shelltools.cd("%s/Vulkan-ValidationLayers-%s" %(get.workDIR(), ver))
        shelltools.makedirs("build")
        shelltools.cd("build")
        #shelltools.system("../scripts/update_deps.py")
        
        validation_opts += "-DCMAKE_INSTALL_LIBDIR=lib \
                            -DSPIRV_TOOLS_LIB='/usr/lib' \
                            -DSPIRV_HEADERS_INSTALL_DIR='/usr/include/spirv' \
                            -DSPIRV_TOOLS_OPT_LIB='/usr/lib' \
                           "
                           
        cmaketools.configure(validation_opts, sourceDir="..")
        
def build():
    shelltools.cd("%s/Vulkan-Loader-%s" %(get.workDIR(), ver))
    shelltools.cd("build")
    cmaketools.make("-j1")
    
    shelltools.cd("%s/Vulkan-ValidationLayers-%s" %(get.workDIR(), ver))
    shelltools.cd("build")
    cmaketools.make("-j1")
    
def install():
    
    shelltools.cd("%s/Vulkan-Loader-%s" %(get.workDIR(), ver))
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" %get.installDIR())
    
    shelltools.cd("%s/Vulkan-ValidationLayers-%s" %(get.workDIR(), ver))
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" %get.installDIR())  
    
    #pisitools.dodoc("README.md", "COPYRIGHT.txt", "LICENSE.txt")
