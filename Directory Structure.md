gruvetube/
│── .env  # Configurations
│── docker-compose.yml  # Container definition
│── requirements.txt  # Python dependencies
│── src/  # Application source code
│   │── app.py  # Flask entry point
│   │── config.py  # Load .env variables
│   │── models.py  # Database models
│   │── routes/  # Flask routes
│   │   │── admin.py  # Admin panel routes
│   │   │── downloads.py  # Download queue routes
│   │   └── playback.py  # Playback settings
│   │── static/  # CSS/JS
│   │── templates/  # HTML templates
│── data/  # Persistent storage
│   │── videos/  # Video files
│   │── music/  # Audio-only files
│── extensions/  # Optional future plugins
└── README.md  # Documentation
