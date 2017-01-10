# main
packages for Pisi-2.0 library, desktops, programming, supported with team

Dear Developers,

Sevgili Geliştiriciler,

Please be carefull following issues;

Lütfen aşağıdaki konularda dikkatli olalım;

There is no systemd in our project that is why we use "--with-systemdsystemunitdir=no" instead of "--with-systemdsystemunitdir=/lib/systemd/system" when we are configure a package.

Bizde systemd olmadığı için paketleri yapılandırırken "--with-systemdsystemunitdir=/lib/systemd/system" yerine "--with-systemdsystemunitdir=no" kullanıyoruz.

When we are configure a package if we use "--libexecdir=", we use it as "--libexecdir=/usr/lib"

Bir paketi yapılandırırken "--libexecdir=" kullanılacaksa "--libexecdir=/usr/lib" böyle olacak.



------------------------------------------------------------------------------------------------------------------------------------------------------------------

[![Throughput Graph](https://graphs.waffle.io/pisilinux/main/throughput.svg)](https://waffle.io/pisilinux/main/metrics)
