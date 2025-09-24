# 5-minute Demo Script — Recon & Findings

Total length: 5:00

00:00 — 00:20   Intro (objective + legal reminder)
00:20 — 01:30   Show Nmap quick discovery & port scan
 - Run: `sudo nmap -Pn -sS -sV -O -p22,21,80 192.168.56.101 -oA reports/nmap_target_demo`
 - Show `nmap` output (highlight open ports and versions)

01:30 — 02:30   Show OpenVAS scan initiation (web UI)
 - Start a previously configured task; explain scan config
 - Show exported summary (PDF) or the "Top Vulnerabilities" view

02:30 — 03:30   Packet capture demo
 - Start `sudo tcpdump -i eth0 -w capture.pcap` (already running in background on demo machine)
 - Show FTP login captured in Wireshark (filter `ftp`), highlight `USER`/`PASS` packets

03:30 — 04:30   Firewall demo
 - Show simple `iptables` rule applied to block an IP or rate-limit (paste commands)
 - Show a subsequent scan attempt and how it is dropped (tail `dmesg` or `iptables -L -v`)

04:30 — 05:00   Wrap-up & next steps
 - Explain remediation: patch services, limit exposure, run repeat scans, maintain logs
 - Link to GitHub repo (this repo) for commands and templates

Recording tips:
- Use `asciinema` for terminal recording: `asciinema rec demo.cast` then `asciinema upload demo.cast`
- Or use `ffmpeg` to record the screen (example provided in `demo_record_steps.md`).
