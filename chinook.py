import os
import argparse
import requests
from bs4 import BeautifulSoup

#TODO Build template for config.ini in case it gets deleted

parser = argparse.ArgumentParser(description="Application that goes seeks and downloads request items")
parser.add_argument("-s", action="store", dest="single_item", help="request only one item", default=None)
parser.add_argument("-c", action="store", dest="config_override", help="use supplied config rather than default (script directory)", default=None)
parser.add_argument('--version', action='version', version='1.0')
args = parser.parse_args()

# Configuring params for script
single_only = False if not args.single_item else True
config_location = args.config_override if args.config_override else os.path.join(os.path.dirname(__file__), "conf", "conf.ini")

movie_url = ""
results = requests.get(movie_url)
print(results.content)
# soup = BeautifulSoup(results.content, 'html.parser')
# a = soup.find_all('tbody')
# print(a)