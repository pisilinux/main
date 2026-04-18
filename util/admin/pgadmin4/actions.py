#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    installdir = get.installDIR()
    shelltools.system("pip3 install --no-build-isolation --ignore-installed "
                      "--prefix=/usr --root='%s' "
                      "-r requirements.txt" % installdir)
    os.environ["COREPACK_ENABLE_STRICT"] = "0"
    os.environ["COREPACK_ENABLE_AUTO_PIN"] = "0"
    os.environ["COREPACK_HOME"] = "/root/.cache/node/corepack"
    os.environ["YARN_IGNORE_NODE"] = "1"
    shelltools.system("corepack enable")
    shelltools.system("corepack prepare yarn@4.9.2 --activate")
    shelltools.system("cd web && yarn install && yarn run bundle")

def build():
    pass

def install():
    installdir = get.installDIR()

    # Ana dizinleri oluştur
    pisitools.dodir("/usr/lib/pgadmin4")
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/var/lib/pgadmin")
    pisitools.dodir("/var/log/pgadmin")
    pisitools.dodir("/usr/share/applications")

    # Dosyaları kopyala
    shelltools.copytree("web", "%s/usr/lib/pgadmin4/web" % installdir)
    shelltools.copytree("docs", "%s/usr/lib/pgadmin4/docs" % installdir)

    # Launcher script
    launcher = "#!/bin/sh\nexec python3 /usr/lib/pgadmin4/web/pgAdmin4.py \"$@\"\n"
    open("%s/usr/bin/pgadmin4" % installdir, "w").write(launcher)
    shelltools.chmod("%s/usr/bin/pgadmin4" % installdir, 0o755)

    # Desktop entry
    desktop = "[Desktop Entry]\nName=pgAdmin 4\nComment=PostgreSQL management tool\nExec=pgadmin4\nIcon=pgadmin4\nTerminal=false\nType=Application\nCategories=Development;Database;\n"
    open("%s/usr/share/applications/pgadmin4.desktop" % installdir, "w").write(desktop)
