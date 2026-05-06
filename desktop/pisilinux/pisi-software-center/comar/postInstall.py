import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
	# MIME veritabanını güncelle (.pisi uzantısını tanısın)
	os.system("update-mime-database /usr/share/mime")

	# Desktop veritabanını güncelle (Hangi dosyanın hangi uygulama ile açılacağını kaydet)
	os.system("update-desktop-database /usr/share/applications")

	# (Opsiyonel) .pisi dosyaları için varsayılan uygulamayı ayarla
	os.system("xdg-mime default pisi-installer.desktop application/pisi-software-center.xml")
