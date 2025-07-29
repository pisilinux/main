
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

i = "-Dprocacpi=enabled \
     -Dsysfsacpi=enabled \
     -Dlibsensors=enabled \
     -Dlibnotify=enabled \
    "

def setup():
    mesontools.configure(i)


def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")

