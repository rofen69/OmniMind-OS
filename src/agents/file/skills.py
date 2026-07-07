"""
File Skills Module

Reusable functions for the File Agent.
"""
import os


def save_to_disk(filename: str, content: str) -> str:
    """
    Save content to a local file inside a workspace directory.

    Args:
        filename (str): The name of the file to create.
        content (str): The text content to write.

    Returns:
        str: A status message indicating success or failure.
    """
    workspace_dir = "workspace"
    
    # Create the workspace directory if it doesn't exist
    if not os.path.exists(workspace_dir):
        os.makedirs(workspace_dir)
        
    filepath = os.path.join(workspace_dir, filename)
    
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully saved to {filepath}"
    except Exception as e:
        return f"Failed to save file: {str(e)}"
