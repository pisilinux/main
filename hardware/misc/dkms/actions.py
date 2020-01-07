#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dosbin("dkms")
    pisitools.doman("dkms.8")
    pisitools.insinto("/usr/share/bash-completion/completions", "dkms.bash-completion", "dkms")
    pisitools.insinto("/etc/dkms", "dkms_framework.conf", "framework.conf")
    pisitools.insinto("/var/lib/dkms", "dkms_dbversion")

    pisitools.dodoc("AUTHORS", "COPYING", "README*", "TODO")
