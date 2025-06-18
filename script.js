// Navigation Scroll Effect with Parallax (disabled for homepage)
window.addEventListener('scroll', () => {
    const nav = document.getElementById('nav');
    if (window.scrollY > 50) {
        nav.style.transform = `translateY(0) scale(0.98)`;
        nav.style.boxShadow = '0 4px 15px rgba(0, 0, 0, 0.7)';
    } else {
        nav.style.transform = `translateY(0) scale(1)`;
        nav.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.5)';
    }
});

// Contact Form Submission Handler (contact.html)
function handleSubmit(event) {
    event.preventDefault();
    alert('Form submitted! (This is a demo, no actual submission.)');
    event.target.reset();
}