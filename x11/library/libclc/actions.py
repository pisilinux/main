#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#
# libclc 23.1.4 - Arch Linux PKGBUILD'inden uyarlanmistir.
# LLVM 23'te libclc bagimsiz olarak, hedef basina ayri cmake
# cagrilariyla derlenir (Arch yontemi).
#

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "llvm-project-%s.src" % get.srcVERSION()

# LLVM 23'te libclc icin desteklenen hedef ucgenler
LIBCLC_TARGETS = [
    "spirv32-unknown-unknown",
    "spirv64-unknown-unknown",
    "amdgcn-amd-amdhsa",
    "nvptx64-nvidia-cuda",
]

# Host derleyici yolu (emul32'de clang32 kullanilir)
HOST_BIN = "/usr/bin"
libdir = "lib32" if get.buildTYPE() == "emul32" else "lib"

def _build_dir(target):
    return "build-libclc-%s" % target


def setup():
    pisitools.dosed("libclc/CMakeLists.txt", "{CMAKE_INSTALL_DATADIR}", "{CMAKE_INSTALL_LIBDIR}")
    # libclc dizinindeyiz; her hedef icin ayri cmake yapilandirmasi
    # setup asamasinda degil, build asamasinda yapilacak.
    pass


def build():
    # her hedef ucgen icin ayri cmake -S libclc -B build-libclc-<target>
    if get.buildTYPE() == "emul32":
        pisitools.cflags.add("-m32 ")
        pisitools.cxxflags.add("-m32")
        host_bin = "/usr/bin"
        cc = "%s/clang" % host_bin
        cxx = "%s/clang++" % host_bin
    else:
        pisitools.cflags.add("-m64 ")
        pisitools.cxxflags.add("-m64")
        host_bin = "/usr/bin"
        cc = "%s/clang" % host_bin
        cxx = "%s/clang++" % host_bin

    for target in LIBCLC_TARGETS:
        bdir = _build_dir(target)
        shelltools.system(
            "PATH=%s:$PATH cmake -S libclc -B %s "
            "-G Ninja "
            "-DCMAKE_BUILD_TYPE=Release "
            "-DCMAKE_INSTALL_PREFIX=/usr "
            "-DCMAKE_C_COMPILER=%s "
            "-DCMAKE_CXX_COMPILER=%s "
            "-DLLVM_DEFAULT_TARGET_TRIPLE=%s "
            "-DCMAKE_INSTALL_LIBDIR=%s"
            % (host_bin, bdir, cc, cxx, target, libdir)
        )
        shelltools.system(
            "PATH=%s:$PATH cmake --build %s" % (host_bin, bdir)
        )


def install():
    # Her hedefin build dizininden kurulum
    for target in LIBCLC_TARGETS:
        bdir = _build_dir(target)
        shelltools.system(
            "DESTDIR=%s cmake --install %s" % (get.installDIR(), bdir)
        )

    # Mesa'nin clover/rusticl icin bekledigi eski duz isimli dosyalar
    shelltools.system(
        "mkdir -p %s/usr/%s/clc" % (get.installDIR(), libdir
    ))
    shelltools.system(
        "ln -sf spirv32-unknown-unknown/libclc.spv "
        "%s/usr/%s/clc/spirv-mesa3d-.spv" % (get.installDIR(), libdir
    ))
    shelltools.system(
        "ln -sf spirv64-unknown-unknown/libclc.spv "
        "%s/usr/%s/clc/spirv64-mesa3d-.spv" % (get.installDIR(), libdir
    ))

    # Mesa icin pkg-config dosyasi (Python 2 ile dogrudan yaz)
    pc_content = (
        "prefix=/usr\n"
        "datarootdir=/usr/share\n"
        "datadir=/usr/%s\n"
        "pkgdatadir=${datadir}/clc\n"
        "libexecdir=${pkgdatadir}\n"
        "\n"
        "Name: libclc\n"
        "Description: Library requirements of the OpenCL C programming language\n"
        "Version: %s\n" % (libdir, get.srcVERSION()
    ))
    shelltools.system(
        "mkdir -p %s/usr/%s/pkgconfig" % (get.installDIR(), libdir)
    )
    pc_path = "%s/usr/%s/pkgconfig/libclc.pc" % (get.installDIR(), libdir)
    f = open(pc_path, "w")
    f.write(pc_content)
    f.close()

    pisitools.dodoc("LICENSE*", "README*")
