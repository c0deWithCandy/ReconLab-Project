#!/usr/bin/env bash
# nmap_scan.sh
# Usage: ./nmap_scan.sh <target-ip-or-cidr>
# SAFE defaults for a lab. Replace target as needed. Do NOT run against networks you don't own.

set -euo pipefail

TARGET=${1:-"192.168.56.101"}
OUTDIR="../reports"
mkdir -p "$OUTDIR"

echo "[*] Running quick ping-scan to discover hosts..."
sudo nmap -sn "$TARGET" -oN "$OUTDIR/nmap_ping_scan.nmap"

echo "[*] Running TCP SYN + version detection + OS detection (all TCP ports)"
sudo nmap -Pn -sS -sV -O -p- --min-rate=500 "$TARGET" -oA "$OUTDIR/nmap_target"

echo "[*] Running targeted UDP scan for common services (may be slow)"
sudo nmap -sU -p 53,67,69,123,161 "$TARGET" -oN "$OUTDIR/nmap_udp_scan.nmap"

echo "[*] Done. Files in $OUTDIR"
