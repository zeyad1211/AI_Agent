import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types






def main():
    load_dotenv()

    verbose = '--verbose' in sys.argv
    args = []  
    # print(args)
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    # print(user_prompt)
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    response_obj = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    response_txt = response_obj.text
    print(response_txt)

    prompt_tokens = response_obj.usage_metadata.prompt_token_count
    response_tokens = response_obj.usage_metadata.candidates_token_count

    if verbose:
        print(f"User prompt: {user_prompt[:-1]}")
        print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}")
    # print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}")
if __name__ == "__main__":
    main()
