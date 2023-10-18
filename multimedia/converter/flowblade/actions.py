#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def build():
    shelltools.system("sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/python3|g' flowblade-trunk/Flowblade/launch/*")
    shelltools.system("sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/python3|g' flowblade-trunk/Flowblade/tools/clapperless.py")
    shelltools.cd("flowblade-trunk")
    pythonmodules.compile(pyVer="3")

def install():
    shelltools.cd("flowblade-trunk")
    pythonmodules.install(pyVer="3")

    shelltools.chmod(get.installDIR() + "/usr/lib/python3.11/site-packages/Flowblade/launch/*")
    shelltools.chmod(get.installDIR() + "/usr/lib/python3.11/site-packages/Flowblade/tools/clapperless.py")

    pisitools.dodoc("AUTHORS", "COPYING", "README*")
