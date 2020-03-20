#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
import os
from pisi.actionsapi import autotools


def build():
    autotools.make('-C lib PREFIX=/usr')
    autotools.make('-C programs PREFIX=/usr lz4 lz4c')


def install():
    autotools.rawInstall('PREFIX=/usr DESTDIR=%s' % os.environ.pop('INSTALL_DIR'))
