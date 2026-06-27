#!/usr/bin/env bash
set -euo pipefail

echo "🔧 Setting up Hawk development environment..."

check_tool() {
    if ! hash "$1" 2>/dev/null; then
        echo "❌ $2" >&2
        exit 1
    fi
}

check_tool rustc "Rust not found. Install: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"
check_tool cargo "Cargo not found. Install Rust toolchain with rustup"
check_tool python3 "python3 not found. Install Python 3.10+"

if [ ! -d ".venv" ]; then
    echo "🐍 Creating Python virtual environment (.venv)..."
    python3 -m venv .venv
fi

echo "📦 Upgrading Python packaging tooling..."
.venv/bin/python -m ensurepip --upgrade >/dev/null 2>&1 || true
.venv/bin/python -m pip install --upgrade pip setuptools wheel
.venv/bin/python -m pip install --upgrade maturin

echo "🦀 Building Hawk Rust extension..."
.venv/bin/python -m maturin develop --release

echo "🧪 Verifying installation..."
.venv/bin/python -c "import hawk, hawk.hawk_core; print('✅ Hawk package:', hawk.__file__); print('✅ Rust extension:', hawk.hawk_core.__file__)"

echo "🚀 Hawk is ready. Run an example with: .venv/bin/python example/simple_strategy.py"
