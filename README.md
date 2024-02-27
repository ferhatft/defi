# Detaylı Blog ve Forum Sitesi

Bu Django tabanlı proje, detaylı bir blog ve forum sitesi oluşturmayı amaçlar. Kullanıcılar, çeşitli içerikler paylaşabilir, tartışabilir ve etkileşime geçebilirler.

## Özellikler

- Kullanıcıların kayıt olup oturum açmasına olanak tanıyan Django Allauth entegrasyonu.
- Zengin metin düzenleme yetenekleri için Django CKEditor'un kullanımı.
- Kullanıcıların profil oluşturup düzenleyebileceği profiller modülü.
- Blog için kategori ve etiket desteği sağlayan Django Taggit entegrasyonu.
- Kullanıcıların blog gönderilerine oy verebileceği ve yorum yapabileceği bir forum sistemi (django-vote ve kendi yorum sistemi).
- Medya dosyalarını yüklemek ve yönetmek için CKEditor Uploader entegrasyonu.

## Başlarken

1. Projeyi bilgisayarınıza klonlayın.
2. Sanal bir ortam oluşturun ve bağımlılıkları yüklemek için `pip install -r requirements.txt` komutunu çalıştırın.
3. Veritabanını oluşturmak için `python manage.py migrate` komutunu çalıştırın.
4. Sunucuyu başlatmak için `python manage.py runserver` komutunu çalıştırın.
5. Tarayıcınızda `http://localhost:8000` adresine giderek uygulamayı görüntüleyebilirsiniz.

