import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")
if GEMINI_KEY is None:
    raise ValueError("Missing GEMINI_KEY")

client = genai.Client(api_key=GEMINI_KEY)

def filter_contents(content: str) -> str:
    result = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=[types.Part.from_text(text="""
        You are the perfect filtering and a parsing program. You will filter
        and parse text exactly as described.
                                                 
        You will receive the raw transcript. From there, keep any 
        information about the schedule like class time, and due dates of 
        assignment. Remove everything else. This will be used to setup 
        the calendar and the todo list for the user. Do not include any
        other things.""")]
        ),
        contents=[
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=f"""{content}""")]
            )
        ])

    if result.text is None:
        raise ValueError("Missing text result, Result: ", result)
    
    return result.text

# *   **Course:** (79-364) The Birth of Modern Childbirth, 1600 to the Present
# *   **Meeting Times:** Tuesday & Thursday, 9:00 AM - 10:20 AM
# *   **Location:** Cyert Hall A70
# *   **Instructor Office Hours:**
#     *   Tuesdays, 10:30 AM - 11:30 AM (Cyert Hall 120)
#     *   Wednesdays, 1:30 PM - 2:30 PM
#     *   By appointment

# **Assignment Due Dates:**

# *   **Online Reflection Post 1:** March 25th, 8:00 PM
# *   **Comments on Reflection Posts 1:** March 26th, 8:00 PM
# *   **Online Reflection Post 2:** April 1st, 8:00 PM
# *   **Comments on Reflection Posts 2:** April 2nd, 8:00 PM
# *   **Perspective Paper Proposal:** April 11th
# *   **Online Reflection Post 3:** April 8th, 8:00 PM
# *   **Comments on Reflection Posts 3:** April 9th, 8:00 PM
# *   **Perspective Paper Presentations:** April 18th
# *   **Online Reflection Post 4:** April 15th, 8:00 PM
# *   **Comments on Reflection Posts 4:** April 16th, 8:00 PM
# *   **Question for Panelists (4/25):** April 22nd, 8:00 PM
# *   **Online Reflection Post 5:** May 1st, 9:00 AM
# *   **Comments on Reflection Posts 5:** May 2nd, 9:00 AM
# *   **Question for Panelists (5/4):** May 3rd, 9:00 AM
# *   **Final Perspective Paper:** May 9th, Noon
