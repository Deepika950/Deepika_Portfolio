import re
import sys

def modify_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. New CSS Design (Professional Theme applied to original structure)
    new_style = """<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    /* Professional Tech Theme: Deep Blue and Emerald */
    --primary: #2563eb;       /* Royal Blue */
    --primary-light: #3b82f6;
    --secondary: #10b981;     /* Emerald Green */
    --dark: #0b1120;          /* Deep Slate Background */
    --dark-surface: rgba(30, 41, 59, 0.7); /* Glass surface */
    --light: #f8fafc;
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --accent: #0ea5e9;        /* Sky Blue */
    --gradient: linear-gradient(135deg, #2563eb 0%, #0ea5e9 100%);
    --gradient-success: linear-gradient(135deg, #059669 0%, #10b981 100%);
    --glass-border: 1px solid rgba(255, 255, 255, 0.08);
    --glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
}

* { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
body { background-color: var(--dark); color: var(--text-primary); line-height: 1.6; overflow-x: hidden; }
h1, h2, h3, h4, .logo { font-family: 'Outfit', sans-serif; }
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--dark); }
::-webkit-scrollbar-thumb { background: var(--primary); border-radius: 4px; }

.container { width: 90%; max-width: 1200px; margin: 0 auto; padding: 10px; }

/* Header */
header { background: rgba(11, 17, 32, 0.85); backdrop-filter: blur(12px); border-bottom: var(--glass-border); position: fixed; width: 100%; top: 0; z-index: 1000; transition: all 0.3s ease; }
.header-container { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; }
.logo { font-size: 1.6rem; font-weight: 800; color: white; letter-spacing: 0.5px; display: flex; align-items: center; gap: 10px;}
nav { display: flex; gap: 15px; }
nav a { color: var(--text-primary); text-decoration: none; font-weight: 500; font-size: 0.95rem; transition: all 0.3s ease; padding: 6px 12px; border-radius: 8px; position: relative;}
nav a:hover { color: var(--accent); background: rgba(255,255,255,0.05); }
.mobile-menu-btn { display: none; background: none; border: none; color: var(--text-primary); font-size: 1.5rem; cursor: pointer; }

/* Hero Section */
.hero { height: 100vh; display: flex; align-items: center; background: radial-gradient(circle at top right, rgba(37, 99, 235, 0.1), transparent 50%), var(--dark); position: relative; overflow: hidden; }
.hero::after { content: ''; position: absolute; width: 40vw; height: 40vw; background: radial-gradient(circle, rgba(16, 185, 129, 0.05) 0%, transparent 60%); bottom: -10%; left: -10%; animation: pulse 10s infinite alternate-reverse; pointer-events: none; }
@keyframes pulse { 0% { transform: scale(1); opacity: 0.5; } 100% { transform: scale(1.1); opacity: 0.8; } }

.hero-content { max-width: 900px; margin: 0 auto; text-align: center; position: relative; z-index: 2; padding-top: 60px; }

.hero-label { display: inline-block; padding: 6px 16px; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); color: var(--secondary); border-radius: 20px; font-size: 0.85rem; font-weight: 600; margin-bottom: 25px; letter-spacing: 1px; animation: slideUp 0.8s ease-out 0.2s both;}

.hero h1 { font-size: 4.5rem; font-weight: 800; margin-bottom: 10px; line-height: 1.1; color: white; animation: slideUp 0.8s ease-out 0.4s both;}

.hero h2 { font-size: 2.2rem; font-weight: 500; color: var(--text-secondary); margin-bottom: 25px; height: 50px; animation: slideUp 0.8s ease-out 0.6s both;}
.typing-text { background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 700; border-right: 3px solid var(--accent); white-space: nowrap; overflow: hidden; padding-right: 5px; animation: blinkCursor 0.75s step-end infinite;}

@keyframes blinkCursor { from, to { border-color: transparent } 50% { border-color: var(--accent); } }
@keyframes slideUp { 0% { opacity: 0; transform: translateY(30px); } 100% { opacity: 1; transform: translateY(0); } }

.hero p { font-size: 1.15rem; color: var(--text-secondary); margin-bottom: 40px; max-width: 700px; margin-left: auto; margin-right: auto; line-height: 1.6; animation: slideUp 0.8s ease-out 0.8s both; }

.hero-btns { display: flex; justify-content: center; gap: 20px; animation: slideUp 0.8s ease-out 1s both; }
.btn { display: inline-flex; align-items: center; justify-content: center; padding: 14px 32px; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 1rem; transition: all 0.3s ease; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
.btn-primary { background: var(--primary); color: white; border: 1px solid var(--primary-light); }
.btn-primary:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(37, 99, 235, 0.4); background: var(--primary-light); }
.btn-outline { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.15); color: var(--text-primary); }
.btn-outline:hover { background: rgba(255, 255, 255, 0.1); border-color: rgba(255, 255, 255, 0.3); transform: translateY(-3px); }

/* Global Sections */
section { padding: 80px 0; position: relative; }
.section-title { text-align: center; margin-bottom: 50px; position: relative; }
.section-title h2 { font-size: 2.5rem; color: var(--text-primary); display: inline-block; position: relative; font-weight: 700;}
.section-title h2::after { content: ''; position: absolute; width: 60px; height: 4px; background: var(--primary); bottom: -12px; left: 50%; transform: translateX(-50%); border-radius: 2px; }

/* About Section */
.about-section { background: rgba(15, 23, 42, 0.4); border-top: 1px solid rgba(255,255,255,0.02); }
.about-content { display: flex; align-items: center; gap: 50px; background: var(--dark-surface); backdrop-filter: blur(16px); border: var(--glass-border); box-shadow: var(--glass-shadow); padding: 40px; border-radius: 20px; }
.profile-img { width: 250px; height: 250px; border-radius: 20px; object-fit: cover; box-shadow: 0 10px 30px rgba(0,0,0,0.4); transform: rotate(-3deg); transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.about-content:hover .profile-img { transform: rotate(0) scale(1.05); box-shadow: 0 15px 40px rgba(37, 99, 235, 0.3); }
.about-text h2 { font-size: 2rem; margin-bottom: 15px; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.about-text p { margin-bottom: 15px; font-size: 1.05rem; color: var(--text-secondary); line-height: 1.7; }

/* Education Section */
.education-section { background: var(--dark); }
.timeline { position: relative; max-width: 800px; margin: 0 auto; }
.timeline::after { content: ''; position: absolute; width: 2px; background: linear-gradient(to bottom, transparent, var(--primary), transparent); top: 0; bottom: 0; left: 50%; transform: translateX(-50%); border-radius: 2px; }
.education-item { padding: 25px; position: relative; background: var(--dark-surface); backdrop-filter: blur(12px); border: var(--glass-border); width: calc(50% - 30px); border-radius: 16px; margin-bottom: 30px; box-shadow: var(--glass-shadow); transition: all 0.4s ease; transform-origin: center; }
.education-item:hover { transform: translateY(-5px) scale(1.02); box-shadow: 0 12px 30px rgba(0,0,0,0.5); border-color: rgba(37, 99, 235, 0.5); }
.education-item::after { content: ''; position: absolute; width: 16px; height: 16px; background: var(--dark); border: 4px solid var(--primary); border-radius: 50%; top: 50%; transform: translateY(-50%); z-index: 1; box-shadow: 0 0 10px var(--primary); transition: all 0.3s ease; }
.education-item:hover::after { background: var(--primary); box-shadow: 0 0 20px var(--primary); transform: translateY(-50%) scale(1.2); }
.left { left: 0; }
.right { left: calc(50% + 30px); }
.left::after { right: -42px; }
.right::after { left: -42px; }
.education-item h3 { color: var(--text-primary); font-size: 1.3rem; margin-bottom: 8px; }
.education-item p { color: var(--text-secondary); margin-bottom: 5px; font-size: 0.95rem; }
.education-item span { color: var(--primary-light); font-weight: 500; display: block; margin-top: 5px; font-size: 0.9rem; }
.percentage { display: inline-block; background: rgba(37, 99, 235, 0.15); color: #60a5fa; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600 !important; margin-top: 10px; border: 1px solid rgba(37, 99, 235, 0.3); }

/* Skills */
.skills-section { background: rgba(15, 23, 42, 0.4); }
.skills-container { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; }
.skill-category { background: var(--dark-surface); backdrop-filter: blur(12px); padding: 30px; border-radius: 16px; border: var(--glass-border); box-shadow: var(--glass-shadow); transition: all 0.3s ease; }
.skill-category:hover { transform: translateY(-8px); border-color: rgba(37, 99, 235, 0.4); box-shadow: 0 15px 35px rgba(0,0,0,0.4); }
.skill-category h3 { color: var(--primary-light); margin-bottom: 25px; font-size: 1.3rem; display: flex; align-items: center; gap: 10px; }
.skill-item { margin-bottom: 20px; }
.skill-info { display: flex; justify-content: space-between; margin-bottom: 8px; font-weight: 500; color: var(--text-secondary); font-size: 0.9rem; }
.skill-bar { height: 6px; background: rgba(255, 255, 255, 0.05); border-radius: 3px; overflow: hidden; }
.skill-progress { height: 100%; background: var(--gradient); border-radius: 3px; width: 0; transition: width 1.5s ease-out; }

/* Projects */
.projects-section { background: var(--dark); }
.projects-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 30px; }
.project-card { background: var(--dark-surface); border: var(--glass-border); border-radius: 16px; overflow: hidden; transition: all 0.4s ease; display: flex; flex-direction: column; }
.project-card:hover { transform: translateY(-10px); border-color: rgba(37, 99, 235, 0.3); box-shadow: 0 20px 40px rgba(0,0,0,0.5); }
.project-img { width: 100%; height: 200px; object-fit: cover; transition: transform 0.6s ease; }
.project-card:hover .project-img { transform: scale(1.05); filter: brightness(1.1); }
.project-content { padding: 30px; flex-grow: 1; display: flex; flex-direction: column; }
.project-content h3 { font-size: 1.3rem; color: var(--text-primary); margin-bottom: 12px; font-weight: 600;}
.project-content p { color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 20px; flex-grow: 1; line-height: 1.6; }
.project-tech { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 25px; }
.tech-tag { background: rgba(255,255,255,0.05); color: var(--text-primary); padding: 4px 12px; border-radius: 6px; font-size: 0.8rem; font-weight: 500;}
.project-links { display: flex; gap: 15px; }
.project-link { display: inline-flex; align-items: center; color: var(--text-primary); text-decoration: none; font-weight: 500; font-size: 0.9rem; transition: all 0.3s ease; background: rgba(255,255,255,0.05); padding: 8px 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);}
.project-link i { margin-left: 6px; }
.project-link:hover { color: white; background: var(--primary); transform: translateY(-2px); border-color: var(--primary-light);}

/* Achievements/Certifications Original Structure (Untouched HTML) with New Styling */
.achievements-section { background: rgba(15, 23, 42, 0.4); overflow: hidden; }
.achievements-section .section-title h2 { color: var(--text-primary); }
.certificates-carousel { position: relative; max-width: 1200px; margin: 40px auto; padding: 0 50px; }
.certificates-track { display: flex; transition: transform 0.5s ease; gap: 30px; padding: 20px 0; }
.certificate-card { position: relative; min-width: calc(33.333% - 20px); height: 400px; perspective: 1000px; cursor: pointer; border-radius: 12px; flex-shrink: 0; box-shadow: var(--glass-shadow); transition: all 0.3s ease; }
.certificate-card.active { transform: scale(1.05); z-index: 2; box-shadow: 0 15px 40px rgba(0,0,0,0.5); border: 1px solid rgba(37, 99, 235, 0.4); }
.certificate-front, .certificate-back { position: absolute; width: 100%; height: 100%; backface-visibility: hidden; transition: transform 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275); border-radius: 12px; padding: 30px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: var(--dark-surface); backdrop-filter: blur(12px); border: var(--glass-border); }
.certificate-front { transform: rotateY(0deg); }
.certificate-back { transform: rotateY(180deg); background: rgba(30, 41, 59, 0.95); padding: 20px;}
.certificate-card.flipped .certificate-front { transform: rotateY(180deg); }
.certificate-card.flipped .certificate-back { transform: rotateY(360deg); }
.certificate-badge { width: 70px; height: 70px; background: rgba(37, 99, 235, 0.1); color: var(--primary-light); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 30px; margin-bottom: 20px; transition: 0.3s;}
.certificate-card:hover .certificate-badge { transform: scale(1.1); background: rgba(37, 99, 235, 0.2); }
.certificate-front h3 { color: var(--text-primary); font-size: 1.2rem; margin-bottom: 10px; text-align: center; font-weight: 600; }
.certificate-front p { color: var(--text-secondary); margin-bottom: 20px; font-size: 0.95rem; text-align: center; }
.view-btn { background: rgba(255,255,255,0.05); color: var(--text-primary); padding: 8px 20px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); font-weight: 500; font-size: 0.9rem; transition: 0.3s; }
.certificate-front:hover .view-btn { background: var(--primary); border-color: var(--primary-light); color: white;}
.certificate-back img { width: 100%; height: auto; max-height: 250px; object-fit: contain; border-radius: 8px; margin-bottom: 20px; border: 1px solid rgba(255,255,255,0.1);}
.carousel-btn { position: absolute; top: 50%; transform: translateY(-50%); width: 45px; height: 45px; background: rgba(30, 41, 59, 0.8); border: var(--glass-border); color: var(--text-primary); border-radius: 50%; font-size: 1.2rem; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; transition: 0.3s; }
.carousel-btn:hover { background: var(--primary); color: white; }
.prev-btn { left: 0; }
.next-btn { right: 0; }
.certificate-actions { display: flex; gap: 10px;}
.zoom-btn { background: rgba(255,255,255,0.1); color: white; border: 1px solid rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 8px; display:flex; align-items:center; gap: 8px; text-decoration: none; font-size: 0.9rem; transition: 0.3s; cursor: pointer;}
.zoom-btn:hover { background: var(--primary); border-color: var(--primary-light); }
.multi-certificates { height: 240px; overflow-y: auto; padding-right: 10px; width: 100%; }
.certificate-scroll-container { display: flex; flex-direction: column; gap: 15px; }
.certificate-item { background: rgba(0,0,0,0.2); padding: 15px; border-radius: 8px; border-left: 4px solid var(--primary-light); }
.certificate-item h4 { margin: 0 0 8px 0; color: var(--text-primary); font-size: 0.9rem; }
.certificate-item p { color: var(--text-secondary); font-size: 0.8rem; margin: 0 0 8px 0;}
.certificate-item img { width: 100%; height: auto; border-radius: 4px; border: 1px solid rgba(255,255,255,0.1); }

/* Modal Styles */
.modal { display: none; position: fixed; z-index: 10000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(11, 17, 32, 0.9); backdrop-filter: blur(10px);}
.modal-content { margin: auto; display: block; width: 90%; max-width: 1000px; padding: 30px; background: var(--dark-surface); border: var(--glass-border); border-radius: 16px; position: relative; top: 50%; transform: translateY(-50%); max-height: 90vh; overflow-y: auto; }
.close-modal { position: absolute; top: 15px; right: 25px; color: var(--text-secondary); font-size: 35px; font-weight: bold; cursor: pointer; transition: 0.3s;}
.close-modal:hover { color: white; transform: rotate(90deg);}
.certificate-gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; padding: 20px 0; }
.certificate-gallery img { width: 100%; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; transition: transform 0.3s; }
.certificate-gallery img:hover { transform: scale(1.03); border-color: var(--primary-light);}
.gallery-certificate h4 { margin-bottom: 15px; color: var(--text-primary); text-align: center;}

/* Contact Section */
.contact-container { display: grid; grid-template-columns: 1fr 1.5fr; gap: 40px; }
.contact-info, .contact-form { background: var(--dark-surface); padding: 40px; border-radius: 16px; border: var(--glass-border); }
.contact-info h3, .contact-form h3 { font-size: 1.6rem; margin-bottom: 25px; color: var(--text-primary); }
.contact-detail { display: flex; align-items: center; margin-bottom: 25px; }
.contact-detail i { width: 45px; height: 45px; background: rgba(37, 99, 235, 0.1); border: 1px solid rgba(37, 99, 235, 0.2); color: var(--primary-light); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; margin-right: 15px; transition: 0.3s;}
.contact-detail:hover i { background: var(--primary); color: white;}
.form-group { margin-bottom: 20px; }
.form-group label { display: block; margin-bottom: 8px; font-weight: 500; color: var(--text-secondary); font-size: 0.95rem;}
.form-control { width: 100%; padding: 14px 18px; background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; font-size: 0.95rem; color: white; transition: all 0.3s ease; }
.form-control:focus { border-color: var(--primary-light); background: rgba(0, 0, 0, 0.4); outline: none; }
textarea.form-control { min-height: 150px; resize: vertical; }
.submit-btn { background: var(--primary); color: white; padding: 14px 30px; border: none; border-radius: 8px; cursor: pointer; font-size: 1rem; font-weight: 600; transition: all 0.3s ease; width: 100%; display: flex; justify-content:center; gap: 8px; align-items: center;}
.submit-btn:hover { background: var(--primary-light); transform: translateY(-3px); box-shadow: 0 8px 20px rgba(37, 99, 235, 0.4); }

/* Footer */
footer { background: var(--dark); padding: 40px 0; text-align: center; border-top: 1px solid rgba(255,255,255,0.05);}
.social-links { display: flex; justify-content: center; gap: 15px; margin-bottom: 20px; }
.social-link { width: 45px; height: 45px; background: rgba(255,255,255,0.05); color: var(--text-primary); font-size: 1.2rem; display: flex; align-items: center; justify-content: center; border-radius: 50%; transition: all 0.3s ease; text-decoration: none;}
.social-link:hover { background: var(--primary); color: white; transform: translateY(-5px); box-shadow: 0 5px 15px rgba(37, 99, 235, 0.3);}
.copyright { font-size: 0.9rem; color: var(--text-secondary); }

/* Utilities & Animations */
.reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s cubic-bezier(0.5, 0, 0, 1); }
.reveal.active { opacity: 1; transform: translateY(0); }

.back-to-top { position: fixed; bottom: 30px; right: 30px; width: 45px; height: 45px; background: var(--primary); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; cursor: pointer; opacity: 0; visibility: hidden; transition: all 0.3s ease; z-index: 999; box-shadow: 0 5px 15px rgba(0,0,0,0.3); }
.back-to-top.active { opacity: 1; visibility: visible; }
.back-to-top:hover { transform: translateY(-5px); background: var(--primary-light); }

/* Responsive Adjustments */
@media (max-width: 992px) {
    .about-content { flex-direction: column; text-align: center; padding: 30px; }
    .timeline::after { left: 40px; }
    .education-item { width: 100%; padding-left: 70px; padding-right: 25px; margin-bottom: 25px;}
    .education-item::after { left: 32px; }
    .left::after, .right::after { left: 32px; right: auto; }
    .right { left: 0; }
    .contact-container { grid-template-columns: 1fr; }
    .certificate-card { min-width: calc(50% - 15px); }
}
@media (max-width: 768px) {
    nav { display: none; position: absolute; top: 100%; left: 0; width: 100%; background: var(--dark); flex-direction: column; padding: 20px; gap: 15px; border-bottom: 1px solid rgba(255,255,255,0.1); }
    nav.active { display: flex; }
    .mobile-menu-btn { display: block; }
    .projects-grid { grid-template-columns: 1fr; }
    .hero h1 { font-size: 3rem; }
    .hero h2 { font-size: 1.5rem; height: auto; }
    .hero-btns { flex-direction: column; width: 100%; }
    .btn { width: 100%; }
    .certificate-card { min-width: 100%; }
    section { padding: 60px 0; }
}
</style>"""

    # Replace <style>
    content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)

    # 2. Modify Hero Section HTML dynamically without breaking structure
    new_hero_content = """<div class="hero-content">
                <span class="hero-label"><i class="fas fa-circle" style="font-size: 10px; margin-right: 5px; color: #10b981;"></i> Actively Seeking Opportunities</span>
                <h1>Deepika Enaganoori</h1>
                <h2><span class="typing-text">Software Developer.</span></h2>
                <p>A passionate B.Tech final-year student specializing in AI and Full Stack Development. I design and build production-ready applications using Django, React, and Python, combining robust backend architecture with intuitive user experiences.</p>
                <div class="hero-btns">
                    <a href="#projects" class="btn btn-primary">View My Work</a>
                    <a href="#contact" class="btn btn-outline">Hire Me</a>
                </div>
            </div>"""
    content = re.sub(r'<div class="hero-content">.*?</div>\s*</div>\s*</section>', new_hero_content + '\n        </div>\n    </section>', content, flags=re.DOTALL)

    # 3. Add 'reveal' classes to major elements
    content = content.replace('<div class="about-content">', '<div class="about-content reveal">')
    content = content.replace('<div class="education-item', '<div class="education-item reveal')
    content = content.replace('<div class="skill-category">', '<div class="skill-category reveal">')
    content = content.replace('<div class="project-card">', '<div class="project-card reveal">')
    content = content.replace('<div class="contact-info">', '<div class="contact-info reveal">')
    content = content.replace('<div class="contact-form">', '<div class="contact-form reveal">')
    
    # 4. Inject updated JavaScript (Includes Typing Effect, Staggered Reveal, etc.)
    new_script = """<script>
    document.addEventListener('DOMContentLoaded', function() {
        
        // Mobile Menu
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mainNav = document.getElementById('main-nav');
        if (mobileMenuBtn && mainNav) {
            mobileMenuBtn.addEventListener('click', () => mainNav.classList.toggle('active'));
        }
        
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                if (!targetId || targetId === '#') return;
                const target = document.querySelector(targetId);
                if (target) {
                    window.scrollTo({ top: target.offsetTop - 70, behavior: 'smooth' });
                    if (mainNav) mainNav.classList.remove('active');
                }
            });
        });
        
        // Back to top
        const backBtn = document.getElementById('back-to-top');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) backBtn.classList.add('active');
            else backBtn.classList.remove('active');
        });
        if(backBtn) backBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

        // Typing effect logic
        const roles = ["Software Developer.", "Full Stack Engineer.", "Django Specialist.", "Problem Solver."];
        let roleIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        const typingEl = document.querySelector('.typing-text');
        
        if (typingEl) {
            function typeEffect() {
                const currentRole = roles[roleIndex];
                
                if (isDeleting) {
                    typingEl.textContent = currentRole.substring(0, charIndex - 1);
                    charIndex--;
                } else {
                    typingEl.textContent = currentRole.substring(0, charIndex + 1);
                    charIndex++;
                }
                
                let typeSpeed = isDeleting ? 50 : 100;
                
                if (!isDeleting && charIndex === currentRole.length) {
                    typeSpeed = 2000;
                    isDeleting = true;
                } else if (isDeleting && charIndex === 0) {
                    isDeleting = false;
                    roleIndex = (roleIndex + 1) % roles.length;
                    typeSpeed = 500;
                }
                setTimeout(typeEffect, typeSpeed);
            }
            setTimeout(typeEffect, 1500);
        }

        // Scroll Reveal & Skill Bars Animations
        const revealElements = document.querySelectorAll('.reveal');
        const revealOptions = { threshold: 0.15, rootMargin: "0px 0px -20px 0px" };
        const revealOnScroll = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    
                    // Specific logic for skill bars
                    if (entry.target.classList.contains('skill-category')) {
                        const bars = entry.target.querySelectorAll('.skill-progress');
                        bars.forEach(bar => {
                            const widthText = bar.parentElement.previousElementSibling.lastElementChild.textContent;
                            bar.style.width = widthText;
                        });
                    }
                    observer.unobserve(entry.target);
                }
            });
        }, revealOptions);
        
        revealElements.forEach(el => revealOnScroll.observe(el));
        
        // --- PRESERVED ORIGINAL CERTIFICATE CAROUSEL LOGIC ---
        const track = document.querySelector('.certificates-track');
        const cards = document.querySelectorAll('.certificate-card');
        const prevBtn = document.querySelector('.prev-btn');
        const nextBtn = document.querySelector('.next-btn');
        const dotsContainer = document.querySelector('.carousel-dots');
        
        if (track && cards.length > 0) {
            let currentIndex = 0;
            const gap = 30; // Matches CSS
            
            if (dotsContainer) {
                cards.forEach((_, index) => {
                    const dot = document.createElement('div');
                    dot.classList.add('dot');
                    if (index === 0) dot.classList.add('active');
                    dot.addEventListener('click', () => goToSlide(index));
                    dotsContainer.appendChild(dot);
                });
            }
            
            function updateCarousel() {
                const cardWidth = cards[0].offsetWidth;
                const offset = -currentIndex * (cardWidth + gap);
                track.style.transform = `translateX(${offset}px)`;
                
                cards.forEach((card, index) => {
                    card.classList.toggle('active', index === currentIndex);
                });
                
                if (dotsContainer) {
                    document.querySelectorAll('.dot').forEach((dot, index) => {
                        dot.classList.toggle('active', index === currentIndex);
                    });
                }
            }
            
            function goToSlide(index) {
                currentIndex = Math.max(0, Math.min(index, cards.length - 1));
                updateCarousel();
            }
            
            function nextSlide() {
                if (currentIndex < cards.length - 1) { currentIndex++; updateCarousel(); }
            }
            
            function prevSlide() {
                if (currentIndex > 0) { currentIndex--; updateCarousel(); }
            }
            
            cards.forEach(card => {
                card.addEventListener('click', function(e) {
                    if (e.target.closest('a') || e.target.closest('button')) return;
                    if (this.classList.contains('active')) {
                        this.classList.toggle('flipped');
                    } else {
                        goToSlide(Array.from(cards).indexOf(this));
                    }
                });
            });
            
            if(nextBtn) nextBtn.addEventListener('click', nextSlide);
            if(prevBtn) prevBtn.addEventListener('click', prevSlide);
            
            let slideInterval = setInterval(() => { if (currentIndex < cards.length - 1) { nextSlide(); } else { goToSlide(0); } }, 5000);
            track.addEventListener('mouseenter', () => clearInterval(slideInterval));
            track.addEventListener('mouseleave', () => slideInterval = setInterval(() => { if (currentIndex < cards.length - 1) { nextSlide(); } else { goToSlide(0); } }, 5000));
            
            window.addEventListener('resize', updateCarousel);
            updateCarousel();
        }

        // Original Modal logic
        const modal = document.getElementById('certificatesModal');
        const closeBtn = document.querySelector('.close-modal');
        const viewAllBtns = document.querySelectorAll('.view-all-btn');
        
        if(modal) {
            viewAllBtns.forEach(btn => {
                btn.addEventListener('click', function(e) {
                    e.stopPropagation(); 
                    const card = this.closest('.certificate-card');
                    const certificates = card.querySelectorAll('.certificate-item');
                    const gallery = modal.querySelector('.certificate-gallery');
                    
                    if(gallery) {
                        gallery.innerHTML = '';
                        certificates.forEach(cert => {
                            const img = cert.querySelector('img');
                            const title = cert.querySelector('h4');
                            
                            const certElement = document.createElement('div');
                            certElement.className = 'gallery-certificate';
                            certElement.innerHTML = `<h4>${title.textContent}</h4><img src="${img.dataset.full || img.src}" alt="${img.alt}">`;
                            gallery.appendChild(certElement);
                        });
                    }
                    modal.style.display = 'block';
                });
            });
            if (closeBtn) closeBtn.addEventListener('click', () => modal.style.display = 'none');
            window.addEventListener('click', event => { if (event.target === modal) modal.style.display = 'none'; });
        }
    });
    </script>"""

    # Inject the script by replacing the existing script block
    content = re.sub(r'<script>.*?</script>', new_script, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    modify_html(sys.argv[1])
