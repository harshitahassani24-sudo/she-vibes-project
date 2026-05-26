# Mommi

A chat-based companion that answers in my mother's voice — so cooking dinner feels less like using an app and more like having the best cook you know in the kitchen with you.

Built during the She Vibes 66-day builder cohort, May–June 2026.

**Live landing page:** [(https://she-vibes-project-drab.vercel.app/)].vercel.app

---

## What It Does

Mommi helps tired working women and hostellers cook healthy, home-style meals on any evening of the week — without the mental load that usually sits between a long workday and an empty kitchen.

You tell Mommi what is in your fridge and how much time you have. It replies with one specific dish, written in my mother's voice, with short and clear steps. Not a recipe app. Closer to a knowing mother on the other end of a chat.

What makes it different is not that it uses AI — many tools do. It is that Mommi is built on one specific person's decades of kitchen wisdom: my mother's. Her warmth, her phrases, her way of making a tired person feel that dinner is small and possible.

---

## Who It Is For

Working women in their twenties and thirties cooking primarily for themselves or a small household. Hostellers and students in shared kitchens with limited time and equipment. Young professionals living alone in cities, who grew up watching someone cook for them and now find themselves in front of a fridge at 9 PM without that person beside them.

Mommi is not built for nutrition optimization. It is built for the quiet kind of care that turns *what should I eat tonight* from a daily defeat into a small, confident answer.

---

## Current State

This is V1, built during the cohort.

**What is live:**

- A public landing page, deployed on Vercel
- The Python agent pipeline: a script that takes a user message, sends it to Google Gemini with a system prompt defining my mother's voice, and returns a thoughtful reply

**What is in development:**

- The Knowledge Base — six markdown files capturing my mother's system, written from recorded conversations with her: voice and tone, pantry and storage, cooking logic by time and mood, substitutions, standard dishes, and refusals
- Telegram bot integration, so real users can message Mommi
- An interactive web version of the agent
- Hosting so the agent stays online independently

---

## How to Set It Up From Scratch

You will need Python 3 and a free Google Gemini API key from [aistudio.google.com](https://aistudio.google.com).

**1. Clone this repository**

`git clone https://github.com/harshitahassani24-sudo/she-vibes-project.git`

`cd she-vibes-project`

**2. Create a virtual environment and activate it**

`python3 -m venv venv`

`source venv/bin/activate`

**3. Install the required libraries**

`pip install google-generativeai python-dotenv requests`

**4. Create a `.env` file in the project root and add your Gemini API key**

`GOOGLE_API_KEY=your-key-here`

The `.env` file is excluded by `.gitignore`, so your key stays private and never reaches GitHub.

**5. Run the agent**

`python3 main.py`

You should see Mommi reply with a cooking suggestion in the terminal.

---

## Technologies Used

**Python** — the language the agent is written in.

**Google Gemini API** — the model that powers Mommi's reasoning and responses.

**HTML and CSS** — the landing page.

**Git and GitHub** — version control and code hosting.

**Vercel** — deployment of the landing page, with automatic redeploys on every push.

**Environment variables** — API keys kept outside the code, in `.env` locally and in Vercel's settings for deployment.

---

## What Is Coming Next

The technical scaffolding is built. The remaining work is mostly writing — the careful translation of how my mother actually thinks about feeding people.

**Now:** Recording conversations with my mother and drafting the Knowledge Base files, beginning with `voice.md` — how she speaks — because every other file has to be delivered in that voice.

**Next:** Connecting a Telegram bot so Mommi has a real channel, then building an interactive web version so anyone can use it from the landing page.

**Goal:** A working V1 of Mommi, used by a small group of real testers, shipped by June 2026.

---

## A Note on the Heart of This Project

The most important file in this project is not the Python code. It is the Knowledge Base — my mother's wisdom, written in her voice. The Python is small and replaceable. The Knowledge Base is irreplaceable. Everything in this build is structured around protecting time for that writing, because it is the part that decides whether Mommi sounds like her or like any other recipe chatbot.

---

## Built By

Harshita — UX Designer by day, writer of Mumma's Archive by evening, and a builder learning to put working systems behind the things she cares about.

Built during She Vibes, May–June 2026.