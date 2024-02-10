#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("CMakeLists.txt", "ECMFeatureSummary", deleteLine=True)
    pisitools.dosed("CMakeLists.txt", "ecm_feature_summary", "feature_summary")
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("README.md")
