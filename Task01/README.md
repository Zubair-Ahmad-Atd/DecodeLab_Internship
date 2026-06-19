# Rule-Based AI Chatbot 🤖

A simple, deterministic chatbot that responds to predefined user inputs using pure `if-else` / dictionary-based logic. Built as **Project 1** of the DecodeLabs Industrial Training Program (Batch 2026).

This project is the foundation phase before diving into machine learning: instead of probabilistic predictions, every response here is **100% traceable and hard-coded** — given the same input, the bot always produces the same output. No hallucination risk, no black box.

---

## 📖 Project Description

The goal of this project is to build a chatbot that simulates basic human conversation through **explicit control flow and decision-making logic** — not deep learning. The bot runs in a continuous loop, accepts user text input, matches it against a predefined knowledge base of intents, and returns the corresponding response. If no match is found, it falls back to a default "I don't understand" reply, and the conversation ends cleanly when the user types an exit command.

This mirrors a real architectural pattern still used in production AI systems today: **rule-based guardrails** sit in front of (or alongside) probabilistic models like LLMs to provide deterministic, auditable, and safe responses for known cases — a pattern used by frameworks like NVIDIA NeMo and Llama Guard.

---

## 🎯 Key Learning Outcomes

By completing this project, the following skills are demonstrated:

- Designing **control flow** logic to drive program behavior
- Implementing **input sanitization** (case folding, whitespace stripping) to make matching reliable
- Building a **continuous input loop** (`while True`) with a clean exit/kill condition
- Structuring a **knowledge base** as a dictionary (key–value intent mapping) instead of a long if-elif chain
- Using the dictionary `.get()` method to combine **lookup + fallback** in a single atomic operation
- Understanding *why* hash maps (`O(1)` lookup) scale better than if-elif ladders (`O(n)` lookup) as the rule set grows
- Recognizing the **architectural role** rule-based systems play as a deterministic control layer around generative AI

---

## ✨ Features

- Handles common greetings (e.g. `hello`, `hi`) and farewells (`bye`, `exit`)
- Responds to a minimum of 5+ predefined user intents
- Case-insensitive and whitespace-tolerant input matching
- Graceful fallback response for any unrecognized input — the bot never crashes or stays silent
- Runs in a continuous loop, simulating an ongoing conversation
- Clean exit command to break out of the loop and end the session
- Zero external dependencies — built entirely with Python's standard library

---

## 🔄 Project Workflow

The chatbot follows the **Input → Process → Output (IPO)** model:

```
INPUT                         PROCESS                          OUTPUT
─────                         ───────                           ──────
Raw user text         →       Sanitization & Normalization  →   
                               Intent Matching (dict lookup) →   Response Generation
                                                                  (Feedback Loop)
```

### Step-by-step pipeline:

1. **Input Loop** — The program starts a `while True` loop that keeps the "conversation" alive indefinitely.
2. **Sanitization** — Raw user input is cleaned with `.lower().strip()` so that `"Hello"`, `"HELLO "`, and `"hello"` are all treated identically.
3. **Knowledge Base Lookup** — The cleaned input is checked against a dictionary of known intents and their responses.
4. **Fallback Handling** — If no exact match is found, a default response (e.g. `"I do not understand."`) is returned instead of failing silently.
5. **Exit Strategy** — If the input matches a designated exit command (e.g. `"exit"` or `"bye"`), the loop breaks and the program ends cleanly.

---

## 🧠 Concepts Covered

| Concept | Description |
|---|---|
| **Control Flow & Decision-Making** | Using conditional logic to determine program behavior based on input |
| **Deterministic ("White Box") Systems** | Every input maps to a known, traceable output — no hallucination risk, fully auditable |
| **Input Sanitization & Normalization** | Cleaning raw input (`.lower()`, `.strip()`) so matching logic is reliable and case/whitespace-insensitive |
| **The Infinite Loop Pattern** | Using `while True` with a defined "kill command" (`break`) to simulate a persistent, ongoing interaction |
| **The If-Elif Anti-Pattern** | Long `if/elif` ladders have linear (`O(n)`) lookup time and become hard to maintain as rules grow |
| **Hash Maps / Dictionaries** | Using key-value pairs for near-instant (`O(1)`) lookup, regardless of how many rules exist |
| **The `.get()` Method** | Combining lookup and fallback into a single atomic operation: `responses.get(user_input, "default reply")` |
| **Rule-Based Guardrails** | How deterministic, rule-based logic is still used today as a safety/control layer around probabilistic LLMs |
| **From Keys to Vectors** | How this project's exact-match dictionary lookup conceptually evolves into the semantic, vector-based matching used in later (ML-based) projects |

---

## 🛠️ Requirements / Tech Stack

- **Python 3.9+**
- **uv** — fast Python package & project manager (used instead of pip/venv/poetry)
- **VS Code** — development environment
- No external libraries required — built entirely with Python's standard library

---

## 📦 Installation

### Prerequisites
- [Python 3.9+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed

Install uv (if not already installed):

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### Set up the environment

Since this project has no external dependencies, a minimal `uv` setup is enough:

```bash
uv init --no-readme   # only if pyproject.toml doesn't already exist
uv sync
```

---

## 📁 Project Structure

```
.
├── main.py          # Core script: knowledge base, sanitization, input loop, response logic
├── pyproject.toml    # Project metadata (managed by uv)
├── uv.lock           # Locked dependency state
└── README.md         # You are here
```

---

## 🚀 Getting Started

Run the chatbot with:

```bash
uv run main.py
```

You'll see a prompt to start chatting. Type a greeting, ask a known question, or type the exit command to end the session.

---

## 💡 Sample Usage

**Core logic** (the heart of `main.py`):

```python
# Knowledge base: intent -> response mapping
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a bunch of code, but I'm doing great!",
    "what is your name": "I'm a rule-based chatbot built for DecodeLabs Project 1.",
    "bye": "Goodbye! Have a great day.",
}

print("Chatbot is ready! Type 'bye' to exit.")

while True:
    raw_input_text = input("You: ")
    clean_input = raw_input_text.lower().strip()

    if clean_input == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    reply = responses.get(clean_input, "I do not understand. Could you rephrase that?")
    print(f"Bot: {reply}")
```

**Example conversation:**
```
Chatbot is ready! Type 'bye' to exit.
You: Hello
Bot: Hi there! How can I help you today?
You: what is your name
Bot: I'm a rule-based chatbot built for DecodeLabs Project 1.
You: tell me a joke
Bot: I do not understand. Could you rephrase that?
You: bye
Bot: Goodbye! Have a great day.
```

---

## 🛣️ Future Improvements

- [ ] Expand the bot's vocabulary with more intents and synonyms
- [ ] Add nested conditions or multi-turn logic for context-aware responses (e.g. remembering the user's name)
- [ ] Give the bot a distinct personality/tone
- [ ] Add partial/fuzzy matching so close variants of a phrase still match (e.g. "helo" → "hello")
- [ ] Layer this rule-based bot in front of an LLM as a **hybrid architecture** — instant responses for known rules, fallback to an LLM for everything else
- [ ] Move from exact-match dictionary keys toward semantic/vector-based matching (the natural bridge into Project 2 & 3's ML-based approaches)

---

## ✅ Conclusion

This project builds the essential foundation every AI engineer needs before touching machine learning: a deterministic, fully traceable decision system. By mastering control flow, input sanitization, the infinite loop pattern, and efficient lookup with dictionaries, this project proves the ability to design clean, predictable logic — the same "white box" principles that power real-world AI guardrails sitting in front of today's large language models.

Built as part of the **DecodeLabs Industrial Training Kit — Batch 2026, Project 1: Rule-Based AI Chatbot**.

📍 Greater Lucknow, India · 🌎 [decodelabs.tech](https://www.decodelabs.tech)
