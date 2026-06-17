# job_data.py
# This file contains all the job roles and their required skills.
# Think of it as the "database" the system matches resumes against.

JOB_ROLES = {
    # ── DATA & AI ──────────────────────────────────────────────────────────
    "Data Scientist": {
        "skills": ["python", "machine learning", "statistics", "pandas", "numpy",
                   "scikit-learn", "data analysis", "sql", "tensorflow", "pytorch",
                   "data visualisation", "matplotlib", "seaborn", "jupyter",
                   "feature engineering", "model evaluation", "deep learning"],
        "description": "Analyse data, build predictive models, and extract insights using ML techniques."
    },
    "Machine Learning Engineer": {
        "skills": ["python", "machine learning", "tensorflow", "pytorch", "mlops",
                   "docker", "kubernetes", "scikit-learn", "model deployment",
                   "api development", "ci/cd", "git", "deep learning", "nlp",
                   "feature engineering", "cloud", "aws", "gcp"],
        "description": "Build and deploy ML models at scale in production environments."
    },
    "Data Analyst": {
        "skills": ["sql", "excel", "python", "tableau", "power bi", "data visualisation",
                   "statistics", "pandas", "reporting", "dashboard", "google analytics",
                   "data cleaning", "business intelligence", "looker", "r"],
        "description": "Interpret data to help businesses make informed decisions."
    },
    "Data Engineer": {
        "skills": ["python", "sql", "spark", "hadoop", "etl", "airflow", "kafka",
                   "data pipeline", "aws", "azure", "gcp", "databricks", "snowflake",
                   "docker", "kubernetes", "data warehouse", "dbt"],
        "description": "Build and maintain data infrastructure and pipelines."
    },
    "NLP Engineer": {
        "skills": ["python", "nlp", "transformers", "bert", "huggingface", "spacy",
                   "nltk", "text classification", "named entity recognition", "pytorch",
                   "tensorflow", "machine learning", "deep learning", "llm", "rag"],
        "description": "Build systems that understand and generate human language."
    },
    "Computer Vision Engineer": {
        "skills": ["python", "opencv", "deep learning", "pytorch", "tensorflow",
                   "image processing", "object detection", "yolo", "cnn",
                   "image segmentation", "data augmentation", "numpy"],
        "description": "Develop systems that interpret and analyse visual data."
    },
    "AI/ML Research Scientist": {
        "skills": ["machine learning", "deep learning", "research", "pytorch", "tensorflow",
                   "python", "mathematics", "statistics", "paper writing", "experimentation",
                   "reinforcement learning", "nlp", "optimization", "algebra"],
        "description": "Conduct cutting-edge research and push the state of ML forward."
    },
    "Business Intelligence Analyst": {
        "skills": ["sql", "tableau", "power bi", "data visualisation", "reporting",
                   "excel", "dashboard", "business analysis", "kpi", "looker",
                   "data modelling", "etl", "business intelligence"],
        "description": "Transform raw data into actionable business insights via dashboards."
    },

    # ── SOFTWARE ENGINEERING ───────────────────────────────────────────────
    "Software Engineer": {
        "skills": ["python", "java", "javascript", "algorithms", "data structures",
                   "git", "rest api", "sql", "problem solving", "oop",
                   "unit testing", "agile", "docker", "linux"],
        "description": "Design and build software systems and applications."
    },
    "Backend Developer": {
        "skills": ["python", "java", "node.js", "rest api", "sql", "postgresql",
                   "mongodb", "docker", "redis", "microservices", "git",
                   "django", "flask", "fastapi", "spring boot"],
        "description": "Build and maintain server-side logic, databases, and APIs."
    },
    "Frontend Developer": {
        "skills": ["html", "css", "javascript", "react", "vue", "typescript",
                   "responsive design", "git", "ui/ux", "webpack", "nodejs",
                   "rest api", "figma", "accessibility", "performance optimisation"],
        "description": "Build user interfaces and client-side web applications."
    },
    "Full Stack Developer": {
        "skills": ["javascript", "react", "node.js", "python", "sql", "mongodb",
                   "rest api", "html", "css", "docker", "git", "typescript",
                   "postgresql", "aws", "microservices"],
        "description": "Handle both frontend and backend development end-to-end."
    },
    "DevOps Engineer": {
        "skills": ["docker", "kubernetes", "ci/cd", "jenkins", "aws", "azure",
                   "gcp", "terraform", "ansible", "linux", "bash", "git",
                   "monitoring", "prometheus", "grafana", "infrastructure as code"],
        "description": "Bridge development and operations to enable fast, reliable software delivery."
    },
    "Cloud Engineer": {
        "skills": ["aws", "azure", "gcp", "terraform", "kubernetes", "docker",
                   "cloud architecture", "networking", "security", "linux",
                   "infrastructure as code", "ci/cd", "cost optimisation"],
        "description": "Design and manage cloud infrastructure and services."
    },
    "Cybersecurity Analyst": {
        "skills": ["network security", "penetration testing", "siem", "firewalls",
                   "vulnerability assessment", "incident response", "linux",
                   "python", "ethical hacking", "cryptography", "compliance",
                   "threat analysis", "security operations"],
        "description": "Protect systems and networks from cyber threats."
    },
    "Mobile Developer (Android)": {
        "skills": ["kotlin", "java", "android", "android studio", "rest api",
                   "mvvm", "jetpack compose", "git", "firebase", "sqlite",
                   "material design", "unit testing"],
        "description": "Build native Android applications."
    },
    "Mobile Developer (iOS)": {
        "skills": ["swift", "xcode", "ios", "uikit", "swiftui", "rest api",
                   "core data", "git", "firebase", "mvvm", "objective-c"],
        "description": "Build native iOS applications for iPhone and iPad."
    },
    "Embedded Systems Engineer": {
        "skills": ["c", "c++", "embedded systems", "rtos", "microcontrollers",
                   "arduino", "raspberry pi", "firmware", "uart", "spi", "i2c",
                   "debugging", "hardware", "iot"],
        "description": "Program software for embedded hardware and microcontrollers."
    },
    "Blockchain Developer": {
        "skills": ["solidity", "ethereum", "smart contracts", "web3", "blockchain",
                   "python", "javascript", "cryptography", "defi", "nft",
                   "truffle", "hardhat", "ipfs"],
        "description": "Build decentralised applications and smart contracts."
    },
    "QA Engineer": {
        "skills": ["testing", "selenium", "pytest", "test automation", "java",
                   "python", "api testing", "postman", "agile", "bug tracking",
                   "jira", "performance testing", "cypress", "manual testing"],
        "description": "Ensure software quality through testing and automation."
    },

    # ── WEB & DESIGN ───────────────────────────────────────────────────────
    "UI/UX Designer": {
        "skills": ["figma", "ui design", "ux design", "user research", "wireframing",
                   "prototyping", "adobe xd", "sketch", "usability testing",
                   "design thinking", "html", "css", "interaction design"],
        "description": "Design intuitive and visually appealing user experiences."
    },
    "Graphic Designer": {
        "skills": ["adobe photoshop", "illustrator", "indesign", "typography",
                   "branding", "visual design", "colour theory", "figma",
                   "print design", "social media design", "creativity"],
        "description": "Create visual concepts to communicate ideas that inspire audiences."
    },
    "Product Designer": {
        "skills": ["figma", "ux design", "ui design", "prototyping", "user research",
                   "design systems", "wireframing", "product thinking", "data-driven design",
                   "accessibility", "cross-functional collaboration"],
        "description": "Shape product experiences by blending UX, UI, and strategy."
    },

    # ── PRODUCT & MANAGEMENT ───────────────────────────────────────────────
    "Product Manager": {
        "skills": ["product strategy", "roadmap", "agile", "scrum", "user stories",
                   "stakeholder management", "data analysis", "ux", "sql",
                   "market research", "prioritisation", "jira", "go-to-market",
                   "kpi", "customer discovery"],
        "description": "Define product vision and guide cross-functional teams to build great products."
    },
    "Project Manager": {
        "skills": ["project planning", "agile", "scrum", "stakeholder management",
                   "risk management", "ms project", "budget management", "jira",
                   "communication", "leadership", "pmp", "kanban"],
        "description": "Plan, execute, and close projects on time and within budget."
    },
    "Scrum Master": {
        "skills": ["scrum", "agile", "kanban", "jira", "sprint planning",
                   "retrospectives", "coaching", "team facilitation",
                   "conflict resolution", "servant leadership", "csm"],
        "description": "Facilitate agile ceremonies and remove impediments for development teams."
    },

    # ── FINANCE ────────────────────────────────────────────────────────────
    "Financial Analyst": {
        "skills": ["financial modelling", "excel", "valuation", "dcf", "sql",
                   "python", "bloomberg", "financial reporting", "forecasting",
                   "accounting", "budgeting", "powerpoint", "cfa"],
        "description": "Analyse financial data and build models to support business decisions."
    },
    "Quantitative Analyst": {
        "skills": ["python", "r", "statistics", "mathematics", "machine learning",
                   "financial modelling", "stochastic calculus", "derivatives",
                   "risk management", "matlab", "c++", "sql", "bloomberg"],
        "description": "Apply mathematical models to financial markets and risk."
    },
    "Accountant": {
        "skills": ["accounting", "excel", "financial reporting", "taxation", "auditing",
                   "bookkeeping", "quickbooks", "sap", "gaap", "ifrs", "budgeting",
                   "payroll", "reconciliation"],
        "description": "Prepare and maintain financial records and ensure regulatory compliance."
    },

    # ── MARKETING ──────────────────────────────────────────────────────────
    "Digital Marketing Specialist": {
        "skills": ["seo", "sem", "google ads", "social media marketing", "content marketing",
                   "email marketing", "google analytics", "facebook ads", "copywriting",
                   "a/b testing", "marketing automation", "hubspot"],
        "description": "Drive online growth through paid and organic digital channels."
    },
    "SEO Specialist": {
        "skills": ["seo", "keyword research", "google analytics", "ahrefs", "semrush",
                   "on-page seo", "link building", "technical seo", "content strategy",
                   "html", "content writing"],
        "description": "Improve website visibility in search engines."
    },
    "Content Writer": {
        "skills": ["content writing", "copywriting", "seo", "blogging", "editing",
                   "research", "social media", "wordpress", "grammarly",
                   "storytelling", "content strategy"],
        "description": "Create compelling written content for digital and print channels."
    },
    "Social Media Manager": {
        "skills": ["social media marketing", "content creation", "instagram", "linkedin",
                   "twitter", "facebook", "canva", "analytics", "community management",
                   "copywriting", "brand voice", "scheduling tools"],
        "description": "Manage brand presence and audience engagement across social platforms."
    },

    # ── OPERATIONS & HR ────────────────────────────────────────────────────
    "HR Manager": {
        "skills": ["recruitment", "talent acquisition", "employee relations", "payroll",
                   "performance management", "onboarding", "hrms", "labour law",
                   "training and development", "compensation", "conflict resolution"],
        "description": "Manage people operations, recruitment, and employee wellbeing."
    },
    "Operations Manager": {
        "skills": ["operations management", "process improvement", "supply chain",
                   "lean", "six sigma", "budgeting", "team leadership",
                   "vendor management", "kpi", "erp", "logistics"],
        "description": "Oversee day-to-day operations and drive process efficiency."
    },
    "Supply Chain Analyst": {
        "skills": ["supply chain", "logistics", "procurement", "erp", "sap",
                   "inventory management", "demand forecasting", "sql", "excel",
                   "vendor management", "lean", "data analysis"],
        "description": "Optimise supply chain processes and reduce operational costs."
    },

    # ── SCIENCE & RESEARCH ─────────────────────────────────────────────────
    "Bioinformatics Scientist": {
        "skills": ["python", "r", "bioinformatics", "genomics", "sequence analysis",
                   "blast", "machine learning", "statistics", "linux", "biopython",
                   "data analysis", "pipeline development"],
        "description": "Analyse biological data using computational tools and algorithms."
    },
    "Research Scientist": {
        "skills": ["research", "data analysis", "statistics", "python", "r",
                   "experimental design", "paper writing", "literature review",
                   "matlab", "laboratory skills", "critical thinking"],
        "description": "Conduct rigorous scientific experiments and publish findings."
    },

    # ── MISCELLANEOUS TECH ─────────────────────────────────────────────────
    "Database Administrator": {
        "skills": ["sql", "postgresql", "mysql", "oracle", "mongodb", "database design",
                   "query optimisation", "backup and recovery", "replication",
                   "performance tuning", "linux", "scripting"],
        "description": "Manage and optimise database systems for performance and reliability."
    },
    "Network Engineer": {
        "skills": ["networking", "cisco", "routing", "switching", "firewalls", "vpn",
                   "tcp/ip", "dns", "dhcp", "linux", "network security",
                   "ccna", "load balancing", "troubleshooting"],
        "description": "Design and maintain computer network infrastructure."
    },
    "Site Reliability Engineer": {
        "skills": ["sre", "kubernetes", "docker", "python", "monitoring", "prometheus",
                   "grafana", "incident management", "linux", "ci/cd", "bash",
                   "distributed systems", "on-call", "slo/sla"],
        "description": "Ensure reliability, scalability, and performance of production systems."
    },
    "Technical Writer": {
        "skills": ["technical writing", "documentation", "api documentation", "markdown",
                   "git", "editing", "user manuals", "confluence", "xml",
                   "research", "communication", "simplification"],
        "description": "Translate complex technical information into clear documentation."
    },
    "Systems Architect": {
        "skills": ["system design", "cloud architecture", "microservices", "distributed systems",
                   "docker", "kubernetes", "aws", "design patterns", "api design",
                   "scalability", "security", "leadership"],
        "description": "Design high-level structure of complex software systems."
    },
    "Game Developer": {
        "skills": ["unity", "unreal engine", "c#", "c++", "game design", "3d modelling",
                   "opengl", "physics simulation", "git", "python", "blender",
                   "gameplay programming", "shader programming"],
        "description": "Design and develop interactive video game experiences."
    },
    "Robotics Engineer": {
        "skills": ["ros", "python", "c++", "robotics", "computer vision", "sensors",
                   "path planning", "kinematics", "embedded systems", "matlab",
                   "control systems", "simulation"],
        "description": "Design, build, and program robotic systems."
    },
    "IoT Engineer": {
        "skills": ["iot", "embedded systems", "mqtt", "python", "c", "aws iot",
                   "arduino", "raspberry pi", "sensors", "networking",
                   "cloud", "edge computing", "firmware"],
        "description": "Build connected devices and IoT infrastructure."
    },
    "Salesforce Developer": {
        "skills": ["salesforce", "apex", "lightning", "soql", "salesforce administration",
                   "crm", "integration", "visualforce", "rest api", "javascript"],
        "description": "Develop and customise Salesforce CRM solutions."
    },
    "SAP Consultant": {
        "skills": ["sap", "sap fico", "sap mm", "sap sd", "abap", "erp",
                   "business process", "configuration", "integration", "sql"],
        "description": "Implement and optimise SAP ERP solutions for enterprises."
    },
    "Healthcare Data Analyst": {
        "skills": ["sql", "python", "healthcare", "hl7", "fhir", "ehr", "tableau",
                   "statistics", "data analysis", "clinical data", "excel",
                   "hipaa", "reporting", "power bi"],
        "description": "Analyse clinical and operational data to improve healthcare outcomes."
    },
    "Cybersecurity Engineer": {
        "skills": ["network security", "python", "cloud security", "zero trust",
                   "penetration testing", "soc", "siem", "devsecops",
                   "vulnerability management", "identity management", "linux"],
        "description": "Design and implement security systems and defences."
    },
}
