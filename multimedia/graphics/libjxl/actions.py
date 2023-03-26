#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, pisitools, get

i = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DBUILD_TESTING=false',
    ' -DBUILD_SHARED_LIBS=true',
    ' -DJPEGXL_FORCE_SYSTEM_LCMS2=true',
    ' -DJPEGXL_FORCE_SYSTEM_HWY=true',
    ' -DJPEGXL_FORCE_SYSTEM_GTEST=true',
    ' -DJPEGXL_FORCE_SYSTEM_BROTLI=true',
    ' -DJPEGXL_ENABLE_SKCMS=false',
    ' -DJPEGXL_ENABLE_SJPEG=false',
    ' -DJPEGXL_ENABLE_BENCHMARK=false',
    ' -DJPEGXL_ENABLE_EXAMPLES=false',
    ' -DJPEGXL_ENABLE_FUZZERS=false',
    ' -B_build -Wno-dev -L '
    ])

def setup():
	cmaketools.configure(i)

def build():
	# fix incorrect g++ options //not required for gcc12
	# shelltools.system("find . -iname 'link.txt' -exec sed -i 's: -R: -Wl,-R:g' {} \;")
	cmaketools.make("-C _build")

def install():
	cmaketools.install("-C _build")

	pisitools.dodoc("AUTHORS", "CHANGELOG.md")
