from presentation import PresentationBuilder

def create_sample_presentation():
    # Create a new presentation builder
    builder = PresentationBuilder()
    
    # Add title slide
    builder.add_title_slide(
        title="Sample Presentation",
        subtitle="Created with PowerPoint Generator"
    )
    
    # Add content slide
    builder.add_content_slide(
        title="Key Points",
        content=[
            "First important point",
            "Second important point",
            "Third important point"
        ]
    )
    
    # Add image slide (note: you'll need to provide a real image path)
    builder.add_image_slide(
        title="Sample Image",
        image_path="path/to/your/image.jpg",  # Replace with actual image path
        caption="Figure 1: Sample Image"
    )
    
    # Save the presentation
    builder.save("sample_presentation.pptx")
    print("Presentation created successfully!")

if __name__ == "__main__":
    create_sample_presentation() 