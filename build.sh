#!/bin/bash
# Simple build script

echo "🔨 Building Hawk Trading Engine (Minimal)"

# Create build directory
mkdir -p build
cd build

# Configure and build with debug symbols
cmake -DCMAKE_BUILD_TYPE=Debug ..
make -j4

# Build Python package
cd ..
pip install -e .

echo "✅ Build complete! Try running:"
echo "python examples/basic_backtest.py"
echo ""
echo "For debugging in VSCode:"
echo "1. Set breakpoints in Python or C++ code"
echo "2. Use F5 to start debugging"
echo "3. Choose 'Python: Current File' for Python debugging"
echo "4. Choose 'C++: Attach to Python' for mixed debugging"
