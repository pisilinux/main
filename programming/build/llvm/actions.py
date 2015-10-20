
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pkgconfig
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools

#WorkDir = "%s-%s.src" % (get.srcNAME(), get.srcVERSION())
libdir = "/usr/lib32/llvm" if get.buildTYPE() == "emul32" else "/usr/lib/llvm"
lib = "lib32" if get.buildTYPE() == "emul32" else "lib"

def setup():    
    if not shelltools.isDirectory("tools/clang"):
        #pisitools.dosed("tools/cfe-3.7.0.src/lib/Driver/ToolChains.cpp", '"ld"', '"ld.gold"')
        shelltools.move("tools/cfe-%s.src" % get.srcVERSION(), "tools/clang")
        shelltools.move("tools/clang-tools-extra-*", "tools/clang/extra")
        shelltools.move("tools/lldb-*", "tools/lldb")
    if not shelltools.isDirectory("projects/compiler-rt"):
        shelltools.move("projects/compiler-rt-3.7*", "projects/compiler-rt")
    
    #pic_option = "enable" if get.ARCH() == "x86_64" else "disable"
    shelltools.export("CC", "gcc")
    shelltools.export("CXX", "g++")

    shelltools.system("patch -d tools/clang/extra -Np1 < clang-tools-extra-3.7.0-install-clang-query.patch")
    
    shelltools.system("patch -d tools/lldb -Np1 < lldb-3.7.0-avoid-linking-to-libLLVM.patch")

    shelltools.makedirs("build")
    
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DLLVM_BUILD_LLVM_DYLIB=ON \
                          -DLLVM_DYLIB_EXPORT_ALL=ON \
                          -DLLVM_LINK_LLVM_DYLIB=ON \
                          -DLLVM_ENABLE_RTTI=ON \
                          -DLLVM_ENABLE_FFI=ON \
                          -DLLVM_BUILD_DOCS=OFF \
                          -DLLVM_ENABLE_SPHINX=OFF \
                          -DLLVM_ENABLE_DOXYGEN=OFF \
                          -DFFI_INCLUDE_DIR=/usr/lib/libffi-3.2.1/include \
                          -DLLVM_BINUTILS_INCDIR=/usr/include", sourceDir="..")
def build():
    shelltools.makedirs("build")
    
    shelltools.cd("build")
    
    cmaketools.make()

def install():
    shelltools.makedirs("build")
    
    shelltools.cd("build")
    
    if get.buildTYPE() == "emul32":
 
        #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
        cmaketools.rawInstall("DESTDIR=%s \
                              PROJ_etcdir=/etc/llvm \
                              PROJ_libdir=/usr/lib32/llvm \
                              PROJ_docsdir=/%s/llvm"
                              % (get.installDIR(),  get.docDIR()))
        shelltools.chmod("%s/usr/lib32/llvm/*.a" % get.installDIR(), mode = 0644)
        pisitools.dosym("llvm/LLVMgold.so", "/usr/lib32/LLVMgold.so")
        pisitools.remove("/usr/lib32/llvm/*LLVMHello.*")
        return
    else:
        cmaketools.rawInstall("DESTDIR=%s \
                              PROJ_etcdir=/etc/llvm \
                              PROJ_libdir=%s \
                              PROJ_docsdir=/%s/llvm"
                              % (get.installDIR(), libdir, get.docDIR()))


    #shelltools.chmod("%s/usr/lib/llvm/*.a" % get.installDIR(), 0644)

    # Install static analyzers which aren't installed by default
    for exe in ("scan-build", "scan-view"):
        pisitools.insinto("/usr/lib/clang-analyzer/%s" % exe, "tools/clang/tools/%s/%s" % (exe, exe))
        pisitools.dosym("/usr/lib/clang-analyzer/%s/%s" % (exe, exe), "/usr/bin/%s" % exe)

    # Symlink the gold plugin where clang expects it
    pisitools.dosym("llvm/LLVMgold.so", "/usr/lib/LLVMgold.so")

    # Remove example file
    pisitools.remove("/usr/lib/llvm/*LLVMHello.*")

    pisitools.remove("/usr/share/doc/llvm/*.tar.gz")
    pisitools.remove("/usr/share/doc/llvm/ocamldoc/html/*.tar.gz")
    pisitools.removeDir("/usr/share/doc/llvm/ps")

    # Install vim syntax files for .ll and .td files
    # llvm.vim additional file add ftdetct vim file to detect .ll and .td as llvm files
    pisitools.insinto("/usr/share/vim/vimfiles/syntax", "utils/vim/*.vim")

    # Install kate syntax file
    #pisitools.insinto("%s/katepart/syntax" % kde4.appsdir, "utils/kate/*.xml")

    pisitools.dodoc("CREDITS.TXT", "LICENSE.TXT", "README.txt")
