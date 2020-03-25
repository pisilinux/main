#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # fixes build. so build uses python3 instead of python2
    pisitools.dosed("runtime/pgAdmin4.pro", "python-config", "python3-config")
    # fixes import error while sphinx builds documentation
    pisitools.dosed("web/pgadmin/browser/__init__.py", "_commit, default_render_json", "_commit, _render_json")
    
    shelltools.system(""" export PYTHONVERSION="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')" """)
    
    shelltools.system(""" sed -E "s|/usr/pgadmin4/web|/usr/lib/pgadmin4/web|g; \
          s|/usr/pgadmin4/lib/python[0-9\\.]+|/usr/lib/python${PYTHONVERSION}|g" \
         -i runtime/ConfigWindow.ui """)
    shelltools.system(""" sed "s|##PYTHONVERSION##|${PYTHONVERSION}|g" -i runtime/Server.cpp """)
	
    shelltools.system(" sed -E -i requirements.txt \
                        -e '/blinker>?=/d' \
                        -e '/extras>?=/d' \
                        -e '/Flask>?=/d' \
                        -e '/Flask-Login>?=/d' \
                        -e '/Flask-Migrate>?=/d' \
                        -e '/Flask-SQLAlchemy>?=/d' \
                        -e '/Flask-WTF>?=/d' \
                        -e '/pycrypto>?=/d' \
                        -e '/passlib>?=/d' \
                        -e '/pytz>?=/d' \
                        -e '/simplejson>?=/d' \
                        -e '/six>?=/d' \
                        -e '/speaklater>?=/d' \
                        -e '/sqlparse>?=/d' \
                        -e '/WTForms>?=/d' \
                        -e '/psutil>?=/d' \
                        -e '/psycopg2>?=/d' \
                        -e '/python-dateutil>?=/d' \
                        -e '/SQLAlchemy>?=/d' \
                        -e '/Flask-Gravatar>?=/d' \
                        -e '/Flask-Mail>?=/d' \
                        -e '/Flask-Principal>?=/d' \
                        -e '/Flask-Paranoid>?=/d' \
                        -e '/htmlmin>?=/d' \
                        -e '/Flask-Security>?=/d' \
                        -e '/Flask-HTMLmin>?=/d' \
                        -e '/Flask-Compress>?=/d' \
                        -e '/sshtunnel>?=/d' \
                        -e '/Werkzeug>?=/d' ")
    shelltools.system("cat requirements.txt")
    
    shelltools.export("LANG", "en_US.UTF-8")
    shelltools.export(" LC_ALL", "en_US.UTF-8")
    
    pisitools.dosed("docs/en_US/Makefile.sphinx", "PYTHON        = python", "PYTHON        = python3")
    
    shelltools.cd("runtime")
    shelltools.system("convert +set date:create +set date:modify pgAdmin4.ico pgAdmin4.png")
    
    shelltools.system("qmake CONFIG+=release")

def build():
    autotools.make("docs")
    shelltools.cd("runtime")
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/pgadmin4/runtime", "runtime/pgAdmin4")
    pisitools.insinto("/usr/lib/pgadmin4/web", "web/*")
    pisitools.insinto("/usr/lib/pgadmin4/docs", "docs*")
    pisitools.insinto("/usr/share/icons/hicolor/256x256/apps", "runtime/pgAdmin4-0.png", "pgAdmin4.png")
    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps", "runtime/pgAdmin4-1.png", "pgAdmin4.png")
    pisitools.insinto("/usr/share/icons/hicolor/32x32/apps", "runtime/pgAdmin4-2.png", "pgAdmin4.png")
    pisitools.insinto("/usr/share/icons/hicolor/16x16/apps", "runtime/pgAdmin4-3.png", "pgAdmin4.png")

    # add documentation
    pisitools.dohtml("docs/en_US/_build/*")

    if get.buildTYPE() != "_emul32":
        pisitools.dodoc("LICENSE", "README")
