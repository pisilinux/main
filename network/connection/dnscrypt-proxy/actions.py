#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.cd("dnscrypt-proxy")
    shelltools.system("""go build -ldflags "-compressdwarf=false -linkmode external" .""")

def install():
    # Main executable
    pisitools.dobin("dnscrypt-proxy/dnscrypt-proxy")

    # Base configuration
    pisitools.dodir("/etc/dnscrypt-proxy")
    pisitools.insinto("/etc/dnscrypt-proxy", "dnscrypt-proxy/example-dnscrypt-proxy.toml", "dnscrypt-proxy.toml")
    pisitools.insinto("/etc/dnscrypt-proxy", "dnscrypt-proxy/example-allowed-ips.txt", "allowed-ips.txt")
    pisitools.insinto("/etc/dnscrypt-proxy", "dnscrypt-proxy/example-allowed-names.txt", "allowed-names.txt")
    pisitools.insinto("/etc/dnscrypt-proxy", "dnscrypt-proxy/example-blocked-ips.txt", "blocked-ips.txt")
    pisitools.insinto("/etc/dnscrypt-proxy", "dnscrypt-proxy/example-blocked-names.txt", "blocked-names.txt")
    pisitools.insinto("/etc/dnscrypt-proxy", "dnscrypt-proxy/example-captive-portals.txt", "captive-portals.txt")
    pisitools.insinto("/etc/dnscrypt-proxy", "dnscrypt-proxy/example-cloaking-rules.txt", "cloaking-rules.txt")
    pisitools.insinto("/etc/dnscrypt-proxy", "dnscrypt-proxy/example-forwarding-rules.txt", "forwarding-rules.txt")

    # generate-domains-blocklist
    pisitools.dodir("/usr/share/dnscrypt-proxy/utils/generate-domains-blocklist")
    pisitools.insinto("/usr/share/dnscrypt-proxy/utils/generate-domains-blocklist", "utils/generate-domains-blocklist/*.conf")
    pisitools.insinto("/usr/share/dnscrypt-proxy/utils/generate-domains-blocklist", "utils/generate-domains-blocklist/*.txt")
    pisitools.dobin("utils/generate-domains-blocklist/generate-domains-blocklist.py")

    # Documentation
    pisitools.dodoc("ChangeLog", "README*", "LICENSE*")
