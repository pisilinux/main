#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools


def build():
    shelltools.system("""sed -e "s|\('https://docs\.readthedocs\.io/en/latest/', \)None|\1'%{SOURCE1}'|" \
                           -e "s|\('http://www\.sphinx-doc\.org/en/stable/', \)None|\1'%{_docdir}/python-sphinx-doc/html/objects.inv'|" \
                           -i docs/conf.py""")


    shelltools.system("mkdir -p build/lib/sphinx_rtd_theme/static/js")
    shelltools.system("cp -p sphinx_rtd_theme/static/js/badge_only.js build/lib/sphinx_rtd_theme/static/js")
    shelltools.system("cp -p sphinx_rtd_theme/static/js/theme.js build/lib/sphinx_rtd_theme/static/js")

    shelltools.system("""sed -i "/'build_py'/d" setup.py""")

    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
