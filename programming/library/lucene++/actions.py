#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = "-DCMAKE_BUILD_TYPE=Release \
     -DCMAKE_INSTALL_PREFIX=/usr \
     -DLIB_DESTINATION=/usr/lib \
     -DBUILD_SHARED_LIBS=ON \
     -DENABLE_TEST=OFF \
	 -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
	 -DCMAKE_CXX_FLAGS='-std=c++20 -DBOOST_VARIANT_USE_RELAXED_GET_BY_DEFAULT' \
     -DENABLE_DEMO=OFF \
    "

def setup():
	shelltools.system("""sed -i \
    -e 's#SET(LUCENE++_VERSION_REVISION.*#SET(LUCENE++_VERSION_REVISION "5")#' \
    -e 's#SET(LUCENE++_VERSION_PATCH.*#SET(LUCENE++_VERSION_PATCH "0")#' \
    CMakeLists.txt""")
	shelltools.export("CXXFLAGS", "-DBOOST_VARIANT_USE_RELAXED_GET_BY_DEFAULT")
	shelltools.export("CXXFLAGS", "-lpthread")
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure("%s" % i, sourceDir='..')

def build():
	shelltools.cd("build")
	cmaketools.make("CMAKE_POLICY_VERSION_MINIMUM=3.5")

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("../AUTHORS", "../COPYING", "../README.md")

