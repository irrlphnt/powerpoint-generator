# PowerPoint Generator

A Python application that generates PowerPoint presentations based on user requirements.

## Project Structure

```
powerpoint-generator/
├── src/
│   ├── __init__.py
│   ├── presentation/
│   │   ├── __init__.py
│   │   ├── slide_generator.py
│   │   ├── template_manager.py
│   │   └── content_formatter.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── config/
│       ├── __init__.py
│       └── settings.py
├── templates/
│   └── base_templates/
├── tests/
│   └── __init__.py
├── requirements.txt
└── README.md
```

## Core Technologies

- Python
- `python-pptx` library for PowerPoint manipulation
- FastAPI/Flask (optional) for web interface

## Key Components

### Presentation Generator Core
- Template management system
- Slide generation engine
- Content formatting utilities
- Layout management

### Input Handling
- User requirement parser
- Configuration management
- Input validation

### Content Management
- Text processing
- Image handling
- Chart generation
- Style management

## Main Features
- Create presentations from templates
- Add/modify slides
- Insert and format text
- Handle images and charts
- Apply consistent styling
- Support custom themes
- Export to PPTX format

## Implementation Phases

### Phase 1: Core Setup
- Set up project structure
- Install dependencies
- Create basic class structure

### Phase 2: Basic Functionality
- Implement basic slide creation
- Add text manipulation
- Basic template management

### Phase 3: Advanced Features
- Image handling
- Chart generation
- Style customization
- Template system

### Phase 4: User Interface
- Command-line interface
- (Optional) Web interface
- Input validation
- Error handling

## Example Usage

```python
from presentation_generator import PresentationBuilder

# Create a new presentation
builder = PresentationBuilder()

# Configure presentation
builder.set_template("business")
builder.set_theme("modern")

# Add content
builder.add_title_slide("My Presentation", "By User")
builder.add_content_slide(
    title="Overview",
    content=["Point 1", "Point 2", "Point 3"],
    layout="bullet_list"
)

# Add image slide
builder.add_image_slide(
    title="Our Results",
    image_path="path/to/image.png",
    caption="Figure 1: Results Analysis"
)

# Generate the presentation
builder.save("output_presentation.pptx")
```

## Dependencies

```
python-pptx>=0.6.21
Pillow>=9.0.0  # for image handling
matplotlib>=3.5.0  # for chart generation
```

## Best Practices
- Use type hints for better code maintainability
- Implement comprehensive error handling
- Write unit tests for core functionality
- Use design patterns (Builder, Factory, etc.)
- Follow PEP 8 style guidelines
- Document code thoroughly 