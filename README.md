# Mom Agent

A chat-based companion that translates my mother's lifetime of home-cooking wisdom into something that sits in a tired person's pocket.

Built during the She Vibes 66-day builder cohort, May–June 2026.

---

## What It Does

Mom Agent helps working women and hostellers cook healthy, home-style meals on any evening of the week — without the mental load that usually sits between a long workday and an empty kitchen.

A user describes what is in their fridge and how much time they have. The agent replies with one specific dish, written in my mother's voice, with short and clear steps. Not a recipe app. Closer to a knowing aunt on the other end of a chat.

The agent draws on a structured Knowledge Base — currently in development — that captures my mother's decades-old system across six dimensions: voice and tone, pantry and storage, cooking logic by time and mood, substitutions, standard dishes, and refusals (the things she would not engage with, like calorie-focused questions).

---

## Who It Is For

Working women in their twenties and thirties cooking primarily for themselves or a small household.

Hostellers and students in shared kitchens with limited time and equipment.

Young professionals living alone in cities, who grew up watching someone cook for them and now find themselves in front of a fridge at 9 PM without that person beside them.

The agent is not built for nutrition optimization. It is built for the quiet kind of care that turns *what should I eat tonight* from a daily defeat into a small confident answer.

---

## Current State

This is V1, built during weeks 5–9 of the cohort. The Python pipeline is working: a script takes a user message, sends it to Google Gemini with the system prompt that defines my mother's voice, and returns a thoughtful reply.

**What is in place:**

- Python script (`main.py`) calling the Gemini API
- First sketch of my mother's voice in the system prompt
- A small GitHub API exploration script (`github_api.py`) from a learning exercise

**What is still being built:**

- The full Knowledge Base files, written from recorded conversations with my mother
- Telegram bot integration so real users can message the agent
- A logging system to track agent responses against my mother's actual judgment
- Hosting so the bot stays online when my laptop is closed

---

## How to Run It Locally

You will need Python 3 and a free Google Gemini API key from [aistudio.google.com](https://aistudio.google.com).

**1. Clone this repository**

`git clone https://github.com/harshitahassani24-sudo/she-vibes-project.git`

`cd she-vibes-project`

**2. Create a virtual environment and activate it**

`python3 -m venv venv`

`source venv/bin/activate`

**3. Install the required libraries**

`pip install google-generativeai python-dotenv requests`

**4. Create a `.env` file in the project folder and add your Gemini API key**

`GOOGLE_API_KEY=your-key-here`

**5. Run the script**

`python3 main.py`

You should see Mom Agent reply with a cooking suggestion in the terminal.

---

## What Is Coming Next

The technical pipeline is built. The remaining work is mostly writing — the careful translation of how my mother actually thinks about feeding people.

**Week 7** — Two recorded conversations with my mother. First drafts of `voice.md` and `pantry.md`.

**Week 8** — Three more conversations. Drafts of `cooking-logic.md`, `substitutions.md`, `dishes.md`, and `refusals.md`. Telegram bot connected so the agent has a real channel.

**Week 9** — Three to five real test users from the people I know. Feedback gathered. Highest-impact fixes made. Agent shipped by June 9, 2026.

---

## Principles Guiding This Build

A few quiet commitments locked in early, while the project was still small enough for the right choices to be easy.

The agent collects the minimum data needed to function. No conversation history, no user profiles, no eating patterns stored.

The agent will not be monetized through advertising, affiliate links, or sponsored ingredients. A tired person at 9 PM is in a state of low resistance, and the agent exists to relieve that depletion, not exploit it.

The agent is designed to make users more capable and independent over time, not more dependent on it. Success is a user who eventually does not need the agent because she has internalized the system it taught her — the way a real mother's teaching works.

My mother is an active participant in shaping how her voice and system are represented. Her decades of work are the foundation of everything the agent will do.

---

## A Note on the Voice

The most important file in this project is not the Python code. It is the Knowledge Base — six markdown files containing my mother's wisdom, written in her voice, currently being drafted from recorded conversations with her.

The Python is small and replaceable. The Knowledge Base is irreplaceable. Everything in this build is structured around protecting time for the writing of those files, because that is the part that decides whether Mom Agent sounds like her or like any other recipe chatbot.

---

## Built By

Harshita — Senior UX Designer by day, writer of Mumma's Archive by evening, and now a builder learning to put working systems behind the things she cares about.

Built during She Vibes, May–June 2026.