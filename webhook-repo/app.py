from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime
from flask_cors import CORS

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["github_events"]
collection = db["events"]



app=Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Server is running"



@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event")

    if event_type=="push":
        document={
            "request_id":data["head_commit"]["id"],
            "author":data["pusher"]["name"],
            "action":"PUSH",
            "from_branch":None,
            "to_branch":data["ref"].split("/")[-1],
            "timestamp":datetime.utcnow().strftime("%d %b %Y - %I:%M %p UTC")
        }
        collection.insert_one(document)
    elif event_type == "pull_request":
        pr = data["pull_request"]

        if data["action"] == "opened":
            document = {
            "request_id": str(pr["id"]),
            "author": pr["user"]["login"],
            "action": "PULL_REQUEST",
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "timestamp": datetime.utcnow().strftime("%d %b %Y - %I:%M %p UTC")
        }

        collection.insert_one(document)


        if pr["merged"]:
            document = {
            "request_id": str(pr["id"]),
            "author": pr["user"]["login"],
            "action": "MERGE",
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "timestamp": datetime.utcnow().strftime("%d %b %Y - %I:%M %p UTC")
        }

        collection.insert_one(document)
    print("Webhook Triggered!")
    print(request.json)
    return jsonify({"status":"received"}),200

@app.route("/events", methods=["GET"])
def get_events():
    events=list(collection.find({},{"_id":0}).sort("_id",-1))
    return jsonify(events)

if __name__=="__main__":
    app.run(port=5000, debug=True)