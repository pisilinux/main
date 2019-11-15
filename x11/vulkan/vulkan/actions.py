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
	if get.buildTYPE() == "_emul32":		
		shelltools.cd("%s/Vulkan-Loader-%s" %(get.workDIR(), ver))
		shelltools.export("ASFLAGS", "--32")
		shelltools.export("CFLAGS", "-m32")
		shelltools.export("CXXFLAGS", "-m32")
		shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
		cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib32 \
                            -DCMAKE_INSTALL_SYSCONFDIR=/etc \
                            -DCMAKE_INSTALL_DATADIR=/share \
                            -DCMAKE_SKIP_RPATH=True \
                            -DBUILD_TESTS=Off \
                            -DBUILD_WSI_XCB_SUPPORT=On \
                            -DBUILD_WSI_XLIB_SUPPORT=On \
                            -DBUILD_WSI_WAYLAND_SUPPORT=On \
                            -DBUILD_SHARED_LIBS=ON \
                            -DVULKAN_HEADERS_INSTALL_DIR='/usr/include' \
                            -DCMAKE_ASM_FLAGS='--32' \
                          ")		
		shelltools.cd("%s/Vulkan-ValidationLayers-%s" %(get.workDIR(), ver))
		shelltools.system("scripts/update_deps.py")
		cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib32 \
                            -DCMAKE_INSTALL_SYSCONFDIR=/etc \
                            -DCMAKE_INSTALL_DATADIR=/share \
                            -DCMAKE_SKIP_RPATH=True \
                            -DCMAKE_INSTALL_INCLUDEDIR='/usr/include/vulkan/' \
                            -DBUILD_TESTS=Off \
                            -DBUILD_WSI_XCB_SUPPORT=On \
                            -DBUILD_WSI_XLIB_SUPPORT=On \
                            -DBUILD_WSI_WAYLAND_SUPPORT=On \
                            -DBUILD_SHARED_LIBS=ON \
                            -DVULKAN_HEADERS_INSTALL_DIR='/usr/include' \
                            -DBUILD_LAYER_SUPPORT_FILES=ON \
                            -DGLSLANG_INSTALL_DIR=glslang/build/install \
                            -DCMAKE_ASM_FLAGS='--32' \
                            ")
	
	else:		
		shelltools.cd("%s/Vulkan-Loader-%s" %(get.workDIR(), ver))		
		cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
                            -DCMAKE_INSTALL_SYSCONFDIR=/etc \
                            -DCMAKE_INSTALL_DATADIR=/share \
                            -DCMAKE_SKIP_RPATH=True \
                            -DBUILD_TESTS=Off \
                            -DBUILD_WSI_XCB_SUPPORT=On \
                            -DBUILD_WSI_XLIB_SUPPORT=On \
                            -DBUILD_WSI_WAYLAND_SUPPORT=On \
                            -DBUILD_SHARED_LIBS=ON \
                            -DVULKAN_HEADERS_INSTALL_DIR='/usr/include' \
                          ")
		
		shelltools.cd("%s/Vulkan-ValidationLayers-%s" %(get.workDIR(), ver))
		shelltools.system("scripts/update_deps.py")
		cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
                            -DCMAKE_INSTALL_SYSCONFDIR=/etc \
                            -DCMAKE_INSTALL_DATADIR=/share \
                            -DCMAKE_SKIP_RPATH=True \
                            -DCMAKE_INSTALL_INCLUDEDIR='/usr/include/vulkan/' \
                            -DBUILD_TESTS=Off \
                            -DBUILD_WSI_XCB_SUPPORT=On \
                            -DBUILD_WSI_XLIB_SUPPORT=On \
                            -DBUILD_WSI_WAYLAND_SUPPORT=On \
                            -DBUILD_SHARED_LIBS=ON \
                            -DVULKAN_HEADERS_INSTALL_DIR='/usr/include' \
                            -DBUILD_LAYER_SUPPORT_FILES=ON \
                            -DGLSLANG_INSTALL_DIR=glslang/build/install \
                          ")
    

def build():
	if get.buildTYPE() == "emul32":
		shelltools.cd("%s/Vulkan-Loader-%s" %(get.workDIR(), ver))
		cmaketools.make()
		
		shelltools.cd("%s/Vulkan-ValidationLayers-%s" %(get.workDIR(), ver))
		cmaketools.make()
	else:
		shelltools.cd("%s/Vulkan-Loader-%s" %(get.workDIR(), ver))
		cmaketools.make()
		
		shelltools.cd("%s/Vulkan-ValidationLayers-%s" %(get.workDIR(), ver))
		cmaketools.make()
    

def install():
    if get.buildTYPE() == "emul32":
		shelltools.cd("%s/Vulkan-Loader-%s" %(get.workDIR(), ver))
		autotools.rawInstall("DESTDIR=%s" %get.installDIR())
		
		shelltools.cd("%s/Vulkan-ValidationLayers-%s" %(get.workDIR(), ver))
		autotools.rawInstall("DESTDIR=%s" %get.installDIR())      
    else:
		shelltools.cd("%s/Vulkan-Loader-%s" %(get.workDIR(), ver))
		autotools.rawInstall("DESTDIR=%s" %get.installDIR())
		
		shelltools.cd("%s/Vulkan-ValidationLayers-%s" %(get.workDIR(), ver))
		autotools.rawInstall("DESTDIR=%s" %get.installDIR())  

    
    #pisitools.dodoc("README.md", "COPYRIGHT.txt", "LICENSE.txt")
