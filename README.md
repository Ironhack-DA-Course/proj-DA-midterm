# Project overview
...

# Installation

1. **Clone the repository**:

```bash
git clone https://github.com/YourUsername/repository_name.git
```

2. **Install UV**

If you're a *MacOS/Linux* user type:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If you're a *Windows* user open an Anaconda Powershell Prompt and type :

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

3. **Create an environment**

```bash
uv venv 
```

3. **Activate the environment**

```bash
python -m ipykernel install --user --name=venv
```

Activate enviroment *everytime* working on project:


If you're a *MacOS/Linux* user type:

Bash shell
```bash
source ./venv/bin/activate
```

Csh/Tcsh shell:

```bash
source ./venv/bin/activate.csh
```

If you're a *Windows* user type:

PS Shell
```bash
.\venv\Scripts\activate
```
Git Bash
```bash
source ./venv/Scripts/activate
```
4. **Install dependencies**:

when requirements.txt/pyproject.toml exists
```bash
uv pip install -r requirements.txt
```

from scratch and add manually new package/lib
```bash
uv add package_name
```

# Questions 
...

# Dataset 
Evaluate yahoo api to retrieve history news -> not available for a long timeframe

...

## Main dataset issues

- ...
- ...
- ...

## Solutions for the dataset issues
...

# Conclussions
...

# Next steps
...
