# Nmap Folder

Contains:
- `nmap_scan.sh` — safe Nmap commands to run inside your lab.
- `parse_nmap.py` — Python script that converts Nmap XML (`-oX`) into a readable Markdown report.
- `sample_nmap.xml` — a small example (placeholder).

## Quick usage

1. Run an Nmap scan and save XML:
```bash
sudo ./nmap_scan.sh 192.168.56.101
# produces reports/nmap_target.xml and reports/nmap_target.nmap
```

2. Convert XML to Markdown:
```bash
python3 parse_nmap.py reports/nmap_target.xml reports/nmap_report.md
```
