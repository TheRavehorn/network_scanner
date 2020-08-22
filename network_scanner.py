#!/usr/bin/env python3
import setup
import scapy.all as scapy
import subprocess


def scan(ip):
    scapy.arping(ip)


print("Simple network scanner 0.01 by Ravehorn.")
subprocess.call("ifconfig", shell=True)
ip_to_scan = input("Type IP range to scan: ")
scan(ip_to_scan)
