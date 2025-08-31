#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    shelltools.system("./install -P %s/usr" % get.installDIR())

    # Use the following command in Distrobox repo to regenerate:
    # echo -n 'pisitools.dodoc('; find docs -name '*.md' | sed 's/^/"/; s/$/",/' | tr '\n' ' ' | sed 's/, $//'; echo ')'
    pisitools.dodoc("docs/README.md", "docs/assets/credits.md", "docs/compatibility.md", "docs/usage/distrobox-rm.md", "docs/usage/distrobox-list.md", "docs/usage/distrobox-ephemeral.md", "docs/usage/distrobox-generate-entry.md", "docs/usage/distrobox-init.md", "docs/usage/distrobox-host-exec.md", "docs/usage/distrobox-enter.md", "docs/usage/distrobox-create.md", "docs/usage/distrobox-assemble.md", "docs/usage/distrobox-export.md", "docs/usage/usage.md", "docs/usage/distrobox-stop.md", "docs/usage/distrobox-upgrade.md", "docs/posts/run_libvirt_in_distrobox.md", "docs/posts/posts.md", "docs/posts/install_podman_static.md", "docs/posts/steamdeck_guide.md", "docs/posts/install_lilipod_static.md", "docs/posts/integrate_vscode_distrobox.md", "docs/posts/execute_commands_on_host.md", "docs/posts/run_latest_gnome_kde_on_distrobox.md", "docs/posts/distrobox_custom.md", "docs/404.md", "docs/useful_tips.md", "docs/featured_articles.md")

