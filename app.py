from flask import Flask, render_template, request, redirect, url_for, flash
from notion_client import Client

class NotionManager:
    def __init__(self, api_key):
        self.notion = Client(auth=api_key)
    
    def add_code_and_description(self, page_id, code_content, description):
        payload = {
            "children": [
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": description
                                }
                            }
                        ]
                    }
                },
                {
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": code_content
                                }
                            }
                        ],
                        "language": "python"
                    }
                }
            ]
        }
        try:
            self.notion.blocks.children.append(block_id=page_id, children=payload["children"])
        except Exception as e:
            raise e

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = "your_secret_key"
        self.notion_manager = None
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.route("/", methods=["GET", "POST"])
        def index():
            if request.method == "POST":
                api_key = request.form["api_key"]
                page_id = request.form["page_id"]
                code_content = request.form["code_content"]
                description = request.form["description"]
                if not self.notion_manager or self.notion_manager.notion.auth != api_key:
                    self.notion_manager = NotionManager(api_key)
                try:
                    self.notion_manager.add_code_and_description(page_id, code_content, description)
                    flash("Code and description added to Notion successfully!", "success")
                except Exception as e:
                    flash(f"Failed to add code and description to Notion: {str(e)}", "danger")
                return redirect(url_for("index"))
            return render_template("index.html")

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    flask_app = FlaskApp()
    flask_app.run()
