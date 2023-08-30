from openai_integration import generate_response

def get_response_for_comment(comment):
    """
    Get AI-generated response for a given comment.
    """
    return generate_response(comment)
