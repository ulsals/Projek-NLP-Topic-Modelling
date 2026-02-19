---
trigger: always_on
---

---
description: Defines the correct Conda environment and terminal execution rules for the AI Agent.
---

# Conda Environment Configuration

You are working within a specific Conda environment on a Windows machine. Whenever you need to execute Python code, run tests, or manage packages, you MUST strictly adhere to the following rules:

1. **Execution Method (Mandatory):** DO NOT attempt to activate the environment using `conda activate`. Instead, use the `conda run` command to execute all Python scripts directly within the target environment.
   - **Environment Name:** `ml_ds_stable`
   - **Command Format:** `conda run -n ml_ds_stable python <script_name.py>`
   - **Example:** `conda run -n ml_ds_stable python main.py`

2. **Direct Interpreter Path (Fallback):** If `conda run` fails, you MUST use the absolute path to the Python executable for this specific Conda environment. DO NOT use the global `python` command.
   - **Path:** `C:\Users\Batara\miniconda3\envs\ml_ds_stable\python.exe`
   - **Example:** `C:\Users\Batara\miniconda3\envs\ml_ds_stable\python.exe script.py`

3. **Package Management:** When installing new dependencies via terminal, ensure they are installed into the correct environment (but always ask when you need to installing new dependeccies).
   - **Using Conda:** `conda install -n ml_ds_stable <package_name>`
   - **Using Pip:** `conda run -n ml_ds_stable pip install <package_name>`

4. **Working Directory:** Ensure all commands are executed from the project root: `D:\File Mata Kuliah\Semester 6\NLP\Projek-NLP-Topic-Modelling`.