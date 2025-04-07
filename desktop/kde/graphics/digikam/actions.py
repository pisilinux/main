#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde6
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools

#shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-G 'Ninja' \
                          -DBUILD_TESTING=OFF \
                          -DBUILD_WITH_QT6=ON \
                          -DENABLE_KFILEMETADATASUPPORT=ON \
                          -DENABLE_MEDIAPLAYER=ON \
                          -DENABLE_AKONADICONTACTSUPPORT=ON \
                          -DENABLE_MYSQLSUPPORT=ON \
                          -DENABLE_APPSTYLES=ON \
                          -DENABLE_QWEBENGINE=ON \
                          -DKDE_INSTALL_LIBDIR=lib \
                          -DOpenGL_GL_PREFERENCE=GLVND", sourceDir = '..')

def build():
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" %get.installDIR())
    
    shelltools.cd("..")
    pisitools.dodoc("COPYING*", "README*", "NEWS")
    
