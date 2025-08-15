#!/bin/bash

# MPlayer revizyon numarası
REVISION=38542

# Kaynak URL
SOURCE_URL="svn://svn.mplayerhq.hu/mplayer/trunk@$REVISION"

# Çıkış dizini ve dosya adları
DIR_NAME="mplayer-$REVISION"
OUTPUT_FILE="$DIR_NAME.xz"

echo "MPlayer revizyon $REVISION indiriliyor..."
svn checkout -r $REVISION $SOURCE_URL $DIR_NAME

if [ $? -eq 0 ]; then
    echo "Indirme başarılı. Sıkıştırma yapılıyor..."
    tar -cJf $OUTPUT_FILE $DIR_NAME
    
    if [ $? -eq 0 ]; then
        echo "Sıkıştırma başarılı: $OUTPUT_FILE"
        # İsteğe bağlı: Geçici dizini silmek
        # rm -rf $DIR_NAME
    else
        echo "Sıkıştırma hatası!" >&2
        exit 2
    fi
else
    echo "SVN indirme hatası!" >&2
    exit 1
fi