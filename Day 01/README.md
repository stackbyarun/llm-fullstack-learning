Chapter 01 ----  Prompt Chaining
#Gemini LLM + LangChain Example

This show's how  Python to extract information from text and transform it into structured JSON output

Technologies Used
- Python 3.13
- LangChain (`langchain_core`, `langchain_google_genai`)
- Google Gemini LLM (`gemini-1.5-flash`) Gemini pro (Student acess)
- Environment Variables for API Key management
- JSON for structured output

---

 What the Code Does

1. Input a text string describing technical specifications (e.g., CPU, RAM, storage).  
2. Extract technical specifications using a prompt chain in LangChain.  
3. Transform the extracted data into JSON with keys `cpu`, `memory`, and `storage`.  
4. Print the JSON output.

Example Input:
```text
The new laptop model features a 3.5 GHz octa-core processor, 16GB of RAM, and a 1TB NVMe SSD.
