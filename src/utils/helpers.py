def format_slide_text(text: str) -> str:
    """Format text for a slide.

    Args:
        text: The text to format.

    Returns:
        The formatted text.
    """
    return text.strip()


def validate_image_path(path: str) -> bool:
    """Validate an image path.

    Args:
        path: The path to validate.

    Returns:
        True if the path is valid, False otherwise.
    """
    import os

    return os.path.exists(path) and os.path.isfile(path)


def create_bullet_points(items: list) -> list:
    """Create bullet points from a list of items.

    Args:
        items: The items to convert to bullet points.

    Returns:
        A list of bullet points.
    """
    return [f"• {item}" for item in items]
