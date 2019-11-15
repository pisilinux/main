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
indir = "%s/VulkanTools-%s" % (get.workDIR(), ver)

def setup():
	shelltools.system("./update_external_sources.sh")
	shelltools.system("scripts/update_deps.py")
	shelltools.system("mkdir -p build")
	shelltools.cd("build")
	
	shelltools.system("cmake .. \
		               -DCMAKE_INSTALL_PREFIX=/usr \
		               -DCMAKE_INSTALL_SYSCONFDIR=/etc \
		               -DCMAKE_INSTALL_DATADIR=/usr/share \
		               -DCMAKE_INSTALL_LIBDIR=lib \
		               -DCMAKE_SKIP_RPATH=True \
		               -DBUILD_WSI_XCB_SUPPORT=On \
		               -DBUILD_WSI_XLIB_SUPPORT=On \
		               -DBUILD_WSI_WAYLAND_SUPPORT=On \
		               -DBUILD_TESTS=OFF \
		               -DBUILD_VIA=OFF \
		               -DCMAKE_BUILD_TYPE=Release \
		               -DVULKAN_HEADERS_INSTALL_DIR=%s/Vulkan-Headers/build/install \
		               -DVULKAN_LOADER_INSTALL_DIR=%s/Vulkan-Loader/build/install  \
		               -DVULKAN_VALIDATIONLAYERS_INSTALL_DIR=%s/Vulkan-ValidationLayers/build/install \
		               " % (indir, indir, indir ) )
	
  

def build():
	shelltools.cd("build")
	cmaketools.make()
    

def install():
	shelltools.cd("build")
	autotools.rawInstall("DESTDIR=%s" %get.installDIR()) 
	shelltools.cd("..")
	pisitools.insinto("/usr/share/doc/vulkan-trace", "vktrace/LICENSE")
	pisitools.insinto("/usr/share/doc/vulkan-extra-layers", "CONTRIBUTING.md")
	pisitools.insinto("/usr/share/doc/vulkan-extra-layers", "GOVERNANCE.md")
	pisitools.insinto("/usr/share/doc/vulkan-extra-layers", "LICENSE.txt")
	pisitools.insinto("/usr/share/doc/vulkan-extra-layers", "README.md")
	pisitools.insinto("/usr/share/doc/vulkan-extra-layers", "layersvt/README.md", "README.layersvt")

    
	#pisitools.dodoc("README.md", "CONTRIBUTING.md", "LICENSE.txt", "CODE_OF_CONDUCT.md", "GOVERNANCE.md")
