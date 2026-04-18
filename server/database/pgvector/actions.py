#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# pgvector builds as a standard PostgreSQL PGXS extension.
# PG_CONFIG is auto-detected via PATH; USE_PGXS=1 tells the
# Makefile to build against the installed PostgreSQL rather than
# the PostgreSQL source tree.

def build():
    autotools.make("USE_PGXS=1 OPTFLAGS=\"\"")

def install():
    autotools.rawInstall("USE_PGXS=1 DESTDIR=%s OPTFLAGS=\"\"" % get.installDIR())
