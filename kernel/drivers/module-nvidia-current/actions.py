# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kerneltools

WorkDir = "."
KDIR = kerneltools.getKernelVersion()
NoStrip = ["/lib/modules"]

version = get.srcVERSION()
driver_dir_name = "nvidia-current"
datadir = "/usr/share/%s" % driver_dir_name
libdir = "/usr/lib32" if get.buildTYPE() == 'emul32' else "/usr/lib"
arch = "x86"  if get.buildTYPE() == 'emul32' else get.ARCH().replace("i6", "x")
nvlibdir = "%s/%s" % (libdir, driver_dir_name)
xorglibdir= "%s/xorg" % libdir

def setup():
    shelltools.system("sh NVIDIA-Linux-x86_64-%s.run -x --target tmp"
                      % get.srcVERSION())
    shelltools.move("tmp/*", ".")

    shelltools.echo("ld.so.conf", nvlibdir)
    shelltools.echo("XvMCConfig", "%s/libXvMCNVIDIA.so" % nvlibdir)
    
    shelltools.copytree("kernel", "kernel-dkms")
    shelltools.unlink("kernel-dkms/dkms.conf")
    pisitools.dosed("kernel-dkms/Makefile", "CC \?= cc", "CC = /usr/bin/cc")

def build():
    # We don't need kernel module for emul32 build
    if get.buildTYPE() == 'emul32':
        return

    shelltools.export("SYSSRC", "/lib/modules/%s/build" % KDIR)
    shelltools.cd("kernel")
    autotools.make("module")   
    

def install():

    if not get.buildTYPE() == 'emul32':
        # Kernel driver
        pisitools.insinto("/lib/modules/%s/extra" % KDIR,
                          "kernel/nvidia.ko")
        
        pisitools.insinto("/lib/modules/%s/extra" % KDIR,
                          "kernel/nvidia-drm.ko")
        
        pisitools.insinto("/lib/modules/%s/extra" % KDIR,
                          "kernel/nvidia-uvm.ko")
        
        pisitools.insinto("/lib/modules/%s/extra" % KDIR,
                          "kernel/nvidia-modeset.ko")

        # Command line tools and their man pages
        pisitools.dobin("nvidia-smi")
        pisitools.doman("nvidia-smi.1.gz")
        pisitools.dobin("nvidia-debugdump")
        pisitools.dobin("nvidia-xconfig")
        pisitools.doman("nvidia-xconfig.1.gz")
        pisitools.dobin("nvidia-bug-report.sh")
        pisitools.dobin("nvidia-cuda-mps-server")
        pisitools.dobin("nvidia-cuda-mps-control")
        pisitools.doman("nvidia-cuda-mps-control.1.gz")
        pisitools.dobin("nvidia-modprobe")
        pisitools.doman("nvidia-modprobe.1.gz")
        pisitools.dobin("nvidia-persistenced")
        pisitools.doman("nvidia-persistenced.1.gz")
        pisitools.dobin("nvidia-settings")
        pisitools.doman("nvidia-settings.1.gz")

        # dkms
        pisitools.insinto("/usr/src/nvidia-%s" % version, "kernel-dkms/*")

    ###  Libraries

    # 32-bit libraries
    if get.buildTYPE() == 'emul32':
        pisitools.dolib("32/libGL.so.1.7.0", nvlibdir)
#        pisitools.dosym("libGL.so.1.7.0", "%s/libGL.so.1.2.0" % nvlibdir)
        pisitools.dosym("libGL.so.1.7.0", "%s/libGL.so.1" % nvlibdir)
        pisitools.dosym("libGL.so.1.7.0", "%s/libGL.so" % nvlibdir)

        pisitools.dolib("32/libEGL.so.1.1.0", nvlibdir)
        #pisitools.dosym("%s/libEGL.so.1.1.0" % nvlibdir, "%s/libEGL.so.1.1.0" % libdir)
        #pisitools.dosym("%s/libEGL.so.1.1.0" % nvlibdir, "%s/libEGL.so.1.0.0" % nvlibdir)
        #pisitools.dosym("%s/libEGL.so.1.1.0" % nvlibdir, "%s/libEGL.so.1" % nvlibdir)
        #pisitools.dosym("%s/libEGL.so.1.1.0" % nvlibdir, "%s/libEGL.so" % nvlibdir)

        pisitools.dolib("32/libEGL_nvidia.so.%s" % version, libdir)
        pisitools.dosym("libEGL_nvidia.so.%s" % version, "%s/libEGL_nvidia.so.1" %libdir)
        pisitools.dosym("libEGL_nvidia.so.%s" % version, "%s/libEGL_nvidia.so" %libdir)

        pisitools.dolib("32/libGLESv1_CM_nvidia.so.%s" % version, libdir)
        pisitools.dolib("32/libGLESv2_nvidia.so.%s" % version, libdir)

        pisitools.dolib("32/libnvidia-compiler.so.%s" % version, libdir)
        pisitools.dosym("libnvidia-compiler.so.%s" % version, "%s/libnvidia-compiler.so.1" % libdir)
        pisitools.dosym("libnvidia-compiler.so.%s" % version, "%s/libnvidia-compiler.so" % libdir)

        #pisitools.dolib("32/libOpenCL.so.1.0.0", libdir)
        #pisitools.dosym("libOpenCL.so.1.0", "%s/libOpenCL.so.1" % libdir)
        #pisitools.dosym("libOpenCL.so.1.0", "%s/libOpenCL.so" % libdir)

        pisitools.dolib("32/libnvidia-opencl.so.%s" % version, libdir)
        pisitools.dosym("libnvidia-opencl.so.%s" % version, "%s/libnvidia-opencl.so.1" % libdir)
        pisitools.dosym("libnvidia-opencl.so.1", "%s/libnvidia-opencl.so" % libdir)

        pisitools.dolib("32/libcuda.so.%s" % version, libdir)
        pisitools.dosym("libcuda.so.%s" % version, "%s/libcuda.so.1" % libdir)
        pisitools.dosym("libcuda.so.1", "%s/libcuda.so" % libdir)

        pisitools.dolib("32/libnvcuvid.so.%s" % version, libdir)
        pisitools.dosym("libnvcuvid.so.%s" % version, "%s/libnvcuvid.so.1" % libdir)
        pisitools.dosym("libnvcuvid.so.1", "%s/libnvcuvid.so" % libdir)

        pisitools.dolib("32/libnvidia-ml.so.%s" % version, libdir)
        pisitools.dosym("libnvidia-ml.so.%s" % version, "%s/libnvidia-ml.so.1" % libdir)

        for lib in ("eglcore", "encode", "fatbinaryloader", "fbc", "glcore",  "glsi", \
                    "glvkspirv", "ifr", "opticalflow", "ptxjitcompiler", "tls", "allocator" ):
            pisitools.dolib("32/libnvidia-%s.so.%s" % (lib, version), libdir)
            pisitools.dosym("libnvidia-%s.so.%s" % (lib, version), "%s/libnvidia-%s.so.1" %(libdir, lib))
            pisitools.dosym("libnvidia-%s.so.%s" % (lib, version), "%s/libnvidia-%s.so" %(libdir, lib))

        pisitools.dolib("32/libvdpau_nvidia.so.%s" % version, "%s/vdpau" % libdir)
        pisitools.dosym("libvdpau_nvidia.so.%s" % version, "%s/libvdpau_nvidia.so" % libdir)

        pisitools.dolib("32/libGLX_nvidia.so.%s" % version, libdir)
        pisitools.dosym("libGLX_nvidia.so.%s" % version, "%s/libGLX_indirect.so.0" % libdir)
        pisitools.dosym("libGLX_nvidia.so.%s" % version, "%s/libGLX_indirect.so" % libdir)
        pisitools.dosym("libGLX_nvidia.so.%s" % version, "%s/libGLX_nvidia.so.0" % libdir)
        pisitools.dosym("libGLX_nvidia.so.%s" % version, "%s/libGLX_nvidia.so" % libdir)

        pisitools.dolib("32/libGLdispatch.so.0", libdir)
        pisitools.dosym("libGLdispatch.so.0", "%s/ibGLdispatch.so" % libdir)

        pisitools.dolib("32/libGLX.so.0", libdir)
        pisitools.dosym("libGLX.so.0", "%s/libGLX.so" % libdir)

        pisitools.dolib("32/libOpenGL.so.0", libdir)
        pisitools.dosym("libOpenGL.so.0", "%s/libOpenGL.so" % libdir)

    else:
        # OpenGl library
        pisitools.dolib("libGL.so.1.7.0", nvlibdir)
#        pisitools.dosym("libGL.so.1.7.0", "%s/libGL.so.1.2.0" % nvlibdir)
        pisitools.dosym("libGL.so.1.7.0", "%s/libGL.so.1" % nvlibdir)
        pisitools.dosym("libGL.so.1.7.0", "%s/libGL.so" % nvlibdir)

        pisitools.dolib("libEGL.so.1.1.0", nvlibdir)
        #pisitools.dosym("%s/libEGL.so.1.1.0" % nvlibdir, "%s/libEGL.so.1.1.0" % libdir)
        #pisitools.dosym("%s/libEGL.so.1.1.0" % nvlibdir, "%s/libEGL.so.1.0.0" % nvlibdir)
        #pisitools.dosym("%s/libEGL.so.1.1.0" % nvlibdir, "%s/libEGL.so.1" % nvlibdir)
        #pisitools.dosym("%s/libEGL.so.1.1.0" % nvlibdir, "%s/libEGL.so" % nvlibdir)
        pisitools.dolib("libEGL_nvidia.so.%s" % version, libdir)
        pisitools.dolib("libEGL.so.%s" % version, libdir)

        pisitools.dolib("libGLESv1_CM_nvidia.so.%s" % version, libdir)
        pisitools.dolib("libGLESv2_nvidia.so.%s" % version, libdir)

        # OpenCL
        pisitools.insinto("/etc/OpenCL/vendors", "nvidia.icd")
        pisitools.dolib("libnvidia-compiler.so.%s" % version, libdir)
        pisitools.dosym("libnvidia-compiler.so.%s" % version, "%s/libnvidia-compiler.so.1" % libdir)
        pisitools.dosym("libnvidia-compiler.so.%s" % version, "%s/libnvidia-compiler.so" % libdir)

        #pisitools.dolib("libOpenCL.so.1.0.0", libdir)
        #pisitools.dosym("libOpenCL.so.1.0.0", "%s/libOpenCL.so.1.0" % libdir)
        #pisitools.dosym("libOpenCL.so.1.0", "%s/libOpenCL.so.1" % libdir)
        #pisitools.dosym("libOpenCL.so.1.0", "%s/libOpenCL.so" % libdir)

        pisitools.dolib("libnvidia-opencl.so.%s" % version, libdir)
        pisitools.dosym("libnvidia-opencl.so.%s" % version, "%s/libnvidia-opencl.so.1" % libdir)
        pisitools.dosym("libnvidia-opencl.so.1", "%s/libnvidia-opencl.so" % libdir)

    # CUDA
        pisitools.dolib("libcuda.so.%s" % version, libdir)
        pisitools.dosym("libcuda.so.%s" % version, "%s/libcuda.so.1" % libdir)
        pisitools.dosym("libcuda.so.1", "%s/libcuda.so" % libdir)

        pisitools.dolib("libnvcuvid.so.%s" % version, libdir)
        pisitools.dosym("libnvcuvid.so.%s" % version, "%s/libnvcuvid.so.1" % libdir)
        pisitools.dosym("libnvcuvid.so.1", "%s/libnvcuvid.so" % libdir)

        # NVML
        # Provides programmatic access to static information and monitoring
        # data for NVIDIA GPUs, as well as limited managment capabilities
        pisitools.dolib("libnvidia-ml.so.%s" % version, libdir)
        pisitools.dosym("libnvidia-ml.so.%s" % version, "%s/libnvidia-ml.so.1" % libdir)

        pisitools.dolib("libnvidia-cfg.so.%s" % version, libdir)
        pisitools.dosym("libnvidia-cfg.so.%s" % version, "%s/libnvidia-cfg.so.1" % libdir)

        pisitools.dolib("libnvoptix.so.%s" % version, libdir)
        pisitools.dosym("libnvoptix.so.%s" % version, "%s/libnvoptix.so.1" % libdir)
        pisitools.dosym("libnvoptix.so.%s" % version, "%s/libnvoptix.so" % libdir)

        pisitools.dolib("libnvidia-egl-wayland.so.1.1.4", libdir)
        pisitools.dosym("libnvidia-egl-wayland.so.1.1.4", "%s/libnvidia-egl-wayland.so.1" % libdir)
        pisitools.dosym("libnvidia-egl-wayland.so.1.1.4", "%s/libnvidia-egl-wayland.so" % libdir)

        # OpenGL core library and others
        for lib in ("allocator", "cbl", "eglcore", "encode", "fatbinaryloader", "fbc", "glcore", "glsi", \
                    "glvkspirv", "ifr", "opticalflow", "ptxjitcompiler", "rtcore", "tls" ):
            pisitools.dolib("libnvidia-%s.so.%s" % (lib, version), libdir)
            pisitools.dosym("libnvidia-%s.so.%s" % (lib, version), "%s/libnvidia-%s.so.1" %(libdir, lib))
            pisitools.dosym("libnvidia-%s.so.%s" % (lib, version), "%s/libnvidia-%s.so" %(libdir, lib))

        # VDPAU driver
        pisitools.dolib("libvdpau_nvidia.so.%s" % version, "%s/vdpau" % libdir)
        pisitools.dosym("libvdpau_nvidia.so.%s" % version, "%s/libvdpau_nvidia.so" % libdir)    

        # X modules
        pisitools.dolib("nvidia_drv.so", "%s/modules/drivers" % xorglibdir)
        pisitools.dolib("libglxserver_nvidia.so.%s" % version, "%s/xorg/extensions" % nvlibdir)
        pisitools.dosym("libglxserver_nvidia.so.%s" % version, "%s/xorg/extensions/libglx.so.1" % nvlibdir)
        pisitools.dosym("libglxserver_nvidia.so.%s" % version, "%s/xorg/extensions/libglx.so" % nvlibdir)
        pisitools.dolib("libglxserver_nvidia.so.%s" % version, "%s/modules/extensions" % xorglibdir)
        pisitools.dosym("libglxserver_nvidia.so.%s" % version, "%s/modules/extensions/libglx.so.1" % xorglibdir)

        # Vulkan driver
        pisitools.dolib("libGLX_nvidia.so.%s" % version, libdir)
        pisitools.dosym("libGLX_nvidia.so.%s" % version, "%s/libGLX_indirect.so.0" % libdir)
        pisitools.dosym("libGLX_nvidia.so.%s" % version, "%s/libGLX_indirect.so" % libdir)
        pisitools.dosym("libGLX_nvidia.so.%s" % version, "%s/libGLX_nvidia.so.0" % libdir)
        pisitools.dosym("libGLX_nvidia.so.%s" % version, "%s/libGLX_nvidia.so" % libdir)
        pisitools.insinto("/etc/vulkan/icd.d", "nvidia_icd.json")
        pisitools.insinto("/etc/vulkan/icd.d", "nvidia_layers.json")

        pisitools.insinto("/usr/share/glvnd/egl_vendor.d", "10_nvidia.json")

        #pisitools.insinto("/usr/share/X11/xorg.conf.d", "nvidia-drm-outputclass.conf")
        #pisitools.insinto("/usr/share/nvidia", "nvidia-application-profiles-367.27-rc")
        #pisitools.insinto("/usr/share/nvidia", "nvidia-application-profiles-367.27-key-documentation")
        pisitools.insinto("/usr/share/pixmaps", "nvidia-settings.png")

        pisitools.dolib("libnvidia-gtk2.so.%s" % version, libdir)
        pisitools.dolib("libnvidia-gtk3.so.%s" % version, libdir)

    # Exit time for emul32 build
    #if get.buildTYPE() == 'emul32':
        #pisitools.insinto(datadir, "ld.so.conf", "32bit-ld.so.conf")
        #return

    pisitools.insinto(datadir, "ld.so.conf")
    pisitools.insinto(datadir, "XvMCConfig")

    # Documentation
    docdir = "xorg-video-%s" % driver_dir_name
    pisitools.dodoc("LICENSE", "NVIDIA_Changelog", "README.txt", destDir=docdir)
    pisitools.dohtml("html/*", destDir=docdir)

    ### Note
    # This package includes nvidia-setting and nvidia-xconfig binaries. However
    # we have seperate packages for each of them. Nvidia provides tarballs for
    # these binaries. Don't forget to update these package with each NVIDIA
    # driver update.
