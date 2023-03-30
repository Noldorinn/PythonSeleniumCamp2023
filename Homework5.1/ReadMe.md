PyTest Decoratörleri

    @pytest.fixture : Test için ihtiyaç duyulan bir öge oluşturur.

    @pytest.mark.parametrize : Teste göderilecek değerleri sırasıyla teste ekler ve her değer için testi çalıştırır.

    @pytest.mark.xfail : Testtin başarısız olacağını öngörülen durumlarda çalıştırılır ve hata olarak raporlanmaz.

    @pytest.mark.skip : Testi çalıştırmaz, sonraki teste atlar.

    @pytest.mark.skipif : Belirli bir koşula bağlı olarak testin çalıştırılmadan atlanmasını sağlar. 

    @pytest.mark.timeout : Testi belli bir zaman aşımı değeri kadar çalıştırır.

    @pytest.mark.filterwarning : Testin bir uyarı mesajını içermesi durumunda testi başarısız olarak belirtmek için kullanılır.

    @pytest.mark.dependency : Testler arasındaki bağlılıkları belirlemeye yarar.

    @pytest.mark.order : Test için sıra belirlemeyi sağlar.

    @pytest.mark.flaky : Test için bir hata oranı belirlemeye yarar ve hata bu değerin üzerinde ise testi tekrarlar.