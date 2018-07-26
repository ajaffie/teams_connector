#!/bin/python3
import requests
import argparse
import json


def main():
    with open("config.json") as conf:
        urls = json.load(conf)["urls"]
    parser = argparse.ArgumentParser(
                    description='Send a message to all channels that have a url configured.')
    parser.add_argument('-s', '--state', dest='state', type=int, required=True)
    parser.add_argument('-n', '--name', dest='name', type=str, required=True)
    args = vars(parser.parse_args())
    message = "Server "+args['name']+" is now "+("online." if args['state'] == 0 else "offline.")
    for url in urls:
        requests.post(url, json={'text': message})


if __name__ == "__main__":
    main()
