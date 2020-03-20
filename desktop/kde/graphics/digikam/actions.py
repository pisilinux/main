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
    kde5.configure("-DBUILD_TESTING=OFF \
                    -DENABLE_KFILEMETADATASUPPORT=ON \
                    -DENABLE_MEDIAPLAYER=ON \
                    -DENABLE_AKONADICONTACTSUPPORT=ON \
                    -DENABLE_MYSQLSUPPORT=ON \
                    -DENABLE_APPSTYLES=ON \
                    -DENABLE_QWEBENGINE=ON \
                    -DOpenGL_GL_PREFERENCE=GLVND")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("COPYING", "COPYING-CMAKE-SCRIPTS", "README*", "NEWS")
    
