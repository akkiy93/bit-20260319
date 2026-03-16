# セッションログ：2026/03/15

## 目的
社内勉強会（2026/03/19）向けに、Claude Codeを使った業務効率化のプレゼン資料を作る。

---

## 時系列ログ

### 1. 方針決定
- minorun365さんのQiita記事（Claude Codeで日常業務を爆速化する）を読み込み、発表のフレームワークとして採用することを決定
- 発表テーマ：「Claude Codeは魔法でもなく使えないわけでもない。正しく使えば半自動で業務効率化できる」
- デモのテーマ候補（テスト仕様書・画面設計書・課題管理表・API仕様書）の中から**テスト仕様書**を選定

### 2. プロジェクト基盤の整備
- minorun365記事のフレームワークに倣い、4つのMDファイルを作成
  - `PLAN.md`：目的・デモフロー・最終成果物
  - `SPEC.md`：仕様詳細・ファイル構成・スライド構成案
  - `TODO.md`：タスク管理（Phase1〜3）
  - `KNOWLEDGE.md`：参考記事の知見まとめ

### 3. デモ用ファイルの作成

#### 機能仕様書（feature_spec.md）
- テーマ：ログイン機能（社内業務管理システム）
- 内容：画面構成・入力項目・バリデーション・アカウントロック・セキュリティ要件・非機能要件

#### テスト仕様書（test_spec.md）
- まず人間（ユーザー）がパッと思いついたテスト項目を音声入力で提示
- Claude Codeが仕様書と照らし合わせてレビュー：
  - 仕様書との不一致3点を指摘（ロック解除方法・ボタン仕様・セッション表現）
  - 追加すべき6項目を提案（マスク表示・文字数制限・エラーメッセージ等）
  - 重複2項目を除外提案
- ユーザーが確認・判断し、最終的に31件のテスト仕様書を確定
- その後、チーム運用用の列を追加（優先度・担当者・ステータス・テスト予定日・テスト実施日）

#### Excel変換スクリプト（convert.py）
- `uv` 経由でopenpyxlをインストール（pip/apt が使えない環境だったため）
- Markdown → Excel変換スクリプトをゼロから作成
  - セクション見出しを色分け（濃紺・青・薄青）
  - ヘッダー行に青背景・白文字
  - ゼブラストライプ（1行おきに薄青）
  - 列幅自動調整
- 実行結果：`test_spec.xlsx`（59行 × 12列）生成成功

### 4. フォルダ整理
- uvの自動生成ファイル（main.py）を削除
- README.mdを更新
- `slides/materials.md`（スライド作成用素材まとめ）を作成

### 5. スライド作成

#### Marpでスライド作成
- `slides/presentation.md`（Marp形式）を13枚構成で作成
- デザイン：濃紺ベース、青系カラー統一
- 構成：タイトル → 誤解2つ → 正しい使い方 → 半自動の価値 → デモ4ステップ → まとめ

#### フォント変更（Noto Sans JP）
- Google Fontsからインポートする形で適用

#### スライドの内容修正（ユーザー指示）
- アジェンダの表現を「2つの誤解」→「2つのイメージを整理する」に変更（角が立たないよう）
- 3ページ目に「バイブコーディング（雰囲気だけ）では開発できない」を追加
- 4ページ目のタイトルを「まだ使えない」→「まだ実用的ではない」に変更
- STEP1スライドのコードブロックを削除
- HTMLを再生成

### 6. PPTX / PDF出力の試行と断念

| 試みた方法 | 結果 |
|-----------|------|
| Marp CLI + WindowsのChromeパスを直接指定 | WSL2からのPuppeteer起動が不安定で失敗 |
| VS Code Marp拡張でエクスポート | ブラウザが見つからないエラーで失敗 |
| VS Code設定でChromeパスを手動指定 | 同様のエラーで失敗 |
| HTMLをChromeで開きPDF印刷 → Google Slidesへ | Google SlidesがPDFインポート非対応のため断念 |

→ **GitHub Pages（HTML公開）に切り替え**

### 7. GitHub Pages公開

- GitHubリポジトリ `akkiy93/bit-20260319` を作成（Public）
- 全ファイルをプッシュ（git + SSH認証）
- GitHub Pages APIでPages設定を有効化
- 公開URL：`https://akkiy93.github.io/bit-20260319/`

### 8. GitHub Actions自動化

- `.github/workflows/deploy-slides.yml` を作成
- `slides/presentation.md` を編集してpushするだけで：
  1. GitHub側でMarp CLIが自動実行
  2. HTMLが自動生成
  3. GitHub Pagesに自動反映
- `update-slides.sh`（ローカル用ワンコマンドスクリプト）も併せて作成

---

## 最終的なファイル構成

```
bit-20260319/
├── PLAN.md
├── SPEC.md
├── TODO.md
├── KNOWLEDGE.md
├── README.md
├── index.html                          ← GitHub Pages用
├── update-slides.sh                    ← ローカル更新用ワンコマンド
├── demo/
│   ├── feature_spec.md                 ← 架空の機能仕様書
│   ├── test_spec.md                    ← テスト仕様書（Markdown）
│   ├── test_spec.xlsx                  ← テスト仕様書（Excel変換後）
│   └── convert.py                      ← 変換スクリプト
├── slides/
│   ├── materials.md                    ← スライド素材まとめ
│   ├── presentation.md                 ← スライド本体（Marp）
│   └── presentation.html              ← 生成済みHTML
├── .github/workflows/
│   └── deploy-slides.yml              ← GitHub Actions
├── pyproject.toml
└── uv.lock
```
