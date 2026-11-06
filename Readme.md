# Backend Language Selector — Python

A rule-based expert system created for **CM3321 — Logic Programming and Artificial Cognitive Systems**. A Tkinter questionnaire collects project requirements, and Experta rules generate backend-language suggestions with scores and explanations.

This is an educational rule-engine project. Its scores are manually defined heuristics, not measured comparisons of programming languages.

## How it works

1. Answer questions about project type, experience, performance, team size, and development speed.
2. The UI passes the answers to the Experta knowledge engine.
3. Matching rules produce language recommendations and reasons.

## Run locally

The original setup uses Python 3.8 and `experta==1.9.4`. Keep that compatibility environment when reproducing the assignment; compatibility with newer Python versions has not been established here. A graphical desktop and Tkinter are required.

```bash
git clone https://github.com/paranietharan/language-selector-python.git
cd language-selector-python
conda create -n language_selector python=3.8
conda activate language_selector
python -m pip install -r requirements.txt
python -m tkinter
python main.py
```

`python -m tkinter` opens a small test window; close it before launching the application. If it fails, install Tk support for your Python environment. A headless terminal alone cannot display the UI.

## Source guide

| File | Responsibility |
| --- | --- |
| [main.py](main.py) | Create the Tkinter window and start the application |
| [ui.py](ui.py) | Questionnaire, navigation, and results presentation |
| [config.py](config.py) | Question options, colors, and fonts |
| [models.py](models.py) | Facts used by the expert system |
| [expert_system.py](expert_system.py) | Recommendation rules and reasoning |
| [requirements.txt](requirements.txt) | Pinned Experta dependency |

The repository has no automated test suite. To explore the rules, compare the explanations produced by several different answer combinations and inspect the corresponding rules in `expert_system.py`.

The companion [CLIPS version](https://github.com/paranietharan/language-selector) preserves the console-based implementation of this learning topic.
