#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, cmaketools, pisitools

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=None',
    ' -DENABLE_EXAMPLES=ON',
    ' -DENABLE_{MILTER,SYSTEMD}=OFF',
    ' -DAPP_CONFIG_DIRECTORY=/etc/clamav',
    ' -DDATABASE_DIRECTORY=/var/lib/clamav',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    cmaketools.configure(j)

def build():
    mesontools.build()

def check():
    mesontools.build("test")
    # pass

def install():
    mesontools.install()

    pisitools.dodir("/var/lib/clamav")

    for t in ["clamd.conf.sample", "freshclam.conf.sample"]:
        pisitools.rename("/etc/clamav/%s" % t, t.replace(".sample", ""))
