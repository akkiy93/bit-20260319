---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap');
  section {
    font-family: 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
    font-size: 28px;
    padding: 48px 64px;
  }
  section.title {
    background: linear-gradient(135deg, #1a3a5c 0%, #2563a8 100%);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 64px 80px;
  }
  section.title h1 {
    font-size: 42px;
    color: white;
    border: none;
    border-left: 8px solid #7EC8E3;
    padding-left: 20px;
    margin-bottom: 24px;
    line-height: 1.4;
  }
  section.title h2 {
    font-size: 24px;
    color: #BDD7EE;
    margin-bottom: 32px;
    padding-left: 28px;
  }
  section.title p {
    color: #90C8E0;
    font-size: 20px;
    padding-left: 28px;
  }
  h1 {
    font-size: 36px;
    color: #1F4E79;
    border-bottom: 3px solid #4472C4;
    padding-bottom: 8px;
    margin-bottom: 24px;
  }
  h2 {
    font-size: 28px;
    color: #2E75B6;
  }
  .highlight {
    background: #DEEAF1;
    border-left: 6px solid #4472C4;
    padding: 12px 20px;
    border-radius: 4px;
    margin: 12px 0;
  }
  .bad {
    background: #FFF0F0;
    border-left: 6px solid #C00000;
    padding: 12px 20px;
    border-radius: 4px;
    margin: 12px 0;
  }
  .good {
    background: #F0FFF4;
    border-left: 6px solid #00B050;
    padding: 12px 20px;
    border-radius: 4px;
    margin: 12px 0;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 22px;
  }
  th {
    background: #4472C4;
    color: white;
    padding: 8px 12px;
  }
  td {
    padding: 8px 12px;
    border: 1px solid #BDD7EE;
  }
  tr:nth-child(even) td {
    background: #DEEAF1;
  }
  .step-box {
    background: #EBF3FB;
    border: 2px solid #4472C4;
    border-radius: 8px;
    padding: 12px 20px;
    margin: 8px 0;
    font-size: 24px;
  }
  .arrow {
    text-align: center;
    font-size: 28px;
    color: #4472C4;
    margin: 2px 0;
  }
---

<!-- _class: title -->

# 脱・Excel職人宣言
## 〜Claude Codeで開発における面倒な業務を半自動化する〜

2026/03/19　社内勉強会

---

# 今日話すこと

1. **Claude Codeへの2つのイメージを整理する**
   バイブスで開発できる ／ 魔法の杖ではない

2. **正しい使い方：人への依頼と同じ考え方**
   方向性・成果物・手順をしっかり伝える

3. **実際にやってみたデモ**
   エクセルのテスト仕様書を半自動で作る

---

# よくある誤解 ①「バイブスで開発できる」

<div class="bad">
❌ 「Claude Codeに言えば何でもやってくれる」
</div>

### 実際は…

- 実はバイブコーディングはバイブスだけでは開発できない
- 曖昧な指示 → 曖昧な成果物が返ってくる

<div class="highlight">
👉 AIも同じ。ゴールと制約を伝えないと期待した結果にならない。
</div>

---

# よくある誤解 ②「魔法の杖ではない」

<div class="bad">
❌ 「品質が落ちる」「信用できない」
</div>

### 実際は…

- **得意なこと**：繰り返し作業・フォーマット変換・情報の整理・網羅的な案出し
- **苦手なこと**：ドメイン固有の判断・品質の最終確認・暗黙知の理解

<div class="highlight">
👉 得意な部分に使えば、人間より速く・ミスなく動く。
</div>

---

# 正しい使い方：人への依頼と同じ

人に仕事を頼むとき、どう伝えますか？

| 伝えること | 例 |
|-----------|---|
| **① 方向性** | 何のためにやるのか |
| **② 成果物** | どんなアウトプットが欲しいか |
| **③ 手順・制約** | どうやって作るか、何はNGか |

<div class="good">
✅ Claude Codeも同じ。この3つを伝えれば、<br>確認・修正のループが減り、速く・正確に動く。
</div>

---

# 「全自動」より「半自動」が最強

| | 全部手作業 | 全部AIに丸投げ | **半自動** |
|---|:---------:|:------------:|:---------:|
| 速さ | 🐢 遅い | ⚡ 速い | ⚡ 速い |
| 品質 | ✅ 高い | ⚠️ 不安定 | **✅ 高い** |
| 人間の関与 | 多すぎ | 少なすぎ | **適切** |
| リスク | 時間コスト | 内容の正確性 | **低い** |

<div class="highlight">
💡 人間が判断すべき部分だけ人間がやる。それ以外はAIに任せる。
</div>

---

# 武器：音声入力を使う

Claude Codeへの指示は**音声入力**が最強

<div class="highlight">
🎤 キーボードより3〜5倍速く、思ったことをそのまま伝えられる
</div>

### 特に重要：最初に「全部ダンプ」する

- ❌ 少ない情報から膨らませる → 自分の意図と違うものができあがる
- ✅ 思っていることを全部しゃべる → 大量の情報を整理・削る

> 「完璧な一文」を考えながら打つより、<br>「雑でいいから全部言い切る」方が、自分の意図に近いものができる


---

# デモ：テスト仕様書を半自動で作る

エンジニアあるある ──「エクセル開いてる時間のほうが長くない？」

<div class="step-box">STEP 1　機能仕様書（Markdown）を用意する</div>
<div class="arrow">↓</div>
<div class="step-box">STEP 2　Claude Codeにテスト項目を提案させる</div>
<div class="arrow">↓</div>
<div class="step-box">STEP 3　人間が確認・補完してテスト仕様書（Markdown）を完成させる</div>
<div class="arrow">↓</div>
<div class="step-box">STEP 4　スクリプトでMarkdown → Excelに自動変換する</div>

---

# STEP 1：機能仕様書を用意する

ログイン機能の仕様書をMarkdownで記述

- 画面構成・入力項目・バリデーション仕様
- アカウントロック仕様・セキュリティ要件・非機能要件

**ポイント**：Markdownで書くことで、AIが読み込みやすくなる

---

# STEP 2：AIにテスト項目を提案させる

Claude Codeが仕様書を読んで網羅的にテスト項目を提案

- 正常系・異常系・境界値を自動で分類
- 見落としがちな観点も拾ってくれる
  - セキュリティ（ハッシュ化・セッション固定攻撃）
  - ブラウザ互換性
  - パフォーマンス要件

<div class="highlight">
💡 AIは「案出し・網羅性チェック」が得意。<br>
まず全部出させてから、人間が取捨選択する。
</div>

---

# STEP 3：人間が確認・補完する

AIの提案をそのまま使わず、人間がレビューする

### 今回実際にやったこと
- ✅ 仕様書と照らし合わせて誤りを修正
- ✅ 重複・不要な項目を除外
- ✅ チーム運用に必要な列を追加（担当者・優先度・ステータス等）

<div class="highlight">
👉 ここが「半自動」のポイント。<br>AIが作った初稿を人間が仕上げる。
</div>

---

# STEP 4：Excelに自動変換する

コマンド1行でMarkdown → 整形済みExcelが生成される

```bash
uv run python3 demo/convert.py
# ✅ 変換完了: test_spec.xlsx
```

### 変換後のExcelの特徴
- ヘッダー行・セクション見出しに色付き
- 列幅を内容に合わせて自動調整
- 担当者・予定日・ステータスの列も完備

---

# 何が嬉しいのか

### ⏱ 時間削減
テスト項目の洗い出し・Excel整形で**1〜2時間 → 30分以内**に

### ✅ 品質向上
AIが網羅的に案出し。人間は「判断」に集中できる

### ♻️ 再利用しやすい
MarkdownはGit管理できる → 次の案件のテンプレートに

### 👥 チームで使いやすい
担当者・優先度・ステータス列で**そのままチーム運用に使える**

---

# まとめ

<div class="good">
✅ Claude Codeは「優秀な後輩」として使う
</div>

- **方向性・成果物・手順**を伝えれば期待通りに動く
- **人間が判断すべき部分**は人間がやる（品質の担保）
- **単純作業・繰り返し作業**はAIに任せる（速度・ミス削減）

### 今日のデモで使ったフレームワーク

| ファイル | 役割 |
|---------|------|
| PLAN.md | やりたいことを言語化（音声入力で） |
| SPEC.md | AIとの認識合わせ |
| TODO.md | 進捗管理 |
| KNOWLEDGE.md | 学びの蓄積 |

---

<!-- _class: title -->

# ご清聴ありがとうございました

質問・相談あればお気軽に！
