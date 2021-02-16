                        
[![Telegram](https://img.shields.io/badge/Telegram-Pisi%20GNU%2FLinux-blue)](https://t.me/joinchat/DnOmFNS_KOjzEpnn)
[![Forum](https://img.shields.io/badge/Forum-Pisi%20GNU%2FLinux-orange)](https://pisilinux.org/forum)
[![Website](https://img.shields.io/badge/Website-Pisi%20GNU%2FLinux-green)](https://pisilinux.org/)
*********************************************************************************
# DİKKAT: Geliştiriciler içindir, sisteminize zarar verebilir.
*********************************************************************************

# Pisi GNU/Linux

Pisi GNU/Linux; Pisi tabanlı son Pardus sürümünü temel alan, özgür yazılım topluluğu tarafından geliştirilen, bilgisayar kullanıcılarına kurulum, yapılandırma ve kullanım konusunda kolaylık sağlamaya çalışan, onların temel masaüstü gereksinimlerini karşılamayı amaçlayan, son kullanıcı odaklı bir GNU/Linux dağıtımıdır.

![](https://github.com/PisiLinuxNew/package-manager/blob/master/data/tray-zero.png)

************************************
Bu depo Pisi GNU/Linux projesinin *core* depo dışındaki tüm bileşenlerini içermektedir.
*************************************
Paketleme Kuralları;

1. pspec.xml ve actions.py dosyaları düzenlenirken *sekme* (Tab tuşu) yerine *boşluk* kullanılmalıdır

1. pspec.xml dosyalarında xml etiketlerinin hizalarına dikkat edilmelidir

1. Dosya yolları yazılırken bir yol diğer yolları kapsamamalıdır

1. actions.py dosyalarında mümkünse *shelltools* yerine *pisitools* kullanılmalı

1. *configure* seçeneklerinde pakete yeni bağımlılık getirecek değişiklikler için mutlaka issue açılmalı, tartışılmadan pull request istenmemelidir.

1. systemd olmadığı için paketleri yapılandırırken *"--with-systemdsystemunitdir=/lib/systemd/system"* yerine *"--with-systemdsystemunitdir=no"* kullanılmalıdır.

1. Bir paketi yapılandırırken *"--libexecdir="* kullanılacaksa *"--libexecdir=/usr/lib"* şeklinde kullanılmalıdır.

1. Tüm paketçiler kendi forklarında çalışmalı ve *Pull Request* istemeli

-----------------------------------------------------------------

Pisi GNU/Linux projesinin geliştirilmesine yardım etmek istiyorsanız;
* Öncelikle kendi github hesabınıza projeyi fork'layıp
* Yaptığınız değişiklikleri Pull Request ile gönderebilirsiniz. 
