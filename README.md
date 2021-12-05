# django-rest-testing

:::note alert
Do not use this project as is. Because the secret key is registered.
:::

DjangoのRESTFrameworkのテストの実行方法を確認するためのリポジトリ。  
テスト用のAPIを1つだけ作成した。しかもRESTFullではない。

以下の公式サイトのテストを参考にしている。
[https://www.django-rest-framework.org/api-guide/testing/](https://www.django-rest-framework.org/api-guide/testing/)

以下のテストを作成済み
- APIRequestFactory
- APIClient

## Testing command
```sh
python manage.py test sampleapp/
```
