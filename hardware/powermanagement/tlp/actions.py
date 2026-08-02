# -*- coding: utf-8 -*-
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          TLP_WITH_SYSTEMD=0 \
                          TLP_WITH_ELOGIND=0 \
                          TLP_NO_INIT=1 \
                          TLP_SBIN=/usr/sbin \
                          TLP_BIN=/usr/bin \
                          TLP_TLIB=/usr/share/tlp \
                          TLP_ULIB=/usr/lib/udev \
                          TLP_CONFUSR=/etc/tlp.conf \
                          TLP_CONFDIR=/etc/tlp.d \
                          TLP_MAN=/usr/share/man \
                          install install-man" % get.installDIR())

    pisitools.dodoc("LICENSE", "README.rst", "changelog")
    pisitools.removeDir("/usr/lib/systemd")
