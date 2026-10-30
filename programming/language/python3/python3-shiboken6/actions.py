#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
import os
import subprocess

def setup():
    # Kaynak dizinine gir
    # if shelltools.can_access_file("pyside-setup"):
        # shelltools.cd("pyside-setup")
    # elif shelltools.can_access_file("pyside-setup-6.11.3"):
        # shelltools.cd("pyside-setup-6.11.3")

    # pkg-config çıktısını al
    try:
        pkgconf_libs = subprocess.check_output(["pkg-config", "python3-embed", "--libs"]).decode('utf-8').strip()
    except Exception:
        pkgconf_libs = os.popen("pkg-config python3-embed --libs").read().strip()

    if not pkgconf_libs:
        pkgconf_libs = "-lpython3.14"

    # NumPy include dizinini al
    try:
        numpy_inc = subprocess.check_output(["numpy-config", "--cflags"]).decode('utf-8').replace("-I", "").strip()
    except Exception:
        numpy_inc = ""

    # CMake'i ayrı bir build dizini ile çalıştır
    shelltools.system("cmake -B build -S . -G Ninja \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE=None \
        -DSHIBOKEN_PYTHON_LIBRARIES='%s' \
        -DBUILD_TESTS=OFF \
        -DFORCE_LIMITED_API=no \
        -DNO_QT_TOOLS=yes \
        -DNUMPY_INCLUDE_DIR='%s'" % (pkgconf_libs, numpy_inc))


def build():
    # Ninja ile derle
    shelltools.system("PYTHONPATH=\"$PWD/build/sources\" ninja -C build")


def install():
    # Mevcut çalışma dizinini kaydet
    # (Pisi genellikle work/ dizinindedir)

    # 1. shiboken6 kütüphanesini kur (zaten başarılı)
    shelltools.system("DESTDIR=%s cmake --install build/sources/shiboken6" % get.installDIR())

    # shiboken6 egg-info (Eğer gerekliyse, dizin yolunu kontrol edin)
    # shelltools.cd("pyside-setup-everywhere-src-6.11.2")  # Doğru dizin adı bu olabilir
    # shelltools.system("PATH=/usr/lib/qt6/bin:$PATH python3 setup.py egg_info --build-type=shiboken6")
    # pythonpath = os.popen("python3 -c \"from sysconfig import get_path; print(get_path('platlib'))\"").read().strip()
    # shelltools.system("cp -r shiboken6.egg-info %s%s" % (get.installDIR(), pythonpath))

    # 2. shiboken6_generator'ı kur
    shelltools.system("DESTDIR=%s cmake --install build/sources/shiboken6_generator" % get.installDIR())

    # 3. pyside6'yı kur
    shelltools.system("DESTDIR=%s cmake --install build/sources/pyside6" % get.installDIR())

    # 4. pyside6-tools'u kur
    shelltools.system("DESTDIR=%s cmake --install build/sources/pyside-tools" % get.installDIR())

    # Lisans ve dokümantasyon
    # shelltools.cd("..")
    pisitools.dodoc("LICENSES/*", "README*")
