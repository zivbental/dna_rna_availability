#!/usr/bin/env bash
# Run from a repository checkout. Extra arguments go to benchmark.py.
set -euo pipefail
BENCHMARK_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$BENCHMARK_ROOT"
BENCHMARK_PYTHON="${BENCHMARK_PYTHON:-$BENCHMARK_ROOT/.venv/bin/python}"
export OMP_NUM_THREADS="${OMP_NUM_THREADS:-1}"
export OPENBLAS_NUM_THREADS="${OPENBLAS_NUM_THREADS:-1}"
export PYTHONUNBUFFERED=1
"$BENCHMARK_PYTHON" validation/multi_dataset/prepare.py
exec "$BENCHMARK_PYTHON" validation/multi_dataset/benchmark.py --workers "${BENCHMARK_WORKERS:-4}" --resume "$@"
