#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools

#shelltools.export("HOME", get.workDIR())

def setup():
    kde5.configure("-DFORCED_UNBUNDLE=ON \
                    -DWITH_LQR=ON \
                    -DWITH_LENSFUN=ON \
                    -DWITH_MarbleWidget=ON \
                    -DENABLE_LCMS2=ON \
                    -DDIGIKAMSC_COMPILE_KIPIPLUGINS=ON \
                    -DDIGIKAMSC_USE_PRIVATE_SHAREDLIBS=ON \
                    -DDIGIKAMSC_COMPILE_LIBKGEOMAP=ON \
                    -DDIGIKAMSC_COMPILE_LIBKVKONTAKTE=ON \
                    -DDIGIKAMSC_COMPILE_LIBMEDIAWIKI=ON \
                    -DDIGIKAMSC_COMPILE_LIBKFACE=ON \
                    -DDIGIKAMSC_COMPILE_LIBKIPI=ON ")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("COPYING", "COPYING-CMAKE-SCRIPTS", "README*", "NEWS")
    
