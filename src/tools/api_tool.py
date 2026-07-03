import requests

class APITool:
    """
    Generic API caller (future MCP / server tool layer)
    """

    def execute(self, url: str, method="GET", payload=None):
        try:
            if method == "GET":
                r = requests.get(url)
            else:
                r = requests.post(url, json=payload)

            return {
                "status": r.status_code,
                "data": r.json() if "json" in r.headers.get("Content-Type", "") else r.text
            }

        except Exception as e:
            return {"error": str(e)}