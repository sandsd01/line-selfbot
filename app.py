import json
import threading
from linepy import (LINE, Channel, OEPoll, OpType)

# loading config
with open('config.json', 'r') as f:
    config = json.load(f)

try:
    if len(config["EMAIL/ID"]) != 0:
        client = LINE(config["EMAIL"], config["PASSWORD"])
    elif config["TOKEN"] == "":
        client = LINE(showQr=True)
    else:
        client = LINE(idOrAuthToken=config["TOKEN"])
except json.decoder.JSONDecodeError as f:
    print("Failed to authenticate")

ops = OEPoll(client)
whitelist = [client.profile.mid, client, ]

while True:
    try:
        Operation = ops.singleTrace(count=50)
        if Operation is not None:
            for op in Operation:
                ops.setRevision(op.revision)
                # self.OpInterrupt[op.type], args=(op,)
                thread1 = threading.Thread(target=LINE_OP_TYPE, args=(op,))
                thread1.start()
                thread1.join()
    except Exception as error:
        print(error)


def LINE_OP_TYPE(op):
    if op.type == 25:  # sent message
        message = op.message
        content = message.text
        msg_to = message.to
        msg_from = message._from

        if message.contentType == 0:
            if "@everyone" in content and msg_from in whitelist:
                group = client.getGroup(msg_to)
                members = [contact for contact in group.members]
                try:
                    for bubble in range((len(members) // 20) + 1):
                        placement = 0
                        mentionees = []
                        for mems in group.members[bubble * 20: (bubble + 1) * 20]:
                            mentionees.append({
                                "S": str(placement),
                                "E": str(placement + 6),
                                "M": mems.id
                            })
                        client.sendMessage(msg_to, '', contentMetadata={
                                           u'MENTION': json.dumps({'MENTIONEES': mentionees})
                                           }, contentType=0)
                except Exception as e:
                    client.sendMessage(msg_to, str(e))
