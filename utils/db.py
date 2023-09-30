from pymongo import MongoClient
print("Connecting to database...")
client = MongoClient(
    "mongodb+srv://onepiece:gear5@cluster0.qgjnyhj.mongodb.net/?retryWrites=true&w=majority"
)

db = client["techzcloud"]
filesdb = db["files"]
print("Connected to database...")

def save_file_in_db(orgname, filename, hash, msg_id=None):
    filesdb.update_one(
        {
            "hash": hash,
            "fid": fid,
        },
        {"$set": {"filename": filename, "filenamex": orgname, "msg_id": msg_id}},
        upsert=True,
    )


def is_hash_in_db(hash):
    data = filesdb.find_one({"hash": hash})
    if data:
        return data
    else:
        return None
