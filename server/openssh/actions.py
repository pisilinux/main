#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "openssh-%s" % get.srcVERSION().replace("_","")

def setup():
    shelltools.export("CFLAGS","%s -fpie" % get.CFLAGS())
    shelltools.export("LDFLAGS","%s -pie" % get.LDFLAGS())

    #pisitools.dosed("pathnames.h", "/usr/X11R6/bin/xauth", r"/usr/bin/xauth")
    pisitools.dosed("sshd_config", "(?m)^(^#UsePAM ).*", r"UsePAM yes")
    pisitools.dosed("sshd_config", "(?m)^(^#PasswordAuthentication ).*", r"PasswordAuthentication no")
    pisitools.dosed("sshd_config", "(?m)^(^#X11Forwarding ).*", r"X11Forwarding yes")
    pisitools.dosed("sshd_config", "(?m)^(^#UseDNS ).*", r"UseDNS no")
    pisitools.dosed("sshd_config", "(?m)^(^#PermitRootLogin ).*", r"PermitRootLogin no")

    autotools.autoreconf("-fi")

    # Kerberos support is a must, libedit is optional
    # Update configure parameters when both are ready
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc/ssh \
                         --datadir=/usr/share/sshd \
                         --with-pam \
                         --with-libedit \
                         --with-kerberos5 \
                         --with-md5-passwords \
                         --with-ipaddr-display \
                         --with-privsep-user=sshd \
                         --with-privsep-path=/var/empty \
                         --with-default-path=/usr/bin \
                         --without-zlib-version-check \
                         --with-superuser-path=/sbin:/bin:/usr/sbin:/usr/bin \
                         --with-pid-dir=/run")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # PAM configuration
    pisitools.dodir("/etc/pam.d")
    shelltools.system("sed 's@d/login@d/sshd@g' /etc/pam.d/login > " + get.installDIR() + "/etc/pam.d/sshd")
    shelltools.system("chmod 644 " + get.installDIR() + "/etc/pam.d/sshd")

    # fixes #10992
    pisitools.dobin("contrib/ssh-copy-id")
    pisitools.doman("contrib/ssh-copy-id.1")

    # an script in contrib
    pisitools.dobin("contrib/findssl.sh")

    shelltools.chmod("%s/etc/ssh/sshd_config" % get.installDIR(), 0600)
    # special request by merensan
    shelltools.echo("%s/etc/ssh/ssh_config" % get.installDIR(), "ServerAliveInterval 5")

    pisitools.dodoc("ChangeLog", "CREDITS", "OVERVIEW", "README*", "TODO", "sshd_config")
