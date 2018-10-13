#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's/lib64/lib/g' cmake/flann_utils.cmake")
    shelltools.system("sed -i '1 i #undef _GLIBCXX_ATOMIC_BUILTINS' src/cpp/flann/algorithms/kdtree_cuda_3d_index.cu")
    shelltools.system("sed -i '1 i #undef _GLIBCXX_USE_INT128' src/cpp/flann/algorithms/kdtree_cuda_3d_index.cu")

    shelltools.system("sed -i 's|#!/usr/bin/env python|#!/usr/bin/python2|' \
                              bin/download_checkmd5.py \
                              bin/run_test.py \
                              src/python/setup.py.tpl \
                              test/test_clustering.py \
                              test/test_index_save.py \
                              test/test_nn_autotune.py \
                              test/test_nn_index.py \
                              test/test_nn.py")
    shelltools.system('sed -i "s|setup\.py install|setup.py install --root=$pkgdir --optimize=1|" src/python/CMakeLists.txt')
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DBUILD_MATLAB_BINDINGS=OFF \
                          -DBUILD_PYTHON_BINDINGS=ON \
                          -DPYTHON_EXECUTABLE=/usr/bin/python2.7 \
                          -DNVCC_COMPILER_BINDIR=/usr/bin")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dosym("libinput.so.5.0.0","/usr/lib/libinput.so.0")
    
    #pisitools.dodoc("COPYING", "README")
