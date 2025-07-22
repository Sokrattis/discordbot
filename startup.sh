#!/bin/bash
cd /home/site/wwwroot
echo "🔧 Iniciando health‑check HTTP na porta 8000"
nohup python3 -m http.server 8000 >/dev/null 2>&1 &
echo "🔧 Iniciando Discord‑Bot"
python3 authades.py