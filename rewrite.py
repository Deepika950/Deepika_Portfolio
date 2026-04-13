import sys

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deepika Enaganoori | Software & Full Stack Developer</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

    :root {
        /* Professional Tech Theme: Deep Blue and Emerald */
        --primary: #2563eb;       /* Royal Blue */
        --primary-light: #3b82f6;
        --secondary: #10b981;     /* Emerald Green */
        --dark: #0b1120;          /* Deep Slate Background */
        --dark-surface: rgba(30, 41, 59, 0.6); /* Glass surface */
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
    .logo { font-size: 1.5rem; font-weight: 800; color: white; letter-spacing: 0.5px; display: flex; align-items: center; gap: 10px;}
    .logo i { color: var(--primary-light); }
    nav { display: flex; gap: 10px; align-items: center; }
    nav a { color: var(--text-primary); text-decoration: none; font-weight: 500; font-size: 0.9rem; transition: all 0.3s ease; padding: 6px 12px; border-radius: 8px; }
    nav a:hover { color: var(--accent); background: rgba(255,255,255,0.05); }
    
    .resume-btn-nav { background: rgba(37, 99, 235, 0.15) !important; color: #60a5fa !important; border: 1px solid rgba(37, 99, 235, 0.3); margin-left: 10px;}
    .resume-btn-nav:hover { background: var(--primary) !important; color: white !important; }
    
    .mobile-menu-btn { display: none; background: none; border: none; color: var(--text-primary); font-size: 1.5rem; cursor: pointer; }

    /* Hero Section (Job Seeker Focused) */
    .hero { height: 100vh; display: flex; align-items: center; background: radial-gradient(circle at top right, rgba(37, 99, 235, 0.1), transparent 50%), var(--dark); position: relative; overflow: hidden; }
    .hero::after { content: ''; position: absolute; width: 40vw; height: 40vw; background: radial-gradient(circle, rgba(16, 185, 129, 0.05) 0%, transparent 60%); bottom: -10%; left: -10%; animation: pulse 10s infinite alternate-reverse; pointer-events: none; }
    @keyframes pulse { 0% { transform: scale(1); opacity: 0.5; } 100% { transform: scale(1.1); opacity: 0.8; } }

    .hero-content { max-width: 900px; margin: 0 auto; text-align: center; position: relative; z-index: 2; padding-top: 60px; }
    
    .hero-label { display: inline-block; padding: 6px 16px; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); color: var(--secondary); border-radius: 20px; font-size: 0.85rem; font-weight: 600; margin-bottom: 25px; letter-spacing: 1px; animation: slideUp 0.8s ease-out 0.2s both;}

    .hero h1 { font-size: 4.5rem; font-weight: 800; margin-bottom: 10px; line-height: 1.1; color: white; animation: slideUp 0.8s ease-out 0.4s both;}
    
    /* Typing Effect for Role */
    .hero h2 { font-size: 2.2rem; font-weight: 500; color: var(--text-secondary); margin-bottom: 25px; height: 50px; animation: slideUp 0.8s ease-out 0.6s both;}
    .typing-text { background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 700; border-right: 3px solid var(--accent); white-space: nowrap; overflow: hidden; padding-right: 5px; animation: blinkCursor 0.75s step-end infinite;}
    
    @keyframes blinkCursor { from, to { border-color: transparent } 50% { border-color: var(--accent); } }
    @keyframes slideUp { 0% { opacity: 0; transform: translateY(30px); } 100% { opacity: 1; transform: translateY(0); } }

    .hero p { font-size: 1.15rem; color: var(--text-secondary); margin-bottom: 40px; max-width: 700px; margin-left: auto; margin-right: auto; line-height: 1.6; animation: slideUp 0.8s ease-out 0.8s both; }

    .hero-btns { display: flex; justify-content: center; gap: 20px; animation: slideUp 0.8s ease-out 1s both; }
    .btn { display: inline-flex; align-items: center; justify-content: center; padding: 14px 32px; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 1rem; transition: all 0.3s ease; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .btn-primary { background: var(--primary); color: white; border: 1px solid var(--primary-light); }
    .btn-primary:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(37, 99, 235, 0.4); background: var(--primary-light); }
    
    .btn-success { background: var(--gradient-success); color: white; border: none;}
    .btn-success:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(16, 185, 129, 0.4); }

    .btn-outline { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.15); color: var(--text-primary); }
    .btn-outline:hover { background: rgba(255, 255, 255, 0.1); border-color: rgba(255, 255, 255, 0.3); transform: translateY(-3px); }

    /* Sections */
    section { padding: 80px 0; position: relative; }
    .section-title { margin-bottom: 50px; display: flex; flex-direction: column; align-items: flex-start; }
    .section-title h2 { font-size: 2.5rem; color: var(--text-primary); display: inline-block; position: relative; font-weight: 700;}
    .section-title h2::after { content: ''; position: absolute; width: 40px; height: 4px; background: var(--primary); bottom: -12px; left: 0; border-radius: 2px; transition: width 0.3s ease;}
    .section-title:hover h2::after { width: 100%; }
    .section-title p { color: var(--accent); font-weight: 600; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }

    /* About Mini */
    .about-section { background: rgba(15, 23, 42, 0.4); border-top: 1px solid rgba(255,255,255,0.02); }
    .about-content { display: grid; grid-template-columns: 1fr 2fr; gap: 50px; align-items: center; }
    .profile-card { background: var(--dark-surface); padding: 20px; border-radius: 16px; border: var(--glass-border); box-shadow: var(--glass-shadow); text-align: center;}
    .profile-img { width: 100%; height: auto; border-radius: 12px; object-fit: cover; margin-bottom: 20px; }
    .about-text h3 { font-size: 1.8rem; margin-bottom: 15px; color: var(--text-primary); font-weight: 600;}
    .about-text p { margin-bottom: 15px; font-size: 1.05rem; color: var(--text-secondary); line-height: 1.7;}
    
    .quick-stats { display: flex; gap: 30px; margin-top: 30px; }
    .stat-item { display: flex; flex-direction: column; }
    .stat-num { font-size: 2rem; font-weight: 800; font-family: 'Outfit'; color: var(--primary-light); line-height: 1;}
    .stat-label { font-size: 0.85rem; color: var(--text-secondary); font-weight: 500; margin-top: 5px;}

    /* Core Competencies (What I Do) */
    .competencies-section { background: var(--dark); }
    .competencies-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }
    .comp-card { background: var(--dark-surface); border: var(--glass-border); padding: 40px 30px; border-radius: 16px; transition: all 0.3s ease; position: relative; overflow: hidden; }
    .comp-card::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 3px; background: var(--gradient); transform: scaleX(0); transform-origin: left; transition: transform 0.4s ease; }
    .comp-card:hover::before { transform: scaleX(1); }
    .comp-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.4); background: rgba(30, 41, 59, 0.8); }
    .comp-icon { width: 60px; height: 60px; background: rgba(37, 99, 235, 0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; color: var(--primary-light); margin-bottom: 25px; }
    .comp-card h3 { font-size: 1.4rem; color: var(--text-primary); margin-bottom: 15px; }
    .comp-card p { color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 20px; line-height: 1.6;}
    .comp-tags { display: flex; flex-wrap: wrap; gap: 8px; }
    .c-tag { background: rgba(255,255,255,0.05); color: #cbd5e1; padding: 4px 10px; border-radius: 6px; font-size: 0.8rem; font-weight: 500;}

    /* Experience & Internships layout (Timeline) */
    .experience-section { background: rgba(15, 23, 42, 0.4); }
    .exp-timeline { border-left: 2px solid rgba(37, 99, 235, 0.3); padding-left: 40px; position: relative; }
    .exp-item { padding-bottom: 50px; position: relative; }
    .exp-item::before { content: ''; position: absolute; left: -47px; top: 0; width: 12px; height: 12px; background: var(--dark); border: 2px solid var(--primary-light); border-radius: 50%; box-shadow: 0 0 10px rgba(37, 99, 235, 0.5); }
    
    .exp-date { color: var(--primary-light); font-weight: 600; font-size: 0.9rem; margin-bottom: 5px; display: block; letter-spacing: 0.5px;}
    .exp-title { font-size: 1.4rem; color: var(--text-primary); font-weight: 700; margin-bottom: 5px; }
    .exp-company { font-size: 1.05rem; color: #cbd5e1; margin-bottom: 15px; display: flex; align-items: center; gap: 8px; }
    .exp-company i { color: var(--secondary); font-size: 0.9rem;}
    .exp-desc { color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6; margin-bottom: 15px; }
    .exp-desc ul { padding-left: 20px; list-style-type: none; }
    .exp-desc li { margin-bottom: 8px; position: relative; }
    .exp-desc li::before { content: "▹"; position: absolute; left: -15px; color: var(--primary-light); font-weight: bold; }

    /* Featured Project (Django Realtime) */
    .featured-project { background: var(--dark-surface); border: 1px solid rgba(37, 99, 235, 0.2); border-radius: 16px; display: grid; grid-template-columns: 1fr 1fr; overflow: hidden; margin-bottom: 50px; box-shadow: var(--glass-shadow); transition: all 0.3s ease;}
    .featured-project:hover { border-color: rgba(37, 99, 235, 0.5); box-shadow: 0 15px 40px rgba(0,0,0,0.5); }
    .fp-image { height: 100%; min-height: 300px; background: url('https://images.unsplash.com/photo-1555066931-4365d14bab8c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80') center/cover; position: relative; }
    .fp-image::after { content: ''; position: absolute; top:0; left:0; right:0; bottom:0; background: linear-gradient(to right, transparent, var(--dark-surface)); }
    .fp-content { padding: 40px; display: flex; flex-direction: column; justify-content: center; z-index: 2;}
    .fp-label { color: var(--secondary); font-weight: 600; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;}
    .fp-title { font-size: 1.8rem; color: var(--text-primary); margin-bottom: 15px; font-weight: 700; }
    .fp-desc { color: var(--text-secondary); font-size: 1rem; line-height: 1.6; margin-bottom: 25px; }
    
    /* Other Projects Grid */
    .projects-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 30px; }
    .project-card { background: rgba(30, 41, 59, 0.4); border: var(--glass-border); border-radius: 12px; overflow: hidden; transition: all 0.3s ease; display: flex; flex-direction: column; }
    .project-card:hover { transform: translateY(-8px); background: rgba(30, 41, 59, 0.8); border-color: rgba(255,255,255,0.1); box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
    .pc-content { padding: 30px; flex-grow: 1; display: flex; flex-direction: column;}
    .pc-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;}
    .pc-icon { font-size: 2rem; color: var(--primary-light); }
    .pc-links a { color: var(--text-secondary); font-size: 1.2rem; margin-left: 10px; transition: color 0.3s;}
    .pc-links a:hover { color: var(--primary-light); }
    .pc-title { font-size: 1.3rem; color: var(--text-primary); margin-bottom: 10px; font-weight: 600;}
    .pc-desc { color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 20px; flex-grow: 1; line-height: 1.5; }
    .pc-tech { display: flex; flex-wrap: wrap; gap: 10px; font-family: 'Inter'; font-size: 0.8rem; color: #94a3b8; font-weight: 500;}

    /* Education (Simplified for Professionals) */
    .education-simple { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
    .edu-card { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); padding: 25px; border-radius: 12px; display: flex; align-items: flex-start; gap: 20px; transition: all 0.3s;}
    .edu-card:hover { background: rgba(255,255,255,0.04); border-color: rgba(37, 99, 235, 0.3); }
    .edu-icon { width: 45px; height: 45px; background: rgba(255,255,255,0.05); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; color: #cbd5e1; flex-shrink:0;}
    .edu-details h4 { font-size: 1.1rem; color: var(--text-primary); margin-bottom: 5px;}
    .edu-details p { font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 5px;}
    .edu-details span { font-size: 0.85rem; color: var(--primary-light); font-weight: 600; display: inline-block; padding: 2px 8px; background: rgba(37, 99, 235, 0.1); border-radius: 4px;}

    /* Achievements / Certifications */
    .cert-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }
    .cert-card { background: rgba(30, 41, 59, 0.4); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 25px; display: flex; flex-direction: column; align-items: flex-start; transition: all 0.3s;}
    .cert-card:hover { border-color: var(--accent); background: rgba(30, 41, 59, 0.8); transform: translateY(-5px);}
    .cert-icon { font-size: 1.8rem; color: var(--accent); margin-bottom: 15px; }
    .cert-title { font-size: 1.1rem; color: var(--text-primary); font-weight: 600; margin-bottom: 5px;}
    .cert-issuer { font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 15px; flex-grow: 1;}
    .view-cert { color: var(--primary-light); font-size: 0.85rem; font-weight: 600; text-decoration: none; display: flex; align-items: center; gap: 5px; transition: 0.3s;}
    .view-cert:hover { color: white; }

    /* Contact Section */
    .contact-container { display: grid; grid-template-columns: 1fr 1.5fr; gap: 40px; }
    .contact-info, .contact-form { background: var(--dark-surface); padding: 40px; border-radius: 16px; border: var(--glass-border); }
    .contact-info h3 { font-size: 1.6rem; margin-bottom: 10px; color: var(--text-primary); }
    .contact-info > p { color: var(--text-secondary); margin-bottom: 30px; font-size: 0.95rem; }
    .contact-detail { display: flex; align-items: center; margin-bottom: 25px; }
    .cd-icon { width: 45px; height: 45px; background: rgba(255,255,255,0.05); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; color: var(--text-primary); margin-right: 15px; transition: 0.3s;}
    .contact-detail:hover .cd-icon { background: var(--primary); color: white;}
    .cd-text h4 { font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 3px; font-weight: 500;}
    .cd-text a, .cd-text p { color: var(--text-primary); font-size: 1rem; font-weight: 500; text-decoration: none; transition: 0.3s;}
    .cd-text a:hover { color: var(--primary-light); }
    
    .form-group { margin-bottom: 20px; }
    .form-control { width: 100%; padding: 14px 18px; background: rgba(0, 0, 0, 0.2); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; color: white; font-size: 0.95rem; transition: all 0.3s; }
    .form-control:focus { outline: none; border-color: var(--primary-light); background: rgba(0, 0, 0, 0.4); }
    textarea.form-control { min-height: 140px; resize: vertical; }
    .submit-btn { background: var(--primary); color: white; padding: 14px 30px; border: none; border-radius: 8px; cursor: pointer; font-size: 0.95rem; font-weight: 600; width: 100%; transition: all 0.3s; }
    .submit-btn:hover { background: var(--primary-light); transform: translateY(-3px); box-shadow: 0 8px 20px rgba(37, 99, 235, 0.4); }

    /* Footer */
    footer { padding: 40px 0; text-align: center; border-top: 1px solid rgba(255,255,255,0.05); background: var(--dark); margin-top: 50px;}
    .social-links { display: flex; justify-content: center; gap: 15px; margin-bottom: 20px; }
    .social-link { width: 45px; height: 45px; background: rgba(255,255,255,0.05); color: var(--text-primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; transition: 0.3s; text-decoration: none; }
    .social-link:hover { background: var(--primary); color: white; transform: translateY(-5px); }
    .copyright { color: var(--text-secondary); font-size: 0.9rem; }

    /* Utilities & Animations */
    .reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s cubic-bezier(0.5, 0, 0, 1); }
    .reveal.active { opacity: 1; transform: translateY(0); }
    
    .back-to-top { position: fixed; bottom: 30px; right: 30px; width: 45px; height: 45px; background: var(--primary); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; opacity: 0; visibility: hidden; transition: 0.3s; z-index: 999; box-shadow: 0 5px 15px rgba(0,0,0,0.3);}
    .back-to-top.active { opacity: 1; visibility: visible; }
    .back-to-top:hover { transform: translateY(-5px); background: var(--primary-light);}

    /* Responsive */
    @media (max-width: 992px) { 
        .about-content, .contact-container { grid-template-columns: 1fr; } 
        .competencies-grid { grid-template-columns: repeat(2, 1fr); }
        .featured-project { grid-template-columns: 1fr; }
        .fp-image { min-height: 250px; }
        .fp-image::after { background: linear-gradient(to bottom, transparent, var(--dark-surface)); }
    }
    @media (max-width: 768px) {
        .hero h1 { font-size: 3rem; }
        .hero h2 { font-size: 1.5rem; height: auto;}
        .competencies-grid { grid-template-columns: 1fr; }
        nav { display: none; position: absolute; top: 100%; left: 0; width: 100%; background: var(--dark); flex-direction: column; padding: 20px; border-bottom: 1px solid rgba(255,255,255,0.1); }
        nav.active { display: flex; }
        .mobile-menu-btn { display: block; }
        .hero-btns { flex-direction: column; gap: 15px; }
        .btn { width: 100%; }
        section { padding: 50px 0; }
        .exp-timeline { padding-left: 25px; }
        .exp-item::before { left: -32px; }
    }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container header-container">
            <div class="logo"><i class="fas fa-terminal"></i> Deepika.E</div>
            <nav id="main-nav">
                <a href="#about">About</a>
                <a href="#competencies">Expertise</a>
                <a href="#experience">Experience</a>
                <a href="#projects">Work</a>
                <a href="#certifications">Certifications</a>
                <a href="#contact" class="resume-btn-nav">Hire Me</a>
            </nav>
            <button class="mobile-menu-btn" id="mobile-menu-btn">
                <i class="fas fa-bars"></i>
            </button>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <span class="hero-label"><i class="fas fa-circle" style="font-size: 10px; margin-right: 5px; color: #10b981;"></i> Actively Seeking Opportunities</span>
                <h1>Hi, I'm Deepika Enaganoori.</h1>
                <h2>I build solutions as a <span class="typing-text">Software Developer.</span></h2>
                <p>A passionate B.Tech final-year student specializing in AI and Full Stack Development. I design and build production-ready applications using Django, React, and Python, combining robust backend architecture with intuitive user experiences.</p>
                <div class="hero-btns">
                    <a href="#projects" class="btn btn-primary">View My Work</a>
                    <a href="https://raw.githubusercontent.com/Deepika950/Deepika_Portfolio/main/assets/document/Deepika_Resume.pdf" class="btn btn-outline" target="_blank" download>
                        Download Resume <i class="fas fa-download" style="margin-left: 8px;"></i>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- About Mini -->
    <section id="about" class="about-section">
        <div class="container reveal">
            <div class="about-content">
                <div class="profile-card">
                    <img src="https://raw.githubusercontent.com/Deepika950/Deepika_Portfolio/main/assets/images/Deepika_pic.jpg" alt="Deepika Enaganoori" class="profile-img">
                    <a href="https://www.linkedin.com/in/deepika-enaganoori" class="btn btn-outline" style="width: 100%; border-radius: 8px; padding: 10px;" target="_blank"><i class="fab fa-linkedin" style="margin-right: 8px;"></i> Connect on LinkedIn</a>
                </div>
                <div class="about-text">
                    <div class="section-title" style="margin-bottom: 20px;">
                        <p>About Me</p>
                        <h2 style="font-size: 2rem;">Driven by Logic, Focused on Impact.</h2>
                    </div>
                    <p>I am currently pursuing a Bachelor's degree at SVR Engineering College, specializing in Artificial Intelligence (CGPA: 8.7/10). Over the past years, I've transitioned from theoretical learning to hands-on software engineering, developing full-stack web applications and machine learning models.</p>
                    <p>My core strength lies in translating complex requirements into clean, efficient, and scalable code. Whether it's architecting a database for a college administration system in Django or integrating AI APIs into a modern frontend, I am ready to step into a professional engineering role and contribute immediately.</p>
                    
                    <div class="quick-stats">
                        <div class="stat-item">
                            <span class="stat-num">4+</span>
                            <span class="stat-label">Major Projects</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-num">5+</span>
                            <span class="stat-label">Tech Certifications</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-num">1st</span>
                            <span class="stat-label">Real-time Deployment</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Core Competencies -->
    <section id="competencies" class="competencies-section">
        <div class="container">
            <div class="section-title reveal">
                <p>What I Do</p>
                <h2>Core Competencies</h2>
            </div>
            
            <div class="competencies-grid">
                <div class="comp-card reveal">
                    <div class="comp-icon"><i class="fas fa-server"></i></div>
                    <h3>Backend & API Development</h3>
                    <p>Building secure, scalable, and robust server-side architectures and RESTful APIs capable of handling complex business logic.</p>
                    <div class="comp-tags">
                        <span class="c-tag">Python</span>
                        <span class="c-tag">Django</span>
                        <span class="c-tag">SQL / MySQL</span>
                        <span class="c-tag">SQLite</span>
                    </div>
                </div>
                
                <div class="comp-card reveal" style="transition-delay: 0.1s;">
                    <div class="comp-icon"><i class="fas fa-layer-group"></i></div>
                    <h3>Frontend Engineering</h3>
                    <p>Creating responsive, dynamic, and intuitive user interfaces that provide seamless user experiences across all devices.</p>
                    <div class="comp-tags">
                        <span class="c-tag">React.js</span>
                        <span class="c-tag">JavaScript (ES6+)</span>
                        <span class="c-tag">HTML5 / CSS3</span>
                        <span class="c-tag">Bootstrap</span>
                    </div>
                </div>
                
                <div class="comp-card reveal" style="transition-delay: 0.2s;">
                    <div class="comp-icon"><i class="fas fa-brain"></i></div>
                    <h3>Data Science & AI</h3>
                    <p>Leveraging machine learning models and data analytics tools to extract insights and build intelligent application features.</p>
                    <div class="comp-tags">
                        <span class="c-tag">Machine Learning</span>
                        <span class="c-tag">TensorFlow</span>
                        <span class="c-tag">Pandas / NumPy</span>
                        <span class="c-tag">NLTK</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience -->
    <section id="experience" class="experience-section">
        <div class="container">
            <div class="section-title reveal">
                <p>Journey So Far</p>
                <h2>Experience & Internships</h2>
            </div>
            
            <div class="exp-timeline">
                
                <!-- Highlighted College Project treated as Experience -->
                <div class="exp-item reveal">
                    <span class="exp-date">2023 - Present</span>
                    <h3 class="exp-title">Lead Developer (Capstone / Real-time Project)</h3>
                    <span class="exp-company"><i class="fas fa-university"></i> SVR Engineering College Administration</span>
                    <div class="exp-desc">
                        <p>Spearheading the development of a real-time <strong>Online Leave Management System</strong> meant for deployment within the college ecosystem.</p>
                        <br>
                        <ul>
                            <li>Architected the complete backend using the <strong>Django framework</strong> and SQLite database.</li>
                            <li>Designed distinct access portals with role-based authentication for Students, Faculty, and Admin.</li>
                            <li>Implemented frontend using HTML, CSS, and Bootstrap, ensuring a responsive mobile-first design.</li>
                            <li>Currently finalizing the system for production rollout to handle hundreds of daily leave requests asynchronously.</li>
                        </ul>
                    </div>
                </div>

                <div class="exp-item reveal">
                    <span class="exp-date">Recent</span>
                    <h3 class="exp-title">Data Science Intern</h3>
                    <span class="exp-company"><i class="fas fa-briefcase"></i> SkillDzire (AICTE Approved)</span>
                    <div class="exp-desc">
                        <p>Engaged in a rigorous internship program focused on practical data science application.</p>
                        <ul>
                            <li>Applied Python data manipulation libraries to clean and process large datasets.</li>
                            <li>Assisted in building predictive models and learning industry-standard deployment practices.</li>
                        </ul>
                    </div>
                </div>
                
                <div class="exp-item reveal">
                    <span class="exp-date">Recent</span>
                    <h3 class="exp-title">AI/ML Intern</h3>
                    <span class="exp-company"><i class="fas fa-briefcase"></i> Eduskills Foundation</span>
                    <div class="exp-desc">
                        <p>Completed hands-on projects exploring foundational Machine Learning algorithms.</p>
                        <ul>
                            <li>Developed workflows for data preprocessing and feature engineering.</li>
                            <li>Gained exposure to deep learning concepts and model evaluation metrics.</li>
                        </ul>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Projects Portfolio -->
    <section id="projects" class="competencies-section">
        <div class="container">
            <div class="section-title reveal">
                <p>Showcase</p>
                <h2>Selected Work</h2>
            </div>
            
            <!-- Featured Full Width Project -->
            <div class="featured-project reveal">
                <div class="fp-image" style="background-image: url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');"></div>
                <div class="fp-content">
                    <span class="fp-label"><i class="fas fa-star"></i> Featured Deployment</span>
                    <h3 class="fp-title">LeavePortal System</h3>
                    <p class="fp-desc">A comprehensive, real-time leave management application designed for institution-wide use. It replaces manual paperwork with a centralized, role-based dashboard for submitters and approvers, featuring dynamic status tracking and email notifications.</p>
                    <div class="pc-tech" style="margin-bottom: 25px;">
                        <span class="c-tag">Python</span>
                        <span class="c-tag">Django</span>
                        <span class="c-tag">SQLite</span>
                        <span class="c-tag">Bootstrap</span>
                    </div>
                    <div style="display: flex; gap: 15px;">
                        <a href="#" class="btn btn-primary">View Case Study</a>
                        <a href="#" class="btn btn-outline" title="GitHub Repo"><i class="fab fa-github"></i></a>
                    </div>
                </div>
            </div>

            <!-- Standard Projects Grid -->
            <div class="projects-grid">
                
                <div class="project-card reveal">
                    <div class="pc-content">
                        <div class="pc-header">
                            <i class="fas fa-leaf pc-icon"></i>
                            <div class="pc-links">
                                <a href="https://github.com/Deepika950/crop-recommendation-system-application" target="_blank"><i class="fab fa-github"></i></a>
                                <a href="https://crop-recommendation-system-application-dw8d.onrender.com/" target="_blank"><i class="fas fa-external-link-alt"></i></a>
                            </div>
                        </div>
                        <h3 class="pc-title">AgriPredict AI</h3>
                        <p class="pc-desc">A Machine Learning powered web application that analyzes soil parameters and climate inputs to recommend the most optimal crop, aiding farmers in data-driven decision making.</p>
                        <div class="pc-tech">
                            <span>Django</span> • <span>Scikit-Learn</span> • <span>MySQL</span>
                        </div>
                    </div>
                </div>

                <div class="project-card reveal" style="transition-delay: 0.1s;">
                    <div class="pc-content">
                        <div class="pc-header">
                            <i class="fas fa-exchange-alt pc-icon"></i>
                            <div class="pc-links">
                                <a href="#"><i class="fab fa-github"></i></a>
                                <a href="#"><i class="fas fa-external-link-alt"></i></a>
                            </div>
                        </div>
                        <h3 class="pc-title">SwiftX Currency Converter</h3>
                        <p class="pc-desc">A dynamic frontend application fetching real-time exchange rates via 3rd-party APIs to instantly compute and convert amounts between international currencies.</p>
                        <div class="pc-tech">
                            <span>React.js</span> • <span>REST API</span> • <span>Hooks</span>
                        </div>
                    </div>
                </div>

                <div class="project-card reveal" style="transition-delay: 0.2s;">
                    <div class="pc-content">
                        <div class="pc-header">
                            <i class="fas fa-comment-dots pc-icon"></i>
                            <div class="pc-links">
                                <a href="#"><i class="fab fa-github"></i></a>
                            </div>
                        </div>
                        <h3 class="pc-title">College Assistant NLP Bot</h3>
                        <p class="pc-desc">An intelligent conversational agent built to handle student queries. Uses Natural Language Processing (NLTK) and TensorFlow to classify intents and generate contextual responses.</p>
                        <div class="pc-tech">
                            <span>Python</span> • <span>TensorFlow</span> • <span>NLTK</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Certifications & Education (Simplified) -->
    <section id="certifications" class="experience-section">
        <div class="container">
            
            <div class="section-title reveal">
                <p>Background</p>
                <h2>Education & Certifications</h2>
            </div>
            
            <h3 style="color: var(--text-primary); margin-bottom: 20px; font-weight: 500;" class="reveal">Academic Background</h3>
            <div class="education-simple" style="margin-bottom: 50px;">
                <div class="edu-card reveal">
                    <div class="edu-icon"><i class="fas fa-graduation-cap"></i></div>
                    <div class="edu-details">
                        <h4>B.Tech in Artificial Intelligence</h4>
                        <p>SVR Engineering College, JNTUA</p>
                        <span>2022 - 2026 | CGPA: 8.7</span>
                    </div>
                </div>
                <div class="edu-card reveal" style="transition-delay: 0.1s;">
                    <div class="edu-icon"><i class="fas fa-book"></i></div>
                    <div class="edu-details">
                        <h4>Intermediate (MPC)</h4>
                        <p>A.P. Model School, Gospadu</p>
                        <span>2022 | Score: 95.2%</span>
                    </div>
                </div>
            </div>

            <h3 style="color: var(--text-primary); margin-bottom: 20px; font-weight: 500;" class="reveal">Professional Certifications</h3>
            <div class="cert-grid">
                
                <div class="cert-card reveal">
                    <i class="fas fa-database cert-icon"></i>
                    <h4 class="cert-title">MongoDB Expert Series</h4>
                    <p class="cert-issuer">MongoDB University</p>
                    <a href="#" class="view-cert">View Series Details <i class="fas fa-arrow-right"></i></a>
                </div>
                
                <div class="cert-card reveal">
                    <i class="fab fa-google cert-icon" style="color: #4285F4;"></i>
                    <h4 class="cert-title">Cloud Foundations</h4>
                    <p class="cert-issuer">Google Cloud (8-Course)</p>
                    <a href="https://www.cloudskillsboost.google/public_profiles/02627208-1fe9-4954-a896-4d9ac59b1314" target="_blank" class="view-cert" style="color:#4285F4;">Verify Badge <i class="fas fa-external-link-alt"></i></a>
                </div>

                <div class="cert-card reveal">
                    <i class="fab fa-python cert-icon" style="color: #f59e0b;"></i>
                    <h4 class="cert-title">Python Foundation</h4>
                    <p class="cert-issuer">Infosys Springboard</p>
                    <a href="#" class="view-cert">View Certificate <i class="fas fa-arrow-right"></i></a>
                </div>

                <div class="cert-card reveal">
                    <i class="fas fa-chart-pie cert-icon" style="color: #8b5cf6;"></i>
                    <h4 class="cert-title">Data Science with R</h4>
                    <p class="cert-issuer">IBM (3-Course Series)</p>
                    <a href="#" class="view-cert">View Series <i class="fas fa-arrow-right"></i></a>
                </div>

            </div>

        </div>
    </section>

    <!-- Contact Form -->
    <section id="contact" class="competencies-section">
        <div class="container">
            <div class="section-title reveal">
                <p>Let's Connect</p>
                <h2>Ready for Opportunities</h2>
            </div>
            
            <div class="contact-container">
                <div class="contact-info reveal">
                    <h3>Get In Touch</h3>
                    <p>I am actively seeking full-time roles and internships in Software Development, Full Stack Engineering, and Django Development. If you have an opportunity or just want to connect, feel free to reach out.</p>
                    
                    <div class="contact-detail">
                        <div class="cd-icon"><i class="fas fa-envelope"></i></div>
                        <div class="cd-text">
                            <h4>Email</h4>
                            <a href="mailto:deepikaenaganoori@gmail.com">deepikaenaganoori@gmail.com</a>
                        </div>
                    </div>
                    
                    <div class="contact-detail">
                        <div class="cd-icon"><i class="fas fa-phone"></i></div>
                        <div class="cd-text">
                            <h4>Phone</h4>
                            <a href="tel:+916301295599">+91 6301295599</a>
                        </div>
                    </div>
                    
                    <div class="contact-detail">
                        <div class="cd-icon"><i class="fab fa-linkedin"></i></div>
                        <div class="cd-text">
                            <h4>LinkedIn</h4>
                            <a href="https://www.linkedin.com/in/deepika-enaganoori" target="_blank">linkedin.com/in/deepika-enaganoori</a>
                        </div>
                    </div>
                </div>
                
                <div class="contact-form reveal" style="transition-delay: 0.1s;">
                    <h3>Send a Message</h3>
                    <form action="https://formsubmit.co/deepikaenaganoori@gmail.com" method="POST">
                        <input type="hidden" name="_template" value="basic">
                        <input type="hidden" name="_next" value="https://Deepika950.github.io/Deepika_Portfolio#about">
                        
                        <div class="form-group">
                            <label>Name</label>
                            <input type="text" name="name" class="form-control" required placeholder="John Doe">
                        </div>
                            
                        <div class="form-group">
                            <label>Email</label>
                            <input type="email" name="email" class="form-control" required placeholder="john@company.com">
                        </div>
                            
                        <div class="form-group">
                            <label>Subject</label>
                            <input type="text" name="subject" class="form-control" required placeholder="Job Opportunity Details">
                        </div>
                            
                        <div class="form-group">
                            <label>Message</label>
                            <textarea name="message" class="form-control" required placeholder="Hello Deepika, we are looking for a Django developer..."></textarea>
                        </div>
                            
                        <button type="submit" class="submit-btn"><i class="fas fa-paper-plane" style="margin-right: 8px;"></i> Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="social-links">
                <a href="https://github.com/Deepika950" class="social-link" target="_blank"><i class="fab fa-github"></i></a>
                <a href="https://www.linkedin.com/in/deepika-enaganoori" class="social-link" target="_blank"><i class="fab fa-linkedin"></i></a>
                <a href="https://leetcode.com/deepika630/" class="social-link" target="_blank"><i class="fas fa-code"></i></a>
                <a href="https://www.credly.com/users/deepika-enaganoori/badges" class="social-link" target="_blank"><i class="fas fa-award"></i></a>
            </div>
            <p class="copyright">&copy; 2024 Deepika Enaganoori. Built with Python, HTML & CSS.</p>
        </div>
    </footer>

    <div class="back-to-top" id="back-to-top"><i class="fas fa-arrow-up"></i></div>

    <script>
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
        backBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

        // Typing effect logic
        const roles = ["Software Developer.", "Full Stack Engineer.", "Django Specialist.", "Problem Solver."];
        let roleIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        const typingEl = document.querySelector('.typing-text');
        
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
                typeSpeed = 2000; // Pause at end of word
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                roleIndex = (roleIndex + 1) % roles.length;
                typeSpeed = 500; // Pause before typing new word
            }
            
            setTimeout(typeEffect, typeSpeed);
        }
        
        // Start typing effect after the slideUp animation finishes
        setTimeout(typeEffect, 1500);

        // Scroll Reveal Animations
        const revealElements = document.querySelectorAll('.reveal');
        const revealOptions = { threshold: 0.15, rootMargin: "0px 0px -20px 0px" };
        const revealOnScroll = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        }, revealOptions);
        
        revealElements.forEach(el => revealOnScroll.observe(el));
    });
    </script>
</body>
</html>"""

with open(sys.argv[1], 'w', encoding='utf-8') as f:
    f.write(html_content)
