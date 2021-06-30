#!/usr/bin/env python3

# imports
import argparse
import requests, json
import sys
from sys import argv
import os

# parser
parser = argparse.ArgumentParser()

parser.add_argument("-v", help="target/host IP address", type=str, dest='target', required=True)

args = parser.parse_args()


# colors
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

# banner
def banner():
    print (red+"IP TRACER")


banner()

ip = args.target
api = "https://ip.api.com/json"

