import os
import re
import subprocess
import tempfile
import importlib
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class AgentPro:
    def __init__(self):
        pass

    def generate_code(self, prompt):
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Python code generator. Respond only with executable Python code, no explanations or comments except for required pip installations at the top."
                },
                {
                    "role": "user",
                    "content": f"Generate Python code to {prompt}. If you need to use any external libraries, include a comment at the top of the code listing the required pip installations."
                }
            ],
            max_tokens=4000,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        code = re.sub(r'^```python|^```|```$', '', response.choices[0].message.content, flags=re.MULTILINE)
        code_lines = code.split('\n')
        while code_lines and not (
            code_lines[0].startswith('import') or
            code_lines[0].startswith('from') or
            code_lines[0].startswith('#')
        ):
            code_lines.pop(0)

        return '\n'.join(code_lines)

    def install_libraries(self, code):
        libraries = re.findall(r'#\s*pip install\s+([\w\-]+)', code)
        if libraries:
            print("Installing required libraries...")
            for lib in libraries:
                try:
                    importlib.import_module(lib.replace('-', '_'))
                    print(f"{lib} is already installed.")
                except ImportError:
                    print(f"Installing {lib}...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            print("Libraries installed successfully.")

    def execute_code(self, code):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
            temp_file.write(code)
            temp_file_path = temp_file.name

        try:
            result = subprocess.run(['python', temp_file_path], capture_output=True, text=True, timeout=30)
            output = result.stdout
            error = result.stderr
        except subprocess.TimeoutExpired:
            output = ""
            error = "Execution timed out after 30 seconds."
        finally:
            os.unlink(temp_file_path)
        return output, error

    def run(self, prompt):
        print(f"Generating code for: {prompt}")
        code = self.generate_code(prompt)
        print("Generated code:\n")
        print(code)

        self.install_libraries(code)

        print("\nExecuting code...")
        output, error = self.execute_code(code)

        if output:
            print("Output:\n", output)
        if error:
            print("Error:\n", error)

# --- 実行部 ---
if __name__ == "__main__":
    agent = AgentPro()
    agent.run("""make a detailed deck on the best forms of leadership with at
least 10 slides and save it to a pptx called leadership.pptx""")
