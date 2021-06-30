#!/usr/bin/env python3

# imports
import argparse
import requests, json
import sys
from sys import argv
import os

# parser values
parser = argparse.ArgumentParse()

parser.add_argument("-v", help="target/host IP address", type=str, dest='target', required=True)

args = parser.parse_args()