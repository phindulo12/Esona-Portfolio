// Initialize AOS (Animate on Scroll)
document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        duration: 1000,
        once: true,
        offset: 100
    });
    
    // Animate skill bars when they come into view
    animateSkillBars();
});

function animateSkillBars() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const skillBar = entry.target.querySelector('.skill-bar');
                if (skillBar && !skillBar.classList.contains('animated')) {
                    const width = skillBar.getAttribute('data-width');
                    skillBar.style.width = width + '%';
                    skillBar.classList.add('animated');
                }
            }
        });
    }, { threshold: 0.5 });
    
    document.querySelectorAll('.skill-item').forEach(item => {
        observer.observe(item);
    });
}
