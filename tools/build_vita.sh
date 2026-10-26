#!/usr/bin/env bash
set -euo pipefail

# Invoke from the repository root, inside the image pinned in the workflow.
CORE_SHA=b45699c9a6b7ed35b075ed0bd9240bd1eb69aa814012c19aee14ef0cc6b79505
RA_COMMIT=69a4f0ea1e8aaf442ae4858f2e7f2b31a1776576
SDK_IMAGE=vitasdk/vitasdk@sha256:7f5eee50ff95b73c8c847dbfef6227aa0035886444b4d0254c21da8369ff1efc
export CORE_SHA RA_COMMIT SDK_IMAGE
mkdir -p vita-out vita-build/core vita-build/source/build-tools
exec > >(tee vita-out/build.log) 2>&1
printf '%s  core-source/modified-core-source.zip\n' "$CORE_SHA" | sha256sum -c -
python3 -m zipfile -e core-source/modified-core-source.zip vita-build/core
git clone --depth 1 --branch v1.22.2 https://github.com/libretro/RetroArch.git vita-build/RetroArch
test "$(git -C vita-build/RetroArch rev-parse HEAD)" = "$RA_COMMIT"
git -C vita-build/RetroArch archive --prefix=RetroArch/ HEAD | tar -x -C vita-build/source
cp core-source/modified-core-source.zip vita-build/source/
cp tools/build_vita.sh tools/verify_vita.py vita-build/source/build-tools/
cp .github/workflows/build-vita-core.yml vita-build/source/build-tools/
arm-vita-eabi-gcc --version > vita-out/toolchain.txt
find "$VITASDK" -iname '*license*' -o -iname '*copyright*' > vita-out/sdk-license-paths.txt
make -C vita-build/core -f Makefile.libretro platform=vita -j2
cp vita-build/core/genesis_plus_gx_libretro_vita.a vita-build/RetroArch/libretro_vita.a
make -C vita-build/RetroArch -f Makefile.vita -j2 retroarch_vita.self
python3 tools/verify_vita.py
cp vita-out/BUILD-VITA.json vita-build/source/
tar -cJf vita-out/Snatcher-KR-V1.0-Vita-source.tar.xz -C vita-build/source .
sha256sum vita-out/*.self vita-out/*.tar.xz > vita-out/SHA256SUMS-build.txt
