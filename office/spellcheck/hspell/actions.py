#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

def setup():
	autotools.configure("--enable-shared --enable-linginfo --enable-fatverb")

def build():
	autotools.make("PERL_USE_UNSAFE_INC=1 hunspell")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.insinto("/usr/share/hunspell", "he.aff", "he_IL.aff")
	pisitools.insinto("/usr/share/hunspell", "he.dic", "he_IL.dic")
