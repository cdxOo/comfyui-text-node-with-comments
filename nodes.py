from .remove_comments import remove_comments

class CDXOO_TextNodeWithComments:
    RETURN_TYPES = ("STRING",)
    CATEGORY = "primitives"
    FUNCTION = "get_sanitized_string"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING", { "default": "", "multiline": True })
            }
        }

    def get_sanitized_string(self, string):
        return (remove_comments(string),)

NODE_CLASS_MAPPINGS = {
    "text-node-with-comments": CDXOO_TextNodeWithComments
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "text-node-with-comments": "Text Node With Comments (@cdxoo)"
}

