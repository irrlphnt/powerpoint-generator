from pathlib import Path
from typing import Dict, Any

# Base paths
BASE_DIR = Path(__file__).parent.parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
BASE_TEMPLATES_DIR = TEMPLATES_DIR / "base_templates"

# Default presentation settings
DEFAULT_SETTINGS: Dict[str, Any] = {
    "slide_width": 10,  # inches
    "slide_height": 7.5,  # inches
    "title_font_size": 44,  # points
    "content_font_size": 32,  # points
    "bullet_font_size": 28,  # points
    "default_template": "default",
    "default_theme": "modern",
}

# Available slide layouts
SLIDE_LAYOUTS = {
    "title": 0,
    "title_and_content": 1,
    "section_header": 2,
    "two_content": 3,
    "comparison": 4,
    "title_only": 5,
    "blank": 6,
    "content_with_caption": 7,
    "picture_with_caption": 8,
}

# Color themes
COLOR_THEMES = {
    "modern": {
        "primary": (0, 112, 192),  # RGB
        "secondary": (112, 173, 71),
        "accent": (255, 192, 0),
        "background": (255, 255, 255),
        "text": (0, 0, 0),
    },
    "classic": {
        "primary": (0, 0, 0),
        "secondary": (128, 128, 128),
        "accent": (192, 192, 192),
        "background": (255, 255, 255),
        "text": (0, 0, 0),
    },
}
