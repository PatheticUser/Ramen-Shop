import os
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

INTER_BOLD = '/home/Rameez/.local/share/fonts/Inter/extras/ttf/Inter-Bold.ttf'
INTER_SEMIBOLD = '/home/Rameez/.local/share/fonts/Inter/extras/ttf/Inter-SemiBold.ttf'
INTER_REGULAR = '/home/Rameez/.local/share/fonts/Inter/extras/ttf/Inter-Regular.ttf'
INTER_MEDIUM = '/home/Rameez/.local/share/fonts/Inter/extras/ttf/Inter-Medium.ttf'

OUT_DIR = 'static/textures/screens'
os.makedirs(f'{OUT_DIR}/aboutMeScreens', exist_ok=True)
os.makedirs(f'{OUT_DIR}/vendingMachineScreens', exist_ok=True)
os.makedirs(f'{OUT_DIR}/arcadeScreens', exist_ok=True)

# ----------------------------------------------------
# 1. BIG SCREEN ABOUT (Desktop)
# ----------------------------------------------------
print("Generating bigScreenAbout...")
im_about = Image.open('oriented_about.png').convert('RGBA')
draw = ImageDraw.Draw(im_about)

# Clear old title & text
draw.rectangle([250, 1015, 1200, 1110], fill=(14, 14, 14, 255))
draw.rectangle([250, 1120, 1850, 1645], fill=(14, 14, 14, 255))

font_title = ImageFont.truetype(INTER_BOLD, 70)
font_body = ImageFont.truetype(INTER_REGULAR, 26)

draw.text((270, 1030), 'Hi, I’m Afifa.', font=font_title, fill=(255, 255, 255, 255))

about_text = (
    "I’m a Junior AI Developer and AI Researcher passionate about building intelligent systems "
    "that transform complex problems into practical, technology-driven solutions. My work focuses "
    "on the development and exploration of Agentic AI, Large Language Models (LLMs), Retrieval-Augmented "
    "Generation (RAG), Natural Language Processing (NLP), Machine Learning, and AI-driven automation.\n\n"
    "I enjoy working across the complete journey of an AI solution—from research and experimentation "
    "to prototyping and practical implementation. I have contributed to projects involving intelligent "
    "agents, document intelligence, machine learning, and decision-support systems. I am a Microsoft Certified "
    "Azure AI Engineer Associate and a Microsoft Learn Student Ambassador.\n\n"
    "Thanks for visiting!"
)

lines = []
for p in about_text.split('\n\n'):
    lines.extend(textwrap.wrap(p, width=68))
    lines.append('')

y = 1135
for line in lines:
    if line:
        draw.text((270, y), line, font=font_body, fill=(230, 230, 230, 255))
    y += 36

# Rotate 270 in PIL to match Three.js UV
res_about = im_about.rotate(270, expand=False)
res_about.save(f'{OUT_DIR}/aboutMeScreens/bigScreenAbout.png')


# ----------------------------------------------------
# 2. BIG SCREEN ABOUT (Mobile)
# ----------------------------------------------------
print("Generating bigScreenAboutMobile...")
im_about_m = Image.open('oriented_about_mobile.png').convert('RGBA')
draw_m = ImageDraw.Draw(im_about_m)

# Clear old title and body in mobile view
draw_m.rectangle([260, 480, 1000, 560], fill=(14, 14, 14, 255))
draw_m.rectangle([260, 565, 1750, 920], fill=(14, 14, 14, 255))

draw_m.text((270, 485), 'Hi, I’m Afifa.', font=ImageFont.truetype(INTER_BOLD, 64), fill=(255, 255, 255, 255))

font_body_m = ImageFont.truetype(INTER_REGULAR, 23)
lines_m = []
for p in about_text.split('\n\n'):
    lines_m.extend(textwrap.wrap(p, width=48))
    lines_m.append('')

y = 575
for line in lines_m:
    if line:
        draw_m.text((270, y), line, font=font_body_m, fill=(230, 230, 230, 255))
    y += 32

res_about_m = im_about_m.rotate(270, expand=False)
res_about_m.save(f'{OUT_DIR}/aboutMeScreens/bigScreenAboutMobile.png')


# ----------------------------------------------------
# 3. BIG SCREEN EXPERIENCE (Desktop)
# ----------------------------------------------------
print("Generating bigScreenExperience...")
im_exp = Image.open('oriented_experience.png').convert('RGBA')
draw_exp = ImageDraw.Draw(im_exp)

# Clear left description and right cards in desktop area (y=1000..1800)
draw_exp.rectangle([250, 1000, 1140, 1800], fill=(14, 14, 14, 255))
draw_exp.rectangle([1150, 1000, 1850, 1800], fill=(14, 14, 14, 255))

draw_exp.text((270, 1030), 'Experience', font=ImageFont.truetype(INTER_BOLD, 64), fill=(255, 255, 255, 255))

exp_left = (
    "Junior AI Developer and AI Researcher with experience building AI agents, "
    "document intelligence, RAG systems, and data pipelines across industry "
    "and freelance research.\n\n"
    "My core areas of interest include agentic workflows, LLM applications, "
    "and intelligent automation.\n\n"
    "Learn more about my projects by visiting the projects section of this site. "
    "Contact me for my full resume."
)

y = 1130
for p in exp_left.split('\n\n'):
    for line in textwrap.wrap(p, width=42):
        draw_exp.text((270, y), line, font=ImageFont.truetype(INTER_REGULAR, 23), fill=(230, 230, 230, 255))
        y += 33
    y += 10

# Draw 3 cards on the right in desktop area
# Card 1: Essentia Technologies
draw_exp.rectangle([1165, 1030, 1845, 1220], fill=(21, 25, 27, 255))
draw_exp.text((1185, 1045), "Essentia Technologies", font=ImageFont.truetype(INTER_BOLD, 28), fill=(0, 255, 240, 255))
draw_exp.text((1185, 1083), "Jr. AI Developer · Contract (Jul 2026 - Present)", font=ImageFont.truetype(INTER_MEDIUM, 18), fill=(130, 230, 255, 255))
essentia_desc = "Contributing to AI-powered solutions, intelligent systems, automation workflows, and practical applications of emerging AI technologies."
y_c = 1115
for line in textwrap.wrap(essentia_desc, width=54):
    draw_exp.text((1185, y_c), line, font=ImageFont.truetype(INTER_REGULAR, 17), fill=(220, 220, 220, 255))
    y_c += 23

# Card 2: Microsoft
draw_exp.rectangle([1165, 1250, 1845, 1460], fill=(21, 25, 27, 255))
draw_exp.text((1185, 1265), "Microsoft", font=ImageFont.truetype(INTER_BOLD, 28), fill=(0, 255, 240, 255))
draw_exp.text((1185, 1303), "Learn Student Ambassador · Freelance (Jun 2026 - Present)", font=ImageFont.truetype(INTER_MEDIUM, 18), fill=(130, 230, 255, 255))
ms_desc = "Engaging with the global Microsoft technical community, exploring emerging AI technologies, and supporting peer learning around artificial intelligence and cloud innovation."
y_c = 1335
for line in textwrap.wrap(ms_desc, width=54):
    draw_exp.text((1185, y_c), line, font=ImageFont.truetype(INTER_REGULAR, 17), fill=(220, 220, 220, 255))
    y_c += 23

# Card 3: Freelance
draw_exp.rectangle([1165, 1490, 1845, 1700], fill=(21, 25, 27, 255))
draw_exp.text((1185, 1505), "Freelance", font=ImageFont.truetype(INTER_BOLD, 28), fill=(0, 255, 240, 255))
draw_exp.text((1185, 1543), "Artificial Intelligence Consultant · Self-employed (Dec 2025 - Present)", font=ImageFont.truetype(INTER_MEDIUM, 18), fill=(130, 230, 255, 255))
free_desc = "Transforming raw client datasets into research-ready analytical insights using statistical modelling, multivariate regression, and hypothesis testing pipelines."
y_c = 1575
for line in textwrap.wrap(free_desc, width=54):
    draw_exp.text((1185, y_c), line, font=ImageFont.truetype(INTER_REGULAR, 17), fill=(220, 220, 220, 255))
    y_c += 23

res_exp = im_exp.rotate(270, expand=False)
res_exp.save(f'{OUT_DIR}/aboutMeScreens/bigScreenExperience.png')


# ----------------------------------------------------
# 4. BIG SCREEN EXPERIENCE (Mobile)
# ----------------------------------------------------
print("Generating bigScreenExperienceMobile...")
im_exp_m = Image.open('oriented_experience_mobile.png').convert('RGBA')
draw_exp_m = ImageDraw.Draw(im_exp_m)

# Clear old content area
draw_exp_m.rectangle([250, 555, 1750, 900], fill=(14, 14, 14, 255))

draw_exp_m.text((270, 560), "Essentia Technologies", font=ImageFont.truetype(INTER_BOLD, 26), fill=(0, 255, 240, 255))
draw_exp_m.text((580, 564), "Jr. AI Developer (Jul 2026 - Present)", font=ImageFont.truetype(INTER_MEDIUM, 20), fill=(130, 230, 255, 255))
draw_exp_m.text((270, 595), "AI solutions, agentic workflows, automation & document intelligence", font=ImageFont.truetype(INTER_REGULAR, 19), fill=(220, 220, 220, 255))

draw_exp_m.text((270, 640), "Microsoft", font=ImageFont.truetype(INTER_BOLD, 26), fill=(0, 255, 240, 255))
draw_exp_m.text((430, 644), "Student Ambassador (Jun 2026 - Present)", font=ImageFont.truetype(INTER_MEDIUM, 20), fill=(130, 230, 255, 255))
draw_exp_m.text((270, 675), "Community engagement, AI learning & cloud innovation", font=ImageFont.truetype(INTER_REGULAR, 19), fill=(220, 220, 220, 255))

draw_exp_m.text((270, 720), "Freelance", font=ImageFont.truetype(INTER_BOLD, 26), fill=(0, 255, 240, 255))
draw_exp_m.text((430, 724), "AI Consultant (Dec 2025 - Present)", font=ImageFont.truetype(INTER_MEDIUM, 20), fill=(130, 230, 255, 255))
draw_exp_m.text((270, 755), "Statistical modelling, regression analysis & reproducible pipelines", font=ImageFont.truetype(INTER_REGULAR, 19), fill=(220, 220, 220, 255))

draw_exp_m.text((270, 800), "Azure AI Certified", font=ImageFont.truetype(INTER_BOLD, 24), fill=(50, 255, 150, 255))
draw_exp_m.text((530, 804), "Microsoft Certified Azure AI Engineer Associate (AI-102)", font=ImageFont.truetype(INTER_MEDIUM, 19), fill=(200, 240, 220, 255))

draw_exp_m.text((270, 850), "Contact me for full experience details*", font=ImageFont.truetype(INTER_REGULAR, 18), fill=(160, 160, 160, 255))

res_exp_m = im_exp_m.rotate(270, expand=False)
res_exp_m.save(f'{OUT_DIR}/aboutMeScreens/bigScreenExperienceMobile.png')


# ----------------------------------------------------
# 5. BIG SCREEN SKILLS (Desktop)
# ----------------------------------------------------
print("Generating bigScreenSkills...")
im_skills = Image.open('oriented_skills.png').convert('RGBA')
draw_skills = ImageDraw.Draw(im_skills)

# Clear left description and right skills cluster in desktop area (y=1000..1800)
draw_skills.rectangle([250, 1000, 1120, 1800], fill=(14, 14, 14, 255))
draw_skills.rectangle([1120, 1000, 1850, 1800], fill=(14, 14, 14, 255))

draw_skills.text((270, 1030), 'Skills', font=ImageFont.truetype(INTER_BOLD, 64), fill=(255, 255, 255, 255))

skills_left = (
    "My technical skills span across Agentic AI, Large Language Models, RAG, "
    "Natural Language Processing, Machine Learning, and AI Automation.\n\n"
    "I focus on building end-to-end intelligent systems, from data preprocessing "
    "and model development to scalable workflow automation and API integrations."
)

y = 1130
for p in skills_left.split('\n\n'):
    for line in textwrap.wrap(p, width=42):
        draw_skills.text((270, y), line, font=ImageFont.truetype(INTER_REGULAR, 23), fill=(230, 230, 230, 255))
        y += 33
    y += 10

# Draw 4 skill categories with cyan headers on right side
categories = [
    ("AI / MACHINE LEARNING", "Python • PyTorch • TensorFlow • Scikit-learn • XGBoost • LoRA / PEFT • YOLO • OpenCV • NLP • ARIMA"),
    ("AI AGENTS & AUTOMATION", "Agentic AI • Intelligent Workflows • RAG Systems • Prompt Engineering • n8n • Power Automate"),
    ("DATA & ANALYTICS", "SPSS • SQL • PostgreSQL • Pandas • NumPy • Hypothesis Testing • Data Pipelines"),
    ("CLOUD & TOOLS", "Azure AI (AI-102 Certified) • Docker • Git • REST APIs • Jupyter • FAISS")
]

y_cat = 1050
for cat_title, cat_skills in categories:
    draw_skills.text((1150, y_cat), cat_title, font=ImageFont.truetype(INTER_BOLD, 26), fill=(0, 255, 240, 255))
    y_cat += 36
    for line in textwrap.wrap(cat_skills, width=48):
        draw_skills.text((1150, y_cat), line, font=ImageFont.truetype(INTER_REGULAR, 20), fill=(225, 235, 240, 255))
        y_cat += 28
    y_cat += 26

res_skills = im_skills.rotate(270, expand=False)
res_skills.save(f'{OUT_DIR}/aboutMeScreens/bigScreenSkills.png')


# ----------------------------------------------------
# 6. BIG SCREEN SKILLS (Mobile)
# ----------------------------------------------------
print("Generating bigScreenSkillsMobile...")
im_skills_m = Image.open('oriented_skills_mobile.png').convert('RGBA')
draw_skills_m = ImageDraw.Draw(im_skills_m)

draw_skills_m.rectangle([250, 560, 1800, 915], fill=(14, 14, 14, 255))

y_m = 565
for cat_title, cat_skills in categories:
    draw_skills_m.text((270, y_m), cat_title, font=ImageFont.truetype(INTER_BOLD, 22), fill=(0, 255, 240, 255))
    y_m += 28
    draw_skills_m.text((270, y_m), cat_skills, font=ImageFont.truetype(INTER_REGULAR, 17), fill=(220, 230, 235, 255))
    y_m += 38

res_skills_m = im_skills_m.rotate(270, expand=False)
res_skills_m.save(f'{OUT_DIR}/aboutMeScreens/bigScreenSkillsMobile.png')


# ----------------------------------------------------
# 7. VENDING MACHINE MENU
# ----------------------------------------------------
print("Generating vendingMachineMenu...")
im_menu = Image.open('decoded_screens/vendingMachineMenu.png').convert('RGBA')
draw_menu = ImageDraw.Draw(im_menu)

project_menu_names = [
    # Row 1 (x centers: 146, 337, 526, 715)
    ("Tender\nIntelligence", 58, 234, 305, 375),
    ("Local RAG\nSystem", 249, 425, 305, 375),
    ("AI Agent\nServices", 438, 614, 305, 375),
    ("User Manual\nAssistant", 627, 803, 305, 375),
    # Row 2
    ("Resume\nScreening", 58, 234, 655, 725),
    ("Language\nDetection", 249, 425, 655, 725),
    ("Loan\nPrediction", 438, 614, 655, 725),
    ("Inventory\nTracking", 627, 803, 655, 725),
]

font_menu = ImageFont.truetype(INTER_BOLD, 17)
for title, x1, x2, y1, y2 in project_menu_names:
    draw_menu.rectangle([x1 + 10, y1, x2 - 10, y2], fill=(156, 255, 222, 255))
    # Draw centered text
    lines = title.split('\n')
    y_t = y1 + (15 if len(lines) == 2 else 25)
    for l in lines:
        w = draw_menu.textlength(l, font=font_menu)
        x_t = x1 + ((x2 - x1) - w) / 2
        draw_menu.text((x_t, y_t), l, font=font_menu, fill=(45, 75, 65, 255))
        y_t += 20

im_menu.save(f'{OUT_DIR}/vendingMachineScreens/vendingMachineMenu.png')


# ----------------------------------------------------
# 8. PROJECTS 1 TO 8 SCREENS
# ----------------------------------------------------
projects_data = [
    {
        "id": 1,
        "menu_name": "Tender\nIntelligence",
        "title": "Enterprise Tender Intelligence & Analysis System",
        "desc": (
            "AI-powered document intelligence system for processing complex tender packages "
            "containing multiple document formats. Implemented document ingestion and content "
            "extraction across PDF, Word, and Excel. Designed workflows for identifying and "
            "structuring tender requirements from large document collections with semantic search, "
            "evidence-based response generation, and validation workflows."
        ),
        "skills": "Python, LLMs, RAG, NLP, Embeddings, Vector Search, AI Automation",
        "image": "extracted_media/image2.jpeg"
    },
    {
        "id": 2,
        "menu_name": "Local RAG\nSystem",
        "title": "Local Retrieval-Augmented Generation (RAG) System",
        "desc": (
            "Developed a local Retrieval-Augmented Generation (RAG) system for intelligent "
            "document processing and context-aware question answering. Built a document ingestion "
            "pipeline supporting PDF, Word, and text documents with chunking and embedding generation. "
            "Integrated FAISS vector similarity search connected to an LLM to generate grounded, "
            "context-aware responses from uploaded knowledge bases."
        ),
        "skills": "Python, RAG, LLMs, NLP, Embeddings, FAISS, Semantic Search",
        "image": "extracted_media/image3.jpeg"
    },
    {
        "id": 3,
        "menu_name": "AI Agent\nServices",
        "title": "AI Agent Services & Intelligent Automation Workflows",
        "desc": (
            "Developed AI agent-based solutions focused on intelligent decision-making, "
            "task automation, and business process support. Contributed to AI Agent services "
            "for client-specific automation and intelligent task execution. Designed multi-step "
            "agentic workflows, automated information retrieval, and API-driven integrations "
            "for practical real-world automation and decision-support use cases."
        ),
        "skills": "Python, AI Agents, Agentic AI, AI Automation, APIs, NLP, Machine Learning",
        "image": "extracted_media/image4.jpeg"
    },
    {
        "id": 4,
        "menu_name": "User Manual\nAssistant",
        "title": "Intelligent User Manual Assistant",
        "desc": (
            "Developed an AI-powered assistant for interacting with technical user manuals "
            "and documentation through natural language. Built document-based question answering, "
            "NLP processing to understand queries and locate relevant sections, and context-aware "
            "grounded answer generation. Integrated document retrieval workflows to simplify access "
            "to complex technical documentation."
        ),
        "skills": "Python, LLMs, NLP, RAG, Semantic Search, Document Processing, AI Automation",
        "image": "extracted_media/image5.jpeg"
    },
    {
        "id": 5,
        "menu_name": "Resume\nScreening",
        "title": "AI-Powered Resume Screening System",
        "desc": (
            "Automated recruitment and resume analysis platform developed during Azure AI training. "
            "Extracts and categorizes candidate qualifications, skills, and experience from resumes "
            "in diverse formats. Employs NLP and similarity matching against job descriptions to rank "
            "candidates objectively and accelerate recruitment pipelines."
        ),
        "skills": "Python, Azure AI (AI-102), NLP, Scikit-learn, Machine Learning, Text Extraction",
        "image": None
    },
    {
        "id": 6,
        "menu_name": "Language\nDetection",
        "title": "Natural Language Detection & Classification System",
        "desc": (
            "Multi-class natural language classification system developed to detect and identify "
            "languages in unstructured text inputs. Uses NLP preprocessing, n-gram vectorization, "
            "and supervised classification models to achieve high accuracy across diverse language pairs."
        ),
        "skills": "Python, NLP, Machine Learning, Text Classification, Scikit-learn",
        "image": None
    },
    {
        "id": 7,
        "menu_name": "Loan\nPrediction",
        "title": "Predictive Loan Eligibility & Risk Assessment System",
        "desc": (
            "Predictive analytics system assessing loan approval likelihood and credit risk. "
            "Built data cleaning, exploratory data analysis (EDA), feature engineering, and "
            "rigorous model validation using statistical classification algorithms to provide "
            "reliable, data-backed financial decision support."
        ),
        "skills": "Python, Machine Learning, Scikit-learn, Pandas, NumPy, Predictive Analytics",
        "image": None
    },
    {
        "id": 8,
        "menu_name": "Inventory\nTracking",
        "title": "Intelligent Inventory Tracking & Demand Forecasting Solution",
        "desc": (
            "Comprehensive inventory tracking and management solution incorporating predictive "
            "stock analysis. Tracks asset movements, prevents stock-outs through automated "
            "reorder thresholds, and provides clear analytics dashboards for operations."
        ),
        "skills": "Python, SQL, PostgreSQL, Data Pipelines, Predictive Analytics",
        "image": None
    },
]

print("Generating project screens 1 to 8...")
for proj in projects_data:
    pid = proj["id"]
    base_file = f'decoded_screens/project{pid}.png'
    im_proj = Image.open(base_file).convert('RGBA')
    draw_p = ImageDraw.Draw(im_proj)

    # 1. Update left thumbnail card label
    draw_p.rectangle([70, 305, 230, 375], fill=(156, 255, 222, 255))
    lines_thumb = proj["menu_name"].split('\n')
    y_th = 315 if len(lines_thumb) == 2 else 325
    for l in lines_thumb:
        draw_p.text((80, y_th), l, font=ImageFont.truetype(INTER_BOLD, 17), fill=(45, 75, 65, 255))
        y_th += 20

    # 2. Update top right screenshot if image exists
    if proj["image"] and os.path.exists(proj["image"]):
        shot = Image.open(proj["image"]).convert('RGB')
        target_w, target_h = 517, 267
        shot_resized = shot.resize((target_w, target_h), Image.Resampling.LANCZOS)
        # Paste at [278, 98]
        im_proj.paste(shot_resized, (278, 98))

    # 3. Update middle card content
    # Clear middle card text area
    draw_p.rectangle([110, 460, 770, 720], fill=(156, 255, 222, 255))

    # Project Title
    font_p_title = ImageFont.truetype(INTER_BOLD, 24)
    draw_p.text((115, 470), proj["title"], font=font_p_title, fill=(35, 65, 55, 255))

    # Project Description
    font_p_desc = ImageFont.truetype(INTER_REGULAR, 15)
    y_d = 508
    for line in textwrap.wrap(proj["desc"], width=72):
        draw_p.text((115, y_d), line, font=font_p_desc, fill=(45, 75, 65, 255))
        y_d += 20
        if y_d > 625:
            break

    # Skills badge and list
    y_badge = 638
    draw_p.rectangle([115, y_badge, 175, y_badge + 26], fill=(35, 65, 55, 255))
    draw_p.text((123, y_badge + 4), "Skills", font=ImageFont.truetype(INTER_BOLD, 14), fill=(255, 255, 255, 255))

    font_p_skills = ImageFont.truetype(INTER_MEDIUM, 15)
    skills_str = proj["skills"]
    draw_p.text((185, y_badge + 4), skills_str, font=font_p_skills, fill=(45, 75, 65, 255))

    im_proj.save(f'{OUT_DIR}/vendingMachineScreens/project{pid}.png')


# ----------------------------------------------------
# 9. ARCADE SCREENS (Credits, Thanks, Default)
# ----------------------------------------------------
print("Generating arcadeScreens...")

def patch_perfect(in_path, out_path, is_credits=False):
    raw = Image.open(in_path).convert('RGBA')
    im = raw.rotate(270)
    grid_copy = im.crop((200, 720, 850, 765))
    im.paste(grid_copy, (200, 800))
    
    if is_credits:
        grid_dev = im.crop((110, 290, 500, 330))
        im.paste(grid_dev, (110, 245))
        grid_mod = im.crop((110, 485, 500, 525))
        im.paste(grid_mod, (110, 438))

    draw = ImageDraw.Draw(im)
    font_copy = ImageFont.truetype(INTER_BOLD, 26)
    copy_text = '© 2026 AFIFA NOOR'
    bbox = draw.textbbox((0, 0), copy_text, font=font_copy)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (1024 - tw) // 2
    ty = 803 + (38 - th) // 2
    draw.text((tx, ty), copy_text, font=font_copy, fill=(255, 255, 255, 255))

    if is_credits:
        font_name = ImageFont.truetype(INTER_BOLD, 28)
        draw.text((120, 248), 'AFIFA NOOR', font=font_name, fill=(255, 255, 255, 255))
        draw.text((120, 442), 'AFIFA NOOR', font=font_name, fill=(255, 255, 255, 255))

    res = im.rotate(90)
    res.save(out_path)

patch_perfect('decoded_screens/arcadeScreenCredits.png', f'{OUT_DIR}/arcadeScreens/arcadeScreenCredits.png', is_credits=True)
patch_perfect('decoded_screens/arcadeScreenThanks.png', f'{OUT_DIR}/arcadeScreens/arcadeScreenThanks.png')
patch_perfect('decoded_arcadeDefault.png', f'{OUT_DIR}/arcadeScreens/arcadeScreenDefault.png')

print("All screen textures successfully generated!")

