#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.util import join_path
from pisi.actionsapi import shelltools

BASE_DIR = 'arc-themes/%s'
ARC_DIR = BASE_DIR % 'Arc'
ARC_SOLID_DIR = BASE_DIR % 'Arc-Solid'
ARC_DARK_DIR = BASE_DIR % 'Arc-Dark'
ARC_DARK_SOLID_DIR = BASE_DIR % 'Arc-Dark-Solid'


def install():
    pisitools.dodir("/usr/share/themes/Arc")
    pisitools.dodir("/usr/share/themes/Arc-Solid")
    pisitools.dodir("/usr/share/themes/Arc-Dark")
    pisitools.dodir("/usr/share/themes/Arc-Dark-Solid")

    for sub_theme in ["gtk-2.0", "gtk-3.0", "metacity-1", "xfwm4", "cinnamon", "gnome-shell", "unity"]:
        pisitools.insinto("/usr/share/themes/Arc", join_path(ARC_DIR, sub_theme))
        pisitools.insinto("/usr/share/themes/Arc-Solid", join_path(ARC_SOLID_DIR, sub_theme))
        pisitools.insinto("/usr/share/themes/Arc-Dark", join_path(ARC_DARK_DIR, sub_theme))
        pisitools.insinto("/usr/share/themes/Arc-Dark-Solid", join_path(ARC_DARK_SOLID_DIR, sub_theme))
