# ProceduralEquationGeneration
Procedurally generate math questions

---
## Installation
First create a virtual environment, ensuring you're using the most recent version of python (3.9.4 at the time of writing)
and activate the environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

Then install the requirements:

```
pip3 install -r requirements.txt
```

## Adding Dependencies
If you need to add or upgrade any dependencies, upgrade or install them as normal using pip, then run the following command

```
pip freeze > requirements.txt
```

This will overwrite the `requirements.txt` file with the new dependencies.
