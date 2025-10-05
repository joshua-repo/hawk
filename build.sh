#!/usr/bin/env bash
set -euo pipefail

echo "🔧 Setting up Hawk development environment..."

# Check prerequisites
command -v uv >/dev/null || { echo "❌ uv not found. Install: curl -LsSf https://astral.sh/uv/install.sh | sh"; exit 1; }
command -v rustc >/dev/null || { echo "❌ Rust not found. Install: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"; exit 1; }

echo "📦 Syncing dependencies..."
uv sync

echo "🦀 Building Hawk package..."
uv pip install --upgrade maturin
uv run maturin develop --release

echo "🧪 Testing installation..."
uv run python -c "
import hawk
import hawk.hawk_core
print('✅ Hawk package:', hawk.__file__)
print('✅ Rust extension:', hawk.hawk_core.__file__)
"

echo "🚀 Done! Run example with: uv run python example/basic_backtest.py"