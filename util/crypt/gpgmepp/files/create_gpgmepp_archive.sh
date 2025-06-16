#!/bin/bash

# Herhangi bir hata oluştuğunda betiği durdur
set -e

# Proje adı
PROJECT_NAME="gpgmepp"
# Arşivin adı (en güncel sürüm olduğu için "latest" kullandık)
ARCHIVE_NAME="${PROJECT_NAME}-latest"
# Kullanıcının belirttiği Git deposu URL'si
GIT_REPO_URL="https://dev.gnupg.org/source/${PROJECT_NAME}.git"
# Arşivlenecek branch/tag (varsayılan olarak HEAD, yani en son commit)
# Eğer belirli bir versiyonu (örn: gpgmepp-2.0.0) indirmek isterseniz,
# bu satırı "gpgmepp-2.0.0" gibi bir etiketle değiştirebilirsiniz.
# Şu anki haliyle depodaki en son halini indirecektir.
REFERENCE="cd13d4b00cd19d723574acf843abee95111070fb"

echo "${PROJECT_NAME} projesinin '${REFERENCE}' referansına ait arşiv oluşturuluyor..."

# Git deposundan belirtilen referansın (HEAD) anlık görüntüsünü alarak doğrudan tar.xz arşivi oluştur
# --prefix sayesinde arşivin içindeki kök klasör adı 'gpgmepp-latest/' olacak
echo "Git deposundan '${REFERENCE}' referansının arşivlenmesi başlatılıyor..."
git archive --format=tar --prefix="${ARCHIVE_NAME}/" "${REFERENCE}" -o "${ARCHIVE_NAME}.tar" --remote="${GIT_REPO_URL}"

# Oluşturulan tar dosyasını xz ile sıkıştır
echo "${ARCHIVE_NAME}.tar dosyası .xz formatına sıkıştırılıyor..."
xz -k "${ARCHIVE_NAME}.tar"

echo "Arşiv başarıyla oluşturuldu: ${ARCHIVE_NAME}.tar.xz"
echo "Dosya mevcut konumunuzda (${PWD}) bulunmaktadır."
