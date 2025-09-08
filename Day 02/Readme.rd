Chapter 2: Routing Pattern Overview

# Router Agent (LangChain + Gemini)
A demonstration of a multi-agent routing architecture using LangChain and Google Gemini.  
The agent analyzes user input and dynamically routes it to the correct specialized handler.
#Key Concepts
- Coordinator Router → LLM-driven intent classifier.
- Handlers (Sub-Agents):
  - `booking_handler` → Simulates travel booking.
  - `info_handler` → Provides general info.
  - `unclear_handler` → Handles invalid/ambiguous input.
- RunnableBranch → Conditional delegation logic.
