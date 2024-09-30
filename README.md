# Install
´´´
    1) python -m venv .venv
    2) .venv/Scripts/activate
		//Si falla la ejecucion dela mbiente  (Set-ExecutionPolicy Unrestricted -Scope Process)
    3) pip install "fastapi[standard]"

    4)pip freeze > requeriments.txt
	    pip install -r requeriments.txt

# Run 
´´´
    .venv/Scripts/activate
    uvicorn src.main:app --reload

