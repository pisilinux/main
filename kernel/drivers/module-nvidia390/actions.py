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
    shelltools.system("sh NVIDIA-Linux-%s-%s.run -x --target tmp"
                      % (arch, get.srcVERSION()))
    shelltools.move("tmp/*", ".")
    
    
    #if get.buildTYPE() != 'emul32':
		#shelltools.system("patch -p1 < linux-5.1.patch")
    
    
    # Our libc is TLS enabled so use TLS library
    #shelltools.unlink("*-tls.so*")
    #shelltools.move("tls/*", ".")

    # xorg-server provides libwfb.so
    shelltools.unlink("libnvidia-wfb.so.*")

    shelltools.echo("ld.so.conf", nvlibdir)
    shelltools.echo("XvMCConfig", "%s/libXvMCNVIDIA.so" % nvlibdir)

def build():
    # We don't need kernel module for emul32 build
    if get.buildTYPE() == 'emul32':
        return

    shelltools.export("SYSSRC", "/lib/modules/%s/build" % KDIR)
    shelltools.cd("kernel")

    autotools.make("module")
    
    #shelltools.cd("uvm")
    #autotools.make("module")

def install():

    if not get.buildTYPE() == 'emul32':
        # Kernel driver
        pisitools.insinto("/lib/modules/%s/extra" % KDIR,
                          "kernel/nvidia.ko")
        
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

    ###  Libraries
    # OpenGl library
    pisitools.dolib("libGL.so.%s" % version, nvlibdir)
    pisitools.dosym("libGL.so.%s" % version, "%s/libGL.so.1.2.0" % nvlibdir)
    pisitools.dosym("libGL.so.%s" % version, "%s/libGL.so.1" % nvlibdir)
    pisitools.dolib("libGL.so.%s" % version, libdir)
    
    pisitools.dolib("libEGL.so.1.1.0", nvlibdir)
    pisitools.dosym("libEGL.so.1.1.0", "%s/libEGL.so.1" % nvlibdir)
    pisitools.dolib("libEGL_nvidia.so.%s" % version, libdir)
    pisitools.dolib("libGLESv1_CM_nvidia.so.%s" % version, libdir)
    pisitools.dolib("libGLESv2_nvidia.so.%s" % version, libdir)

    # OpenCL
    pisitools.insinto("/etc/OpenCL/vendors", "nvidia.icd")
    pisitools.dolib("libnvidia-compiler.so.%s" % version, libdir)
    pisitools.dosym("libnvidia-compiler.so.%s" % version, "%s/libnvidia-compiler.so.1" % libdir)
    
    pisitools.dolib("libOpenCL.so.1.0.0", libdir)
    pisitools.dosym("libOpenCL.so.1.0.0", "%s/libOpenCL.so.1.0" % libdir)
    pisitools.dosym("libOpenCL.so.1.0", "%s/libOpenCL.so.1" % libdir)
    
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

    

    # OpenGL core library and others
    for lib in ("glcore", "tls", "encode", "fbc", "glsi", "ifr", "eglcore"):
        pisitools.dolib("libnvidia-%s.so.%s" % (lib, version), libdir)
        pisitools.dosym("libnvidia-%s.so.%s" % (lib, version), "%s/libnvidia-%s.so.1" %(libdir, lib))

    # VDPAU driver
    pisitools.dolib("libvdpau_nvidia.so.%s" % version, "%s/vdpau" % libdir)
    pisitools.dosym("libvdpau_nvidia.so.%s" % version, "%s/libvdpau_nvidia.so" % libdir)
    
    # nvidia-tls library
    pisitools.dolib("libnvidia-tls.so.%s" % version, libdir)
    pisitools.dolib("tls/libnvidia-tls.so.%s" % version, "%s/tls" % libdir)

    # X modules
    pisitools.dolib("nvidia_drv.so", "%s/modules/drivers" % xorglibdir)
    pisitools.dolib("libglx.so.%s" % version, "%s" % nvlibdir)
    pisitools.dosym("libglx.so.%s" % version, "%s/libglx.so.1" % nvlibdir)
    pisitools.dosym("libglx.so.%s" % version, "%s/libglx.so" % nvlibdir)
    pisitools.dolib("libglx.so.%s" % version, "%s/modules/extensions" % xorglibdir)
    pisitools.dosym("libglx.so.%s" % version, "%s/modules/extensions/libglx.so.1" % xorglibdir)
    
    pisitools.dolib("libGLX_nvidia.so.%s" % version, libdir)
    pisitools.dosym("libGLX_nvidia.so.%s" % version, "%s/libGLX_indirect.so.0" % libdir)
    
    # PTX JIT Compiler (Parallel Thread Execution (PTX) is a pseudo-assembly language for CUDA)
    pisitools.dolib("libnvidia-ptxjitcompiler.so.%s" % version, libdir)
    
    # Fat (multiarchitecture) binary loader
    pisitools.dolib("libnvidia-fatbinaryloader.so.%s" % version, libdir)
    
    pisitools.insinto("/usr/share/X11/xorg.conf.d", "nvidia-drm-outputclass.conf")
  #  pisitools.insinto("/usr/share/nvidia", "nvidia-application-profiles-367.27-rc")
   # pisitools.insinto("/usr/share/nvidia", "nvidia-application-profiles-367.27-key-documentation")
    #pisitools.insinto("/usr/share/pixmaps", "nvidia-settings.png")
    

    # Exit time for emul32 build
    if get.buildTYPE() == 'emul32':
        pisitools.insinto(datadir, "ld.so.conf", "32bit-ld.so.conf")
        return

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
