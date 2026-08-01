from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure(
        "--prefix=/usr "
        "--enable-all"
    )

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
