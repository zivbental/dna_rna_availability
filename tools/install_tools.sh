#!/usr/bin/env bash
# Bootstrap a self-contained micromamba environment holding the external
# command-line tools used by the rnavail accessibility pipeline.
#
# Everything lands under <project>/.tools and can be removed with:
#   rm -rf .tools
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLS="$ROOT/.tools"
MAMBA="$TOOLS/bin/micromamba"
ENV="$TOOLS/env"
export MAMBA_ROOT_PREFIX="$TOOLS"

mkdir -p "$TOOLS/bin"

if [ ! -x "$MAMBA" ]; then
  echo "[bootstrap] downloading micromamba ..."
  # The release tarball is bzip2-compressed and `bzip2` is not always present,
  # so unpack through Python's stdlib rather than relying on tar -j.
  curl -Ls -o "$TOOLS/micromamba.tar.bz2" \
    https://micro.mamba.pm/api/micromamba/linux-64/latest
  python3 - "$TOOLS" <<'PYEOF'
import bz2, io, os, sys, tarfile
tools = sys.argv[1]
with open(os.path.join(tools, "micromamba.tar.bz2"), "rb") as fh:
    raw = bz2.decompress(fh.read())
with tarfile.open(fileobj=io.BytesIO(raw)) as tf:
    member = tf.getmember("bin/micromamba")
    tf.extract(member, path=tools)
os.chmod(os.path.join(tools, "bin", "micromamba"), 0o755)
PYEOF
  rm -f "$TOOLS/micromamba.tar.bz2"
fi
"$MAMBA" --version

CHANNELS="-c conda-forge -c bioconda"

# Core set: failure here is fatal, these carry the pipeline.
echo "[bootstrap] creating env with core tools ..."
"$MAMBA" create -y -p "$ENV" $CHANNELS --json >/dev/null 2>&1 || true
"$MAMBA" install -y -p "$ENV" $CHANNELS viennarna || {
  echo "[bootstrap] FATAL: core install failed"; exit 1; }

# Optional set: probed one at a time so a single unavailable package
# does not abort the rest. contrafold also carries the eternafold adapter,
# which reuses this same binary under EternaFoldParams.v1 (bundled in
# rnavail/adapters/data/, no separate install step).
for pkg in rnastructure linearfold contrafold; do
  echo "[bootstrap] optional: $pkg"
  "$MAMBA" install -y -p "$ENV" $CHANNELS "$pkg" >/dev/null 2>&1 \
    && echo "   installed $pkg" || echo "   unavailable, skipped $pkg"
done

echo
echo "[bootstrap] binaries now available in $ENV/bin :"
ls "$ENV/bin" | grep -iE 'rna|linear|contra|fold|bifold|partition' | sort | sed 's/^/   /'
