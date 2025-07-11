# Project overview - Credit Risk Data Analysis 

With the new policy and reserved fund, our bank aims to offer existing customers some credit product. 
The objective is minimizing risk by avoiding loans to customers classified as high-risk with poor credit scores. 
This strategy will be also implemented by targeting and acquiring good customers.

We did the data cleaning using pandas functions such as .replace,map function etc.., then export it as a CSV.
In order to analyse the data we used groupby in pandas with aggregate functions.
With the results from the functions we have created some visualizations also.

- Dataset: https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data
- Slides : https://docs.google.com/presentation/d/12ohVUDCfmn3gUf3rh3gCu7MOkmfEcNccA44wJ2z5fxo/edit?slide=id.gd1bf8d60a4_0_0#slide=id.gd1bf8d60a4_0_0
- Trello : https://trello.com/invite/b/6867ef71ab27315759d757cd/ATTI1e226f0a98ffdaf5d9a4ceedebdde02792D91D40/my-trello-board

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
- Loans taken for business and education is more riskier than other loans
- If customers has a problem in their credit history they will likely classified as bad score
- Accounts with no checking accounts are most likely critical accounts
- Credit score changes based on identity (e.g., gender,marital status,age etc.) 

# Dataset 
German Credit Data – 1,000 customer records with features like loan purpose, credit history, checking account status, ...

## Main dataset issues

- Encoded data to decode
- Inconsistent string formats (capitalization, spacing)
- Multi-label values (e.g., “male/single,female/divorced etc.”)


## Solutions for the dataset issues

- Renamed and standardized columns
- Converted string values to lowercase
- Grouped and aggregated for ratio analysis
- Using lower case to clean text
- Map functions to change from attributes to variables
- Lambda functions for flagging key credit risk indicators

# Conclussions

- ❌ Business and education most riskly group -> new car and furniture are the part of our risky group
- ❌ Customers with problem in their credit history are likely to have bad score -> Customers, who paid back duly, are among the risky group
- ✅ No checking account correlates with critical history  -> Strongly supported
- ❌ Young applicants show highest bad rate -> Male: divorced/separated and female: married/divorced are the riskiest segments.


# Next steps
- Expand the project to connect with SQL
- Update data
