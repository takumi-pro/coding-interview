## セットアップ

### 環境変数
以下変数を`.env`へ追加
```
DB_USER={username}
DB_PASSWORD={password}
DB_HOST={hostname}
DB_NAME={dbname}
DB_PORT={port}
```

### データベース
起動
```bash
make db-up
```

停止
```bash
make db-down
```

### Djangoアプリ

仮想環境に入る
```bash
pipenv shell
```

パッケージのインストール
```bash
pipenv install
```

マイグレート
```bash
cd src
python manage.py migrate
```

企業データ挿入
`src/companycategory/fixtures/company_data.json`にある5件の企業データが挿入される
```bash
python manage.py loaddata company_data.json
```

サーバ起動
```bash
python manage.py runserver
```

## API仕様書
サーバ起動後に`http://localhost/docs`にアクセスするとAPI仕様書が閲覧できる。

エンドポイントは以下
```http
BaseURL: http://localhost:8000

・GET /api/categories：一覧取得
・POST /api/categories：作成
・GET /api/categories/{categoryId}：詳細取得
・PUT /api/categories/{categoryId}：更新
・DELETE /api/categories/{categoryId}：削除
```


<img width="500px" alt="api-document" src="https://github.com/takumi-pro/takumi-pro/assets/65642316/cc2275c2-0ac8-409c-b118-d9ba21252aee" />

## テスト
```bash
# 仮想環境に入る
pipenv shell

# srcに移動
cd src

# テスト実行
python manage.py test
```