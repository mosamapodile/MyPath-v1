# 🚀 MyPath (v1-Core)

> **"Disrupting South African senior phase culture. Every student, every school, one definitive future map."**

MyPath is a gamified, AI-driven career exploration and academic tracking ecosystem designed explicitly for South African Grade 10–12 learners. By processing real-time subject performance alongside structural socio-economic variables (APS scores, NSFAS thresholds, and local market scarcity metrics), MyPath dynamically maps out **Three Definitive Futures** for every student: The Traditional University Route, The TVET Technical Route, and the Direct-to-Market Scarcity Skill Route.

Built as an entry for the **FNB App Academy 2026**, MyPath addresses youth structural unemployment by transforming academic tracking from an administrative chore into cultural social capital.

---

## 🎯 The Vision: Cultural Disruption
In South Africa, millions of pupils enter the matric gates blind to how their term marks translate into tertiary entry requirements or economic participation. Having a MyPath profile is designed to be a status symbol. 
* **Gamified Hustle:** Term marks fuel an algorithmic XP engine. Academic growth equals leveling up.
* **Democratized AI:** High-speed, data-optimized career routing accessible on low-tier mobile networks.
* **National Scale:** Built to handle concurrent traffic spikes when nationwide term marks drop.

---

## 🏗️ System Architecture & Tech Stack

MyPath decouples intensive, expensive LLM data generation from the core application thread to ensure maximum performance under constrained network conditions.

* **Backend Engine:** Python 3.12 / Django 5.0 (Enterprise-ready MVC architecture)
* **API Delivery:** Django REST Framework (DRF) with full token authentication context
* **Task Orchestration:** Celery 5.4 + Redis 5.0 (Asynchronous background worker queue)
* **AI Processing Matrix:** OpenAI GPT-4o-mini API (Hyper-localized prompt engineering templates)
* **Frontend client:** React / Vite / Tailwind CSS (Responsive mobile-first UI wrapper)
* **Database Management:** SQLite3 (Local Dev Core) / PostgreSQL ready

---

## 📂 Repository Layout

```text
mypath_backend/
│
├── config/                  # Core orchestration & system settings
│   ├── settings.py          # Unified system configuration & backend registries
│   ├── celery.py            # Celery broker asynchronous orchestration instantiation
│   └── urls.py              # Root routing registry
│
└── apps/                    # Decoupled core feature applications
    ├── authentication/      # Custom User models & Student XP Profiles
    ├── academics/           # Mark records, Subject definitions, and Gamification Signals
    └── career_ai/           # OpenAI prompt layers & background execution tasks
