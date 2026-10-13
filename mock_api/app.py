"""Mock API used to exercise Haystack change verification locally.

Run:  python mock_api/app.py            -> http://localhost:4010
Env:  PORT (default 4010), API_KEY (default "demo-key"), BROKEN=1 (simulate a regression)
"""
import json
import os

from flask import Flask, abort, jsonify, request

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY", "demo-key")
BROKEN = os.environ.get("BROKEN", "0") == "1"
_documents = {
    1: {"id": 1, "title": "Quarterly report"},
    2: {"id": 2, "title": "Meeting notes"},
}
_next_id = 3


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/openapi.json")
def openapi():
    path = os.path.join(os.path.dirname(__file__), "openapi.json")
    with open(path, encoding="utf-8") as handle:
        return jsonify(json.load(handle))


@app.get("/api/v1/documents")
def list_documents():
    items = list(_documents.values())
    return jsonify(items=items, count=len(items))


@app.get("/api/v1/documents/<int:doc_id>")
def get_document(doc_id):
    if BROKEN:
        abort(500, description="simulated failure")
    document = _documents.get(doc_id)
    if document is None:
        abort(404, description="document not found")
    return jsonify(document)


@app.post("/api/v1/documents")
def create_document():
    global _next_id
    payload = request.get_json(silent=True) or {}
    title = payload.get("title")
    if not title:
        abort(400, description="title is required")
    document = {"id": _next_id, "title": title}
    _documents[_next_id] = document
    _next_id += 1
    return jsonify(document), 201


@app.delete("/api/v1/documents/<int:doc_id>")
def delete_document(doc_id):
    if _documents.pop(doc_id, None) is None:
        abort(404, description="document not found")
    return jsonify(deleted=True)


@app.get("/api/v1/documents/<int:doc_id>/tags")
def document_tags(doc_id):
    if request.headers.get("X-API-Key") != API_KEY:
        abort(401, description="Missing or invalid API key")
    if doc_id not in _documents:
        abort(404, description="document not found")
    return jsonify(id=doc_id, tags=["finance", "draft"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "4010")))
