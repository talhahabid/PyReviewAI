import os
from dotenv import load_dotenv
from groq import Groq
from utills import readFiles, writeFeedback
load_dotenv()
    
READ_DIRECTORY = "input_files"
WRITE_DIRECTORY = "output_files"
SYSTEM = {
            "role": "system",
            "content": 
                    """
                        You are a code reviewer. Analyze the following Python function and return: 
                        1. A brief quality summary.
                        2. Line-specific comments for any issues.
                        3. A quality rating: Good / Needs Improvement / Buggy
                    """
        }
USER = lambda content: {
    "role": "user",
    "content": f"Here is the function to review:\n\n{content}"
}

input_files = readFiles(READ_DIRECTORY)

client = Groq(api_key=os.getenv("API_KEY"))

for file_name, content in input_files.items():
    chat_completion = client.chat.completions.create(
        messages=[SYSTEM, USER(content)],
        model="llama-3.3-70b-versatile",
    )
    feedback = chat_completion.choices[0].message.content
    writeFeedback(WRITE_DIRECTORY, file_name, feedback)