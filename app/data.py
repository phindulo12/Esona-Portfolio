def get_profile():
    return {
        "name": "Esona Mzalazala",
        "title": "BSc Teaching Graduate | Emerging Education Professional",
        "headline": "Shaping confident learners with creative lesson design and inclusive classroom leadership.",
        "bio": [
            "Recent BSc Teaching graduate with strong experience in curriculum planning, classroom culture, and student-centered instruction.",
            "I design engaging learning experiences that honor diversity, encourage curiosity, and build meaningful academic progress.",
            "Focused on blending evidence-based pedagogy with digital tools to support every student's growth."
        ],
        "specialties": [
            "Differentiated lesson design",
            "Inclusive classroom strategies",
            "Assessment & reflective teaching",
            "Learning technology integration"
        ],
        "experience": [
            {
                "role": "Student Teacher",
                "organization": "Riverstone Academy",
                "dates": "Jan 2024 - Jun 2024",
                "details": "Led interdisciplinary units in literacy and science, building strong learner engagement through cooperative inquiry and student reflection."
            },
            {
                "role": "Teaching Assistant",
                "organization": "Learning Lab Institute",
                "dates": "Jul 2023 - Dec 2023",
                "details": "Supported differentiated instruction, tracked student progress, and collaborated with teachers to strengthen classroom routines and formative assessment."
            }
        ],
        "education": [
            {
                "degree": "BSc in Teaching",
                "institution": "State University of Education",
                "dates": "2024"
            }
        ],
        "projects": [
            {
                "slug": "inclusive-stem-curriculum",
                "name": "Inclusive STEM Curriculum",
                "description": "Designed an accessible, inquiry-based unit that invited learners to investigate real-world problems and reflect on their own learning process.",
                "detail": "This project guided students through an interactive STEM inquiry cycle, using hands-on experiments and reflective writing to build strong conceptual understanding and academic confidence.",
                "highlights": [
                    "Designed differentiated learning pathways for diverse learners.",
                    "Used formative reflections to fuel student growth.",
                    "Connected science concepts to real-world challenges."
                ]
            },
            {
                "slug": "digital-classroom-hub",
                "name": "Digital Classroom Hub",
                "description": "Created a student-centered digital hub for formative feedback, portfolios, and family communication to support continuous learning.",
                "detail": "This project developed a classroom hub where students showcased learning artifacts, families received updates, and teachers shared real-time progress to strengthen home-school partnerships.",
                "highlights": [
                    "Built an accessible portfolio workflow for student reflection.",
                    "Improved engagement with consistent family communication.",
                    "Supported data-informed planning through formative tracking."
                ]
            },
            {
                "slug": "adaptive-reading-lab",
                "name": "Adaptive Reading Lab",
                "description": "Built a reading lab experience that adjusted reading levels and scaffolded comprehension for each learner.",
                "detail": "The Adaptive Reading Lab combined small-group coaching, leveled texts, and student-led discussions that prioritized fluency, meaning-making, and confidence.",
                "highlights": [
                    "Scaffolded instruction through targeted small-group rotations.",
                    "Used student data to drive next-step reading goals.",
                    "Encouraged peer collaboration with guided discussion cycles."
                ]
            },
            {
                "slug": "community-learning-showcase",
                "name": "Community Learning Showcase",
                "description": "Created a showcase event where learners shared projects, reflections, and family connections with confidence.",
                "detail": "This project cultivated learner agency by inviting students to present work, reflect on growth, and celebrate learning with families and community partners.",
                "highlights": [
                    "Designed a strengths-based presentation protocol.",
                    "Centered student voice in exhibition planning.",
                    "Promoted family engagement through meaningful celebration."
                ]
            }
        ],
        "contact": {
            "email": "esona.mzalazala@example.com",
            "linkedin": "linkedin.com/in/esona-mzalazala",
            "portfolio": "esona-teachfolio.com"
        }
    }


def get_lessons():
    return [
        {
            "title": "Inquiry-based Literacy Studio",
            "description": "A reading and writing workshop that connected storytelling, research, and peer collaboration to deepen literacy confidence."
        },
        {
            "title": "STEAM Exploration Lab",
            "description": "A hands-on science unit that encouraged student investigation, hypothesis testing, and creative presentation through classroom engineering challenges."
        },
        {
            "title": "Digital Learning Showcase",
            "description": "A blended learning sequence where learners used digital tools to document progress, reflect on growth, and present learning products."
        }
    ]


def get_testimonials():
    return [
        {
            "quote": "Esona brings warmth, structure, and a thoughtful spirit to every lesson. Their planning is always grounded in student voice.",
            "author": "Mentor Teacher, Riverstone Academy"
        },
        {
            "quote": "A strong collaborator who adapts quickly and builds trust with learners. Esona’s classroom environment is welcoming and ambitious.",
            "author": "Instructional Coach, Learning Lab Institute"
        }
    ]


def get_project(slug):
    profile = get_profile()
    return next((project for project in profile["projects"] if project["slug"] == slug), None)
