import json
import os
import threading
from dotenv import load_dotenv
from linepy import (LINE, Channel, OEPoll, OpType)

# Auth
load_dotenv()
try:
    if (id_ := os.getenv("EMAIL_ID")) and (pwd := os.getenv("PASSWORD")):
        client = LINE(id_, pwd)
    elif token := os.getenv("TOKEN"):
        client = LINE(idOrAuthToken=token)
    else:
        client = LINE(showQr=True)
except Exception as e:
    print("Failed to authenticate")
    print(e)
    exit(1)

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

        # message only contains text
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
