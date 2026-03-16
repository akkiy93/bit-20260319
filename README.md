# Claude Code 業務効率化デモ

社内勉強会（2026/03/19）向けのプレゼン資料・デモ一式。

## スライド公開URL

https://akkiy93.github.io/bit-20260319/

## フォルダ構成

```
bit-20260319/
├── README.md
├── index.html                   # GitHub Pages 公開用（自動生成）
├── update-slides.sh             # スライドをローカルで更新するスクリプト
├── docs/                        # プロジェクト管理ドキュメント
│   ├── PLAN.md                  # 目的・デモフロー
│   ├── SPEC.md                  # 仕様詳細
│   ├── TODO.md                  # タスク管理
│   ├── KNOWLEDGE.md             # 参考記事の知見まとめ
│   ├── SESSION_LOG.md           # 作業ログ
│   ├── SUMMARY.md               # まとめ・振り返り
│   └── materials.md             # スライド作成用素材
├── demo/                        # デモファイル一式
│   ├── feature_spec.md          # 架空の機能仕様書（ログイン機能）
│   ├── test_spec.md             # テスト仕様書（Markdown）
│   ├── test_spec.xlsx           # テスト仕様書（Excel変換後）
│   └── convert.py               # Markdown→Excel変換スクリプト
├── slides/                      # スライドファイル
│   ├── presentation.md          # スライド本体（Marp形式）
│   └── presentation.html        # 生成済みHTML
├── .github/workflows/
│   └── deploy-slides.yml        # GitHub Actions（自動デプロイ）
├── pyproject.toml
└── uv.lock
```

## デモの実行方法

```bash
uv run python3 demo/convert.py
```
