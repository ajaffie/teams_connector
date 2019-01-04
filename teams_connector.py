#!/bin/python3
import requests
import argparse
import json
import os

def main():
    with open(os.path.realpath(os.path.join(os.path.dirname(__file__), "config.json"))) as conf:
        urls = json.load(conf)["urls"]
    parser = argparse.ArgumentParser(
                    description='Send a message to all channels specified.')
    parser.add_argument('-s', '--state', dest='state', type=int, required=True)
    parser.add_argument('-n', '--name', dest='name', type=str, required=True)
    args = vars(parser.parse_args())
    message_suffix = " is now "+("online." if args['state'] == 0 else "offline.")
    for url in urls:
        if '*' in url['servers'] or args['name'] in url['servers']: 
            message = ((url['custom_names'][args['name']] if url['custom_names'].get(args['name'], None) != None else "Server "+args['name'])
            + message_suffix)
            requests.post(url['url'], json={'text': message})


if __name__ == "__main__":
    main()
