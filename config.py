import os

API_ID = API_ID = 9344337

API_HASH = os.environ.get("API_HASH", "7e55bf98380e416d5de1c4c567395a32")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6348631191:AAHAOHOL5i46ibm0AsNuqiVlT7xhKrbsov0")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6040965491))

LOG = -1001892889781

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6040965491","5123039648").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


