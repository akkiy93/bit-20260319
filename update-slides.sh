#!/bin/bash
# スライドを更新してGitHubにプッシュするスクリプト
set -e

echo "📄 HTMLを生成中..."
marp slides/presentation.md --output slides/presentation.html --no-stdin

echo "📋 index.htmlにコピー中..."
cp slides/presentation.html index.html

echo "📦 Gitにコミット・プッシュ中..."
git add slides/presentation.md slides/presentation.html index.html
git commit -m "Update slides" || echo "変更なし、スキップ"
git push

echo "✅ 完了！ https://akkiy93.github.io/bit-20260319/"
