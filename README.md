# Claude Code 業務効率化デモ

社内勉強会（2026/03/19）向けのプレゼン資料・デモ一式。

## フォルダ構成

```
bit-20260319/
├── PLAN.md          # プロジェクトの目的・デモフロー
├── SPEC.md          # 仕様詳細・ファイル構成・スライド構成案
├── TODO.md          # タスク管理
├── KNOWLEDGE.md     # 参考記事（minorun365）の知見まとめ
├── demo/
│   ├── feature_spec.md    # 架空の機能仕様書（ログイン機能）
│   ├── test_spec.md       # テスト仕様書（Markdown）
│   ├── test_spec.xlsx     # テスト仕様書（Excel変換後）
│   └── convert.py         # Markdown→Excel変換スクリプト
├── slides/
│   ├── materials.md       # スライド作成用素材・構成案
│   └── presentation.md    # スライド本体（Marp形式）※作成予定
├── pyproject.toml
└── uv.lock
```

## デモの実行方法

```bash
uv run python3 demo/convert.py
```
