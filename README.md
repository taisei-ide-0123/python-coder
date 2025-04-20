# AgentPro – AI Agent for Python Code Generation & Execution

This repository is an implementation of an AI assistant that generates and executes Python code based on natural language prompts, inspired by the tutorial article below by **Hamza Farooq**:

📄 Article Reference:
[Build Your Agents from Scratch (Part A) – Towards Data Science](https://towardsdatascience.com/build-your-agents-from-scratch-forget-autogen-or-crewai-part-a-a114cd1e785f/)

---

## 🧠 Overview

**AgentPro** is an OpenAI-powered agent that takes user prompts, generates Python code using GPT models, installs necessary libraries, and executes the code — all automatically.

This version is adapted to run **locally** without relying on Google Colab.

---

## 🔧 Features

- Uses OpenAI's GPT model to generate executable Python code
- Automatically detects and installs required Python libraries
- Executes the generated code safely in a temporary environment
- Prints output and error messages to the console

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone git@github.com:taisei-ide-0123/python-coder.git
cd python-coder
```

### 2. Create a `.env` File

Add your OpenAI API key in a `.env` file:

```ini
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 3. Install Required Packages

```bash
pip install openai python-dotenv pillow requests
```

### 4. Run the Script

```bash
python main.py
```

---

## 💬 Example

You can use prompts like the following to generate and execute Python code:

```python
agent.run("""make a detailed deck on the best forms of leadership with at
least 10 slides and save it to a pptx called leadership.pptx""")
```

This will generate a PowerPoint presentation using `python-pptx` and save it as `leadership.pptx`.

---

## ⚠️ Notes

- Generated code is executed automatically — use responsibly and verify outputs.
- OpenAI API usage may incur charges. Please monitor your usage.
- This is a basic prototype. Features like web search, image generation, and decision logic can be added later.

---

## 🛠 Potential Future Enhancements

- Web search integration (e.g., SerpAPI)
- More advanced prompt parsing
- File input/output handling
- GUI or Web-based interface

---

## 🙌 Credits

Original tutorial by **Hamza Farooq**
Article link: [Build Your Agents from Scratch (Part A)](https://towardsdatascience.com/build-your-agents-from-scratch-forget-autogen-or-crewai-part-a-a114cd1e785f/)

---

## 📃 License

MIT License (you can modify this based on your use case)

---

## 📝 Sample Execution Log

```bash
$ python3 main.py
Generating code for: make a detailed deck on the best forms of leadership with at
least 10 slides and save it to a pptx called leadership.pptx
Generated code:

# Required pip installations:
# pip install python-pptx

from pptx import Presentation
from pptx.util import Inches

# Create a presentation object
prs = Presentation()

# Slide 1: Title Slide
slide_1 = prs.slides.add_slide(prs.slide_layouts[0])
title = slide_1.shapes.title
subtitle = slide_1.placeholders[1]
title.text = "The Best Forms of Leadership"
subtitle.text = "Understanding Effective Leadership Styles"

# Slide 2: Introduction
slide_2 = prs.slides.add_slide(prs.slide_layouts[1])
title = slide_2.shapes.title
content = slide_2.placeholders[1]
title.text = "Introduction"
content.text = "Leadership plays a crucial role in guiding teams and organizations. This presentation explores various leadership styles that have proven effective."

# Slide 3: Transformational Leadership
slide_3 = prs.slides.add_slide(prs.slide_layouts[1])
title = slide_3.shapes.title
content = slide_3.placeholders[1]
title.text = "Transformational Leadership"
content.text = "Transformational leaders inspire and motivate their followers to achieve exceptional outcomes by fostering an environment of trust and innovation."

# Slide 4: Servant Leadership
slide_4 = prs.slides.add_slide(prs.slide_layouts[1])
title = slide_4.shapes.title
content = slide_4.placeholders[1]
title.text = "Servant Leadership"
content.text = "Servant leaders prioritize the needs of their team members, focusing on their growth and well-being, which in turn enhances team performance."

# Slide 5: Autocratic Leadership
slide_5 = prs.slides.add_slide(prs.slide_layouts[1])
title = slide_5.shapes.title
content = slide_5.placeholders[1]
title.text = "Autocratic Leadership"
content.text = "Autocratic leaders make decisions unilaterally, providing clear direction and expectations, which can be effective in crisis situations."

# Slide 6: Democratic Leadership
slide_6 = prs.slides.add_slide(prs.slide_layouts[1])
title = slide_6.shapes.title
content = slide_6.placeholders[1]
title.text = "Democratic Leadership"
content.text = "Democratic leaders encourage group participation in decision-making, fostering a sense of ownership and commitment among team members."

# Slide 7: Laissez-Faire Leadership
slide_7 = prs.slides.add_slide(prs.slide_layouts[1])
title = slide_7.shapes.title
content = slide_7.placeholders[1]
title.text = "Laissez-Faire Leadership"
content.text = "Laissez-faire leaders provide minimal direction and allow team members to make decisions, which can lead to high levels of autonomy."

# Slide 8: Charismatic Leadership
slide_8 = prs.slides.add_slide(prs.slide_layouts[1])
title = slide_8.shapes.title
content = slide_8.placeholders[1]
title.text = "Charismatic Leadership"
content.text = "Charismatic leaders use their charm and persuasive communication to inspire and engage their followers, creating strong emotional connections."

# Slide 9: Situational Leadership
slide_9 = prs.slides.add_slide(prs.slide_layouts[1])
title = slide_9.shapes.title
content = slide_9.placeholders[1]
title.text = "Situational Leadership"
content.text = "Situational leaders adapt their style based on the needs of their team and the challenges they face, ensuring flexibility and responsiveness."

# Slide 10: Conclusion
slide_10 = prs.slides.add_slide(prs.slide_layouts[1])
title = slide_10.shapes.title
content = slide_10.placeholders[1]
title.text = "Conclusion"
content.text = "Effective leadership is not one-size-fits-all. Understanding the various styles allows leaders to adapt and apply the best approach for their teams."

# Save the presentation
prs.save('leadership.pptx')

Installing required libraries...
Installing python-pptx...
Collecting python-pptx
  Downloading python_pptx-1.0.2-py3-none-any.whl.metadata (2.5 kB)
Requirement already satisfied: Pillow>=3.3.2 in ./venv/lib/python3.12/site-packages (from python-pptx) (11.2.1)
Collecting XlsxWriter>=0.5.7 (from python-pptx)
  Downloading XlsxWriter-3.2.3-py3-none-any.whl.metadata (2.7 kB)
Collecting lxml>=3.1.0 (from python-pptx)
  Downloading lxml-5.3.2-cp312-cp312-macosx_10_9_x86_64.whl.metadata (3.6 kB)
Requirement already satisfied: typing-extensions>=4.9.0 in ./venv/lib/python3.12/site-packages (from python-pptx) (4.13.2)
Downloading python_pptx-1.0.2-py3-none-any.whl (472 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 472.8/472.8 kB 1.3 MB/s eta 0:00:00
Downloading lxml-5.3.2-cp312-cp312-macosx_10_9_x86_64.whl (4.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 1.1 MB/s eta 0:00:00
Downloading XlsxWriter-3.2.3-py3-none-any.whl (169 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 169.4/169.4 kB 956.9 kB/s eta 0:00:00
Installing collected packages: XlsxWriter, lxml, python-pptx
Successfully installed XlsxWriter-3.2.3 lxml-5.3.2 python-pptx-1.0.2

[notice] A new release of pip is available: 24.0 -> 25.0.1
[notice] To update, run: pip install --upgrade pip
Libraries installed successfully.

Executing code...

```
