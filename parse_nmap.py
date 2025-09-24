#!/usr/bin/env python3
"""parse_nmap.py
Convert nmap XML (-oX) into a human-friendly Markdown report.

Usage:
    python3 parse_nmap.py input_nmap.xml output_report.md
"""
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

def parse_host(host):
    addr = host.find('address').get('addr') if host.find('address') is not None else 'unknown'
    status = host.find('status').get('state') if host.find('status') is not None else 'unknown'
    os_el = host.find('os')
    os_name = 'unknown'
    if os_el is not None:
        osmatch = os_el.find('osmatch')
        if osmatch is not None:
            os_name = osmatch.get('name')
    ports = []
    ports_el = host.find('ports')
    if ports_el is not None:
        for p in ports_el.findall('port'):
            portid = p.get('portid')
            proto = p.get('protocol')
            state = p.find('state').get('state') if p.find('state') is not None else ''
            svc = p.find('service')
            svcname = svc.get('name') if svc is not None else ''
            svcprod = svc.get('product') if svc is not None and 'product' in svc.attrib else ''
            svcver = svc.get('version') if svc is not None and 'version' in svc.attrib else ''
            ports.append((proto, portid, state, svcname, svcprod, svcver))
    return dict(addr=addr, status=status, os=os_name, ports=ports)

def main(inp, outp):
    tree = ET.parse(inp)
    root = tree.getroot()
    hosts = []
    for host in root.findall('host'):
        hosts.append(parse_host(host))
    with open(outp, 'w') as f:
        f.write(f"# Nmap Scan Report\n\nGenerated: {datetime.utcnow().isoformat()}Z\n\n")
        for h in hosts:
            f.write(f"## Host: {h['addr']}\n\n")
            f.write(f"Status: {h['status']}\n\nOS Guess: {h['os']}\n\n")
            f.write("### Open Ports\n\n")
            if not h['ports']:
                f.write("No open ports found or ports filtered.\n\n")
            else:
                f.write("| Proto | Port | State | Service | Product | Version |\n")
                f.write("|---|---:|---|---|---|---|\n")
                for p in h['ports']:
                    proto, portid, state, svcname, svcprod, svcver = p
                    f.write(f"| {proto} | {portid} | {state} | {svcname} | {svcprod} | {svcver} |\n")
                f.write('\n')
    print(f"Wrote report to {outp}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: parse_nmap.py input.xml output.md')
        sys.exit(2)
    main(sys.argv[1], sys.argv[2])
