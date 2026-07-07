"""
API Tool Module

Generic API caller (future MCP / server tool layer).
"""
import requests
from typing import Any, Dict, Optional

class APITool:
    """
    Generic API caller (future MCP / server tool layer)
    """

    def execute(self, url: str, method: str = "GET", payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute an HTTP request.
        
        Args:
            url (str): The URL to request.
            method (str): The HTTP method (e.g., GET, POST). Defaults to "GET".
            payload (Optional[Dict[str, Any]]): The JSON payload for POST requests.
            
        Returns:
            Dict[str, Any]: The execution result containing status code and response data.
        """
        try:
            if method.upper() == "GET":
                r = requests.get(url, timeout=10)
            else:
                r = requests.post(url, json=payload, timeout=10)

            content_type = r.headers.get("Content-Type", "")
            return {
                "status": r.status_code,
                "data": r.json() if content_type.startswith("application/json") else r.text
            }

        except Exception as e:
            return {"error": str(e)}