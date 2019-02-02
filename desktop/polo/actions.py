#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("LC_ALL", "en_US.UTF-8")
    shelltools.system("sed -i 's|term.feed_child(cmd, -1);|term.feed_child(cmd.to_utf8());|g' src/Gtk/TermBox.vala")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "LICENSE*", "COPYING", "README*")
