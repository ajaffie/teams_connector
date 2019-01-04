# Icinga2 Microsoft Teams Connector

#### By Andrew Jaffie (ajaffie)


## Description

This simple script makes use of the 'incoming webhook' connector in MS Teams. It will simply send a message stating that the server has either gone offline or online based on the last hard state of the host. 

## Requirements

Internet access, Python 3, and the requests package are required.

## Installation
1. Clone git repo:

    git clone https://github.com/ajaffie/teams_connector.git
    cd teams_connector
    git tag -l
    git checkout <latest tagged version>

2. Create webhook(s) in desired MS Teams channels and add the urls to the `urls` list in `config.json`.
3. For each webhook in `config.json`, either put a "\*" to include all notifications for that channel, or list the servers you want notifications to be sent to that channel for.
*Optional:* You can specify custom names for servers to use instead of "Server <name>" in the messages. This is most useful for cases where the script executed automatically by a system such as Icinga or Nagios where the name specified is the internal name/FQDN and you want a more user-friendly message printed.
4. Add `NotificationCommand` definition and `Notification` apply rules to your Icinga2/Nagios/etc. configurations.
5. Stop cluttering your inbox and instead annoy everyone in MS Teams!

(A `NotificationCommand` definition is included, but you **MUST** change the path, as it uses a custom defined constant.)
