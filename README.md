# Hawk

Hawk is a lightweight trading backtesting project with a Python frontend and a Rust/PyO3 backend.

## Getting Started

### Prerequisites

- Rust toolchain with `cargo` and `rustc`
- Python 3.10+

### Setup

From the repository root:

```bash
./build.sh
```

This will:

- create a `.venv` Python virtual environment if needed
- install/upgrade Python packaging tools
- install `maturin`
- build the Rust extension and install it into the local venv
- verify the package and extension import

### Run an example

```bash
.venv/bin/python example/simple_strategy.py
```

## Common Commands

- `./build.sh`
  - full developer setup and install
- `.venv/bin/python -m pip install --upgrade maturin`
  - upgrade maturin inside the local venv
- `.venv/bin/python -m maturin develop --release`
  - rebuild the Python extension in place

## FAQ

### Q: Why does Python say `libhawk_core_lib.so` is missing?

A: That means Python is loading an old or stale compiled extension. Rebuild using the local venv and reinstall with:

```bash
.venv/bin/python -m maturin develop --release
```

If the error persists, remove the stale installed extension from `.venv/lib/python3.10/site-packages/` and rebuild.

### Q: What if `.venv` does not exist?

A: `build.sh` creates it automatically. You can also create it manually:

```bash
python3 -m venv .venv
```

### Q: How do I run the example without the helper script?

Use the local venv Python directly:

```bash
.venv/bin/python example/simple_strategy.py
```

### Q: I changed Rust code. How do I rebuild?

```bash
.venv/bin/python -m maturin develop --release
```

### Q: Do I need `uv`?

A: No. `build.sh` now uses standard Python tooling directly and does not require `uv`.
