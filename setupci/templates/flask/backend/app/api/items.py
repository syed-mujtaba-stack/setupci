from flask import Blueprint, request, jsonify
from app import db
from app.models.item import Item

items_bp = Blueprint("items", __name__)

@items_bp.route("/", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

@items_bp.route("/", methods=["POST"])
def create_item():
    data = request.get_json() or {}
    if "title" not in data:
        return jsonify({"error": "title is required"}), 400
    
    item = Item(
        title=data["title"],
        description=data.get("description"),
        is_done=data.get("is_done", False)
    )
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@items_bp.route("/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify(item.to_dict())

@items_bp.route("/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.get_json() or {}
    
    if "title" in data:
        item.title = data["title"]
    if "description" in data:
        item.description = data["description"]
    if "is_done" in data:
        item.is_done = data["is_done"]
        
    db.session.commit()
    return jsonify(item.to_dict())

@items_bp.route("/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"})
