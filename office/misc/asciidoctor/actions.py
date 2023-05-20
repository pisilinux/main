#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


_rubyver="3.2.0"

def build():
    shelltools.system("gem build asciidoctor.gemspec")

def install():
    shelltools.system("gem install  --ignore-dependencies --no-user-install -V -i %s/usr/lib/ruby/gems/%s/ -n %s/usr/bin asciidoctor-%s.gem" % (get.installDIR(), _rubyver, get.installDIR(), get.srcVERSION()))

    pisitools.domove("/usr/lib/ruby/gems/%s/gems/asciidoctor-%s/man/asciidoctor.1" %(_rubyver, get.srcVERSION() ), "/usr/share/man/man1/")
    pisitools.removeDir("/usr/lib/ruby/gems/%s/gems/asciidoctor-%s/man" % (_rubyver, get.srcVERSION()))
    pisitools.remove("/usr/lib/ruby/gems/%s/cache/asciidoctor-%s.gem" % (_rubyver, get.srcVERSION()))
    # pisitools.doman("man/asciidoctor.1")

    pisitools.dodoc("LICENSE", "README*")
