#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5

def install():
    pisitools.dosed("src/mainwindow.py", "Kde3", "Kde5")
    pythonmodules.install()

    # Copy Notification Rc file for Kde
    pisitools.insinto("%s/package-manager/" % kde5.appsdir, "src/package-manager.notifyrc")

    for lang in ('de','en','es','fr','nl','sv','tr'):
        pisitools.insinto("%s/html/%s/package-manager/" % (kde5.docdir, lang),
                          "help/%s/main_help.html" % lang, "index.html")

