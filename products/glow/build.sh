#!/bin/bash
# Usage: ./build.sh file.html ...  -> file.pdf (Chromium print-to-PDF, margin boxes + page numbers)
CH=${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}
for f in "$@"; do
  "$CH" --headless --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf="${f%.html}.pdf" "file://$(pwd)/$f" 2>&1 | grep -v -i "ssl\|dbus\|gpu" | tail -1
done
