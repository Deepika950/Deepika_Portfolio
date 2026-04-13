import re
import sys

def modify_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to carefully replace the existing <style> block, or just the whole <head> content.
    # It's safer to extract from <head> to </style> and replace everything after "<head>" up to "</style>".
    
    # 1. New CSS Design (Enhanced for animations, lowered spacing)
    new_style = """<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

:root {
    --primary: #8b5cf6;
    --secondary: #3b82f6;
    --dark: #0f172a;
    --dark-surface: rgba(30, 41, 59, 0.7);
    --light: #f8fafc;
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;
    --accent: #ec4899;
    --gradient: linear-gradient(135deg, #8b5cf6 0%, #3b82f6 100%);
    --gradient-hover: linear-gradient(135deg, #a78bfa 0%, #60a5fa 100%);
    --glass-border: 1px solid rgba(255, 255, 255, 0.1);
    --glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}

* { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
body { background-color: var(--dark); color: var(--text-primary); line-height: 1.6; overflow-x: hidden; }
h1, h2, h3, h4, .logo { font-family: 'Outfit', sans-serif; }
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--dark); }
::-webkit-scrollbar-thumb { background: var(--primary); border-radius: 4px; }

.container { width: 90%; max-width: 1200px; margin: 0 auto; padding: 10px; }

/* Header */
header { background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(12px); border-bottom: var(--glass-border); position: fixed; width: 100%; top: 0; z-index: 1000; transition: all 0.3s ease; }
.header-container { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; }
.logo { font-size: 1.6rem; font-weight: 700; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: 1px; }
nav { display: flex; gap: 15px; }
nav a { color: var(--text-primary); text-decoration: none; font-weight: 500; font-size: 0.95rem; transition: all 0.3s ease; padding: 6px 12px; border-radius: 20px; position: relative;}
nav a::after { content: ''; position: absolute; width: 0; height: 2px; bottom: 0; left: 50%; background: var(--gradient); transition: all 0.3s ease; transform: translateX(-50%); border-radius: 2px; }
nav a:hover::after { width: 80%; }
nav a:hover { color: var(--primary); }
.mobile-menu-btn { display: none; background: none; border: none; color: var(--text-primary); font-size: 1.5rem; cursor: pointer; }

/* Hero Section */
.hero { height: 100vh; display: flex; align-items: center; background: var(--dark); position: relative; overflow: hidden; }
.hero::before { content: ''; position: absolute; width: 60vw; height: 60vw; background: radial-gradient(circle, rgba(139, 92, 246, 0.2) 0%, transparent 70%); top: -20%; right: -20%; animation: pulse 8s infinite alternate; pointer-events: none;}
.hero::after { content: ''; position: absolute; width: 50vw; height: 50vw; background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, transparent 70%); bottom: -20%; left: -20%; animation: pulse 10s infinite alternate-reverse; pointer-events: none; }
@keyframes pulse { 0% { transform: scale(1); opacity: 0.5; } 100% { transform: scale(1.1); opacity: 0.8; } }

.hero-content { max-width: 800px; margin: 0 auto; text-align: center; position: relative; z-index: 2; padding-top: 60px; }

/* Animated Typewriter Name */
.hero h1 { 
    font-size: 4rem; 
    font-weight: 700; 
    margin-bottom: 20px; 
    line-height: 1.2; 
    color: transparent;
    background: linear-gradient(to right, #4facfe 0%, #00f2fe 50%, #f093fb 100%);
    -webkit-background-clip: text;
    background-clip: text;
    background-size: 200% auto;
    animation: shine 4s linear infinite;
    display: inline-block;
}

@keyframes shine {
    to { background-position: 200% center; }
}

.hero p { font-size: 1.2rem; color: var(--text-secondary); margin-bottom: 30px; animation: slideUp 1s ease-out 0.5s both; }

@keyframes slideUp { 0% { opacity: 0; transform: translateY(30px); } 100% { opacity: 1; transform: translateY(0); } }

.hero-btns { display: flex; justify-content: center; gap: 15px; animation: slideUp 1s ease-out 0.8s both; }
.btn { display: inline-flex; align-items: center; justify-content: center; padding: 12px 28px; border-radius: 30px; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); letter-spacing: 0.5px; overflow: hidden; position: relative; z-index: 1;}
.btn::before { content: ''; position: absolute; top: 0; left: 0; width: 0; height: 100%; background: rgba(255,255,255,0.2); transition: all 0.4s ease; z-index: -1; }
.btn:hover::before { width: 100%; }
.btn-primary { background: var(--gradient); color: white; box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4); border: none; }
.btn-primary:hover { transform: translateY(-3px) scale(1.02); box-shadow: 0 8px 25px rgba(139, 92, 246, 0.6); }
.btn-outline { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2); color: var(--text-primary); }
.btn-outline:hover { background: rgba(255, 255, 255, 0.1); border-color: rgba(255, 255, 255, 0.4); transform: translateY(-3px); }

/* Sections - Reduced Spacing */
section { padding: 60px 0; position: relative; }
.section-title { text-align: center; margin-bottom: 40px; }
.section-title h2 { font-size: 2.5rem; color: var(--text-primary); display: inline-block; position: relative; }
.section-title h2::after { content: ''; position: absolute; width: 60%; height: 3px; background: var(--gradient); bottom: -10px; left: 20%; border-radius: 2px; }

/* About */
.about-section { background: var(--dark); padding-top: 80px; }
.about-content { display: flex; align-items: center; gap: 40px; background: var(--dark-surface); backdrop-filter: blur(16px); border: var(--glass-border); box-shadow: var(--glass-shadow); padding: 30px; border-radius: 20px; }
.profile-img { width: 220px; height: 220px; border-radius: 20px; object-fit: cover; box-shadow: 0 10px 30px rgba(0,0,0,0.4); transform: rotate(-3deg); transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.about-content:hover .profile-img { transform: rotate(0) scale(1.05); box-shadow: 0 15px 40px rgba(139, 92, 246, 0.3); }
.about-text h2 { font-size: 2rem; margin-bottom: 15px; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.about-text p { margin-bottom: 15px; font-size: 1.05rem; color: var(--text-secondary); }

/* Education */
.education-section { background: rgba(15, 23, 42, 0.4); }
.timeline { position: relative; max-width: 800px; margin: 0 auto; }
.timeline::after { content: ''; position: absolute; width: 2px; background: linear-gradient(to bottom, transparent, var(--primary), transparent); top: 0; bottom: 0; left: 50%; transform: translateX(-50%); border-radius: 2px; }
.education-item { padding: 25px; position: relative; background: var(--dark-surface); backdrop-filter: blur(12px); border: var(--glass-border); width: calc(50% - 30px); border-radius: 16px; margin-bottom: 30px; box-shadow: var(--glass-shadow); transition: all 0.4s ease; transform-origin: center; }
.education-item:hover { transform: translateY(-5px) scale(1.02); box-shadow: 0 12px 30px rgba(0,0,0,0.5); border-color: rgba(139, 92, 246, 0.5); }
.education-item::after { content: ''; position: absolute; width: 16px; height: 16px; background: var(--dark); border: 4px solid var(--primary); border-radius: 50%; top: 50%; transform: translateY(-50%); z-index: 1; box-shadow: 0 0 10px var(--primary); transition: all 0.3s ease; }
.education-item:hover::after { background: var(--primary); box-shadow: 0 0 20px var(--primary); transform: translateY(-50%) scale(1.2); }
.left { left: 0; }
.right { left: calc(50% + 30px); }
.left::after { right: -42px; }
.right::after { left: -42px; }
.education-item h3 { color: var(--text-primary); font-size: 1.3rem; margin-bottom: 8px; }
.education-item p { color: var(--text-secondary); margin-bottom: 5px; font-size: 0.95rem; }
.education-item span { color: var(--secondary); font-weight: 500; display: block; margin-top: 5px; font-size: 0.9rem; }
.percentage { display: inline-block; background: rgba(139, 92, 246, 0.15); color: #a78bfa; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600 !important; margin-top: 10px; border: 1px solid rgba(139, 92, 246, 0.3); }

/* Skills */
.skills-container { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px; }
.skill-category { background: var(--dark-surface); backdrop-filter: blur(12px); padding: 30px 25px; border-radius: 16px; border: var(--glass-border); box-shadow: var(--glass-shadow); transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); position: relative; overflow: hidden; }
.skill-category::before { content: ''; position: absolute; top: 0; left: -100%; width: 50%; height: 100%; background: linear-gradient(to right, transparent, rgba(255,255,255,0.05), transparent); transform: skewX(-20deg); transition: 0.5s; pointer-events: none; }
.skill-category:hover::before { left: 150%; }
.skill-category:hover { transform: translateY(-8px); border-color: rgba(139, 92, 246, 0.5); box-shadow: 0 15px 35px rgba(0,0,0,0.5); }
.skill-category h3 { color: var(--text-primary); margin-bottom: 20px; font-size: 1.3rem; display: flex; align-items: center; gap: 10px; }
.skill-category h3 i { background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.5rem; }
.skill-item { margin-bottom: 20px; }
.skill-info { display: flex; justify-content: space-between; margin-bottom: 6px; font-weight: 500; color: var(--text-secondary); font-size: 0.9rem; }
.skill-bar { height: 6px; background: rgba(255, 255, 255, 0.05); border-radius: 3px; overflow: hidden; }
.skill-progress { height: 100%; background: var(--gradient); border-radius: 3px; position: relative; width: 0; transition: width 1.5s ease-out; }
/* Added JS logic will fill these bars on scroll */

/* Projects */
.projects-section { background: rgba(15, 23, 42, 0.4); padding-bottom: 80px; }
.projects-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 30px; }
.project-card { background: var(--dark-surface); backdrop-filter: blur(12px); border-radius: 16px; overflow: hidden; border: var(--glass-border); box-shadow: var(--glass-shadow); transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); display: flex; flex-direction: column; }
.project-card:hover { transform: translateY(-10px) scale(1.02); box-shadow: 0 20px 40px rgba(0,0,0,0.6); border-color: rgba(139, 92, 246, 0.4); }
.project-img { width: 100%; height: 180px; object-fit: cover; transition: transform 0.6s ease; }
.project-card:hover .project-img { transform: scale(1.1); filter: brightness(1.1); }
.project-content { padding: 25px; flex-grow: 1; display: flex; flex-direction: column; position: relative; z-index: 2; background: linear-gradient(to top, var(--dark-surface) 80%, transparent); margin-top: -20px; border-radius: 16px 16px 0 0; }
.project-content h3 { color: var(--text-primary); margin-bottom: 8px; font-size: 1.2rem; }
.project-content p { color: var(--text-secondary); margin-bottom: 15px; font-size: 0.95rem; flex-grow: 1; line-height: 1.5; }
.project-tech { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px; }
.tech-tag { background: rgba(59, 130, 246, 0.1); color: #60a5fa; padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; border: 1px solid rgba(59, 130, 246, 0.2); transition: all 0.3s ease; }
.project-card:hover .tech-tag { background: rgba(59, 130, 246, 0.2); }
.project-links { display: flex; gap: 15px; }
.project-link { display: inline-flex; align-items: center; color: var(--text-primary); text-decoration: none; font-weight: 500; font-size: 0.9rem; transition: all 0.3s ease; background: rgba(255,255,255,0.05); padding: 8px 12px; border-radius: 8px; }
.project-link i { margin-left: 6px; }
.project-link:hover { color: white; background: var(--primary); transform: translateY(-2px); box-shadow: 0 4px 10px rgba(139, 92, 246, 0.4); }

/* Achievements */
.achievements-section { background: var(--dark); padding: 60px 0; overflow: hidden; }
.achievements-section .section-title h2 { color: var(--text-primary); }
.certificates-carousel { position: relative; max-width: 1200px; margin: 20px auto; padding: 0 50px; }
.certificates-track { display: flex; transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1); gap: 20px; padding: 20px 0; }
.certificate-card { position: relative; min-width: calc(33.333% - 14px); height: 350px; perspective: 1000px; cursor: pointer; border-radius: 16px; flex-shrink: 0; }
.certificate-card.active { z-index: 2; transform: scale(1.05); }
.certificate-front, .certificate-back { position: absolute; width: 100%; height: 100%; backface-visibility: hidden; transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275); border-radius: 16px; padding: 30px 20px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: var(--dark-surface); backdrop-filter: blur(12px); border: var(--glass-border); box-shadow: var(--glass-shadow); }
.certificate-front { transform: rotateY(0deg); }
.certificate-back { transform: rotateY(180deg); padding: 15px; }
.certificate-card.flipped .certificate-front { transform: rotateY(180deg); }
.certificate-card.flipped .certificate-back { transform: rotateY(360deg); }
.certificate-badge { width: 70px; height: 70px; background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; color: #a78bfa; font-size: 28px; transition: transform 0.3s ease;}
.certificate-card:hover .certificate-badge { transform: scale(1.1) rotate(5deg); background: rgba(139, 92, 246, 0.2); }
.certificate-front h3 { color: var(--text-primary); font-size: 1.2rem; margin-bottom: 10px; text-align: center; }
.certificate-front p { color: var(--text-secondary); margin-bottom: 20px; font-size: 0.9rem; text-align: center; }
.view-btn { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); color: var(--text-primary); padding: 8px 20px; border-radius: 30px; font-weight: 500; font-size: 0.9rem; transition: all 0.3s; }
.certificate-front:hover .view-btn { background: var(--primary); border-color: var(--primary); transform: translateY(-2px); }
.certificate-back img { width: 100%; height: 180px; object-fit: contain; border-radius: 8px; margin-bottom: 15px; transform: none; border: none; }
.certificate-actions { display: flex; gap: 10px; }
.zoom-btn { background: rgba(255, 255, 255, 0.1); color: white; padding: 8px 16px; border-radius: 8px; font-size: 0.85rem; display: flex; align-items: center; gap: 6px; transition: all 0.3s; text-decoration: none; border: 1px solid rgba(255, 255, 255, 0.2); cursor: pointer; }
.zoom-btn:hover { background: var(--primary); border-color: var(--primary); }
.multi-certificates { height: 180px; overflow-y: auto; width: 100%; margin-bottom: 15px; }
.certificate-item { background: rgba(0,0,0,0.2); padding: 10px; border-radius: 8px; border-left: 3px solid var(--primary); margin-bottom: 10px; }
.certificate-item h4 { color: var(--text-primary); margin-bottom: 5px; font-size: 0.9rem;}
.certificate-item p { color: var(--text-secondary); margin-bottom: 5px; font-size: 0.8rem;}
.carousel-btn { position: absolute; top: 50%; transform: translateY(-50%); width: 40px; height: 40px; background: rgba(30, 41, 59, 0.8); backdrop-filter: blur(10px); border: var(--glass-border); border-radius: 50%; color: var(--text-primary); font-size: 1.2rem; cursor: pointer; z-index: 10; transition: all 0.3s; display: flex; align-items: center; justify-content: center; }
.carousel-btn:hover { background: var(--primary); color: white; border-color: var(--primary); transform: translateY(-50%) scale(1.1); }
.prev-btn { left: 0; }
.next-btn { right: 0; }
.carousel-dots { display: flex; justify-content: center; gap: 10px; margin-top: 30px; }
.dot { width: 8px; height: 8px; border-radius: 50%; background: rgba(255,255,255,0.2); cursor: pointer; transition: all 0.3s; }
.dot.active { background: var(--primary); transform: scale(1.5); }

/* Modal */
.modal { display: none; position: fixed; z-index: 10000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(15, 23, 42, 0.9); backdrop-filter: blur(10px); }
.modal-content { margin: 5% auto; width: 95%; max-width: 1000px; background: var(--dark-surface); border: var(--glass-border); border-radius: 16px; padding: 25px; position: relative; max-height: 90vh; overflow-y: auto; }
.close-modal { position: absolute; top: 15px; right: 25px; color: var(--text-secondary); font-size: 30px; cursor: pointer; transition: 0.3s; }
.close-modal:hover { color: white; transform: rotate(90deg);}
.certificate-gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; margin-top: 20px; }
.gallery-certificate { background: rgba(0,0,0,0.3); padding: 10px; border-radius: 10px; }
.gallery-certificate img { width: 100%; border-radius: 6px; }
.gallery-certificate h4 { color: white; margin-bottom: 10px; text-align: center; font-size:0.9rem;}

/* Contact Section */
.contact-section { background: rgba(15, 23, 42, 0.6); padding-bottom: 60px; }
.contact-container { display: grid; grid-template-columns: 1fr 1.5fr; gap: 30px; }
.contact-info, .contact-form { background: var(--dark-surface); backdrop-filter: blur(12px); padding: 30px; border-radius: 20px; border: var(--glass-border); box-shadow: var(--glass-shadow); transition: all 0.4s ease; }
.contact-info:hover, .contact-form:hover { border-color: rgba(139, 92, 246, 0.3); box-shadow: 0 15px 30px rgba(0,0,0,0.4); }
.contact-info h3, .contact-form h3 { color: var(--text-primary); margin-bottom: 25px; font-size: 1.5rem; }
.contact-detail { display: flex; align-items: center; margin-bottom: 20px; padding: 10px; border-radius: 12px; transition: all 0.3s ease; }
.contact-detail:hover { background: rgba(255,255,255,0.03); transform: translateX(5px); }
.contact-detail i { width: 45px; height: 45px; background: rgba(139, 92, 246, 0.1); color: var(--primary); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; margin-right: 15px; flex-shrink: 0; transition: all 0.3s ease; }
.contact-detail:hover i { background: var(--primary); color: white; }
.contact-detail h4 { color: var(--text-secondary); font-size: 0.85rem; margin-bottom: 3px; }
.contact-detail a, .contact-detail p { color: var(--text-primary); text-decoration: none; font-weight: 500; font-size: 0.95rem; transition: 0.3s; }
.contact-detail a:hover { color: var(--primary); }
.form-group { margin-bottom: 20px; }
.form-group label { display: block; margin-bottom: 6px; color: var(--text-secondary); font-weight: 500; font-size: 0.9rem;}
.form-control { width: 100%; padding: 12px 16px; background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 10px; color: white; font-size: 0.95rem; transition: all 0.3s; }
.form-control:focus { outline: none; border-color: var(--primary); background: rgba(0, 0, 0, 0.3); box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2); }
textarea.form-control { min-height: 120px; resize: vertical; }
.submit-btn { background: var(--gradient); color: white; padding: 14px 30px; border: none; border-radius: 30px; cursor: pointer; font-size: 0.95rem; font-weight: 600; transition: all 0.3s; width: 100%; display: flex; justify-content: center; align-items: center; gap: 8px;}
.submit-btn:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(139, 92, 246, 0.5); }

/* Footer */
footer { background: var(--dark); border-top: 1px solid rgba(255,255,255,0.05); padding: 30px 0; text-align: center; }
.social-links { display: flex; justify-content: center; gap: 15px; margin-bottom: 0; }
.social-link { width: 40px; height: 40px; background: var(--dark-surface); border: var(--glass-border); color: var(--text-primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); text-decoration: none; }
.social-link:hover { background: var(--primary); color: white; transform: translateY(-5px) rotate(360deg); border-color: var(--primary); box-shadow: 0 8px 15px rgba(139, 92, 246, 0.4); }

/* Animation utilities - Staggered fade in up */
.reveal { opacity: 0; transform: translateY(30px); transition: all 0.7s cubic-bezier(0.5, 0, 0, 1); }
.reveal.active { opacity: 1; transform: translateY(0); }

.back-to-top { position: fixed; bottom: 30px; right: 30px; width: 45px; height: 45px; background: var(--dark-surface); backdrop-filter: blur(10px); border: var(--glass-border); color: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; cursor: pointer; opacity: 0; visibility: hidden; transition: all 0.3s; z-index: 999; box-shadow: 0 5px 15px rgba(0,0,0,0.3);}
.back-to-top.active { opacity: 1; visibility: visible; }
.back-to-top:hover { background: var(--primary); color: white; transform: translateY(-5px); }

/* Responsive adjustments */
@media (max-width: 1024px) { .contact-container { grid-template-columns: 1fr; } .hero h1 { font-size: 3rem; } .certificate-card { min-width: calc(50% - 10px); } }
@media (max-width: 768px) {
    .about-content { flex-direction: column; text-align: center; padding: 25px; gap: 25px;}
    .timeline::after { left: 40px; }
    .education-item { width: 100%; padding-left: 70px; margin-bottom: 25px;}
    .education-item::after { left: 32px; }
    .left::after, .right::after { left: 32px; right: auto; }
    .right { left: 0; }
    nav { display: none; position: absolute; top: 100%; left: 0; width: 100%; background: rgba(15, 23, 42, 0.95); backdrop-filter: blur(15px); flex-direction: column; padding: 15px; text-align: center; border-bottom: var(--glass-border); gap: 10px;}
    nav.active { display: flex; }
    nav a { padding: 10px;}
    .mobile-menu-btn { display: block; }
    .certificate-card { min-width: 100%; }
    .projects-grid { grid-template-columns: 1fr; }
    section { padding: 50px 0; }
}
@media (max-width: 480px) {
    .hero h1 { font-size: 2.2rem; }
    .hero p { font-size: 1rem; }
    .hero-btns { flex-direction: column; width: 100%; gap: 10px;}
    .section-title h2 { font-size: 1.8rem; margin-bottom: 30px;}
    .contact-info, .contact-form, .skill-category, .about-content { padding: 20px; }
    .profile-img { width: 180px; height: 180px; }
    .project-img { height: 160px; }
}
</style>"""

    content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)
    
    # Update HTML inside the hero area specifically for typewriter class if needed
    # We will just style it in CSS with an animated background clip to keep HTML clean.
    
    # 2. Re-inject JS (added skill progress bar animations)
    new_script = """<script>
    document.addEventListener('DOMContentLoaded', function() {
        // Carousel logic
        const track = document.querySelector('.certificates-track');
        const cards = document.querySelectorAll('.certificate-card');
        const prevBtn = document.querySelector('.prev-btn');
        const nextBtn = document.querySelector('.next-btn');
        const dotsContainer = document.querySelector('.carousel-dots');
        
        if (track && cards.length > 0) {
            let currentIndex = 0;
            const gap = 20;
            
            cards.forEach((_, index) => {
                const dot = document.createElement('div');
                dot.classList.add('dot');
                if (index === 0) dot.classList.add('active');
                dot.addEventListener('click', () => goToSlide(index));
                dotsContainer.appendChild(dot);
            });
            
            function updateCarousel() {
                const cardWidth = cards[0].offsetWidth;
                const offset = -currentIndex * (cardWidth + gap);
                track.style.transform = `translateX(${offset}px)`;
                cards.forEach((card, index) => card.classList.toggle('active', index === currentIndex));
                document.querySelectorAll('.dot').forEach((dot, index) => dot.classList.toggle('active', index === currentIndex));
            }
            
            function goToSlide(index) { currentIndex = Math.max(0, Math.min(index, cards.length - 1)); updateCarousel(); }
            function nextSlide() { if (currentIndex < cards.length - 1) { currentIndex++; updateCarousel(); } else { goToSlide(0); } }
            function prevSlide() { if (currentIndex > 0) { currentIndex--; updateCarousel(); } }
            
            cards.forEach(card => {
                card.addEventListener('click', function(e) {
                    if (e.target.closest('a') || e.target.closest('button')) return;
                    if (this.classList.contains('active')) this.classList.toggle('flipped');
                    else goToSlide(Array.from(cards).indexOf(this));
                });
            });
            
            nextBtn.addEventListener('click', nextSlide);
            prevBtn.addEventListener('click', prevSlide);
            
            let slideInterval = setInterval(nextSlide, 5000);
            track.addEventListener('mouseenter', () => clearInterval(slideInterval));
            track.addEventListener('mouseleave', () => slideInterval = setInterval(nextSlide, 5000));
            window.addEventListener('resize', updateCarousel);
            updateCarousel();
        }

        // Modal
        const modal = document.getElementById('certificatesModal');
        const closeBtn = document.querySelector('.close-modal');
        const viewAllBtns = document.querySelectorAll('.view-all-btn');
        
        viewAllBtns.forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.stopPropagation(); 
                const card = this.closest('.certificate-card');
                const certificates = card.querySelectorAll('.certificate-item');
                const gallery = modal.querySelector('.certificate-gallery');
                gallery.innerHTML = '';
                certificates.forEach(cert => {
                    const img = cert.querySelector('img');
                    const title = cert.querySelector('h4');
                    const certElement = document.createElement('div');
                    certElement.className = 'gallery-certificate';
                    certElement.innerHTML = `<h4>${title.textContent}</h4><img src="${img.dataset.full || img.src}" alt="${img.alt}">`;
                    gallery.appendChild(certElement);
                });
                modal.style.display = 'block';
            });
        });
        
        if (closeBtn) closeBtn.addEventListener('click', () => modal.style.display = 'none');
        window.addEventListener('click', e => { if (e.target === modal) modal.style.display = 'none'; });

        // Mobile Nav
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mainNav = document.getElementById('main-nav');
        if (mobileMenuBtn && mainNav) mobileMenuBtn.addEventListener('click', () => mainNav.classList.toggle('active'));
        
        // Smooth scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                if (!targetId || targetId === '#') return;
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    window.scrollTo({ top: targetElement.offsetTop - 70, behavior: 'smooth' });
                    if (mainNav) mainNav.classList.remove('active');
                }
            });
        });
        
        // Back To Top
        const backToTopBtn = document.getElementById('back-to-top');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) backToTopBtn.classList.add('active');
            else backToTopBtn.classList.remove('active');
        });
        if(backToTopBtn) backToTopBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

        // Staggered Scroll Reveal & Skill Bar Animation
        const revealElements = document.querySelectorAll('.reveal');
        const skillBars = document.querySelectorAll('.skill-progress');
        
        const revealOptions = { threshold: 0.1, rootMargin: "0px 0px -50px 0px" };
        const revealOnScroll = new IntersectionObserver(function(entries, observer) {
            entries.forEach((entry, index) => {
                if (!entry.isIntersecting) return;
                
                // Add stagger effect based on order
                setTimeout(() => {
                    entry.target.classList.add('active');
                    
                    // Specific logic for skill bars
                    if (entry.target.classList.contains('skill-category')) {
                        const bars = entry.target.querySelectorAll('.skill-progress');
                        bars.forEach(bar => {
                            const width = bar.parentElement.previousElementSibling.lastElementChild.textContent;
                            bar.style.width = width;
                        });
                    }
                }, 100 * (index % 5)); // Stagger by 100ms
                
                observer.unobserve(entry.target);
            });
        }, revealOptions);
        
        revealElements.forEach(el => revealOnScroll.observe(el));
    });
    </script>"""

    content = re.sub(r'<script>.*?</script>', '', content, flags=re.DOTALL)
    content = content.replace('</body>', new_script + '\n</body>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    modify_html(sys.argv[1])
