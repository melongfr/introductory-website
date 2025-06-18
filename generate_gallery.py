# Python script to generate static HTML for Science Gallery
# Run this script to generate gallery.html with embedded images
# Save the output to gallery.html or copy the gallery-grid content

gallery_items = [
    {
        "src": "https://images.unsplash.com/photo-1576085898634-d0873a993e4b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        "alt": "Biology",
        "title": "Biology in Medicine",
        "desc": "Exploring human anatomy for surgical advancements."
    },
    {
        "src": "https://images.unsplash.com/photo-1554475900-0a0350e3fc7b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        "alt": "Chemistry",
        "title": "Chemistry in Medicine",
        "desc": "Studying molecular structures for drug development."
    },
    {
        "src": "https://images.unsplash.com/photo-1578496781985-452d4a934d43?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        "alt": "Physics",
        "title": "Physics in Medicine",
        "desc": "Applying imaging techniques like MRI for diagnostics."
    }
]

# Generate gallery HTML
gallery_html = '<div class="gallery-grid" id="gallery-grid">\n'
for item in gallery_items:
    gallery_html += f'''    <div class="gallery-card">
        <img src="{item['src']}" alt="{item['alt']}">
        <div class="gallery-info">
            <h3>{item['title']}</h3>
            <p>{item['desc']}</p>
        </div>
    </div>\n'''
gallery_html += '</div>'

# Full HTML for gallery.html
full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gallery - [Your Name]</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body class="light-mode">
    <!-- Navigation -->
    <nav id="nav">
        <div class="logo">[Your Name]</div>
        <div class="nav-links">
            <a href="index.html">Home</a>
            <a href="about.html">About</a>
            <a href="skills.html">Skills</a>
            <a href="gallery.html" class="active">Gallery</a>
            <a href="contact.html">Contact</a>
            <button class="theme-toggle" id="theme-toggle">☀️</button>
        </div>
    </nav>

    <!-- Science Gallery Section -->
    <section id="gallery" class="gallery">
        <h2>Science Gallery</h2>
        {gallery_html}
    </section>

    <!-- Footer -->
    <footer>
        <p>© 2025 [Your Name]. All rights reserved.</p>
    </footer>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
    <script src="script.js"></script>
</body>
</html>
'''

# Save to file
with open('gallery.html', 'w') as f:
    f.write(full_html)

print("gallery.html has been generated with static image content.")