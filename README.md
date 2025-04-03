# Install
´´´
    1) python -m venv .venv
    2) .venv/Scripts/activate
		//Si falla la ejecucion dela mbiente  (Set-ExecutionPolicy Unrestricted -Scope Process)
    3) pip install "fastapi[standard]"
        python -m pip install fastapi
        python -m pip install uvicorn

    4)pip freeze > requeriments.txt //Este es para generar por primera vez
	    pip install -r requeriments.txt //Si ya esta generado no se ejecuta el anterior
        //En caso de que falle
        python -m pip install -r requirements.txt

# Daa Base
  Port 3306

# Run 
´´´
    .venv/Scripts/activate
    uvicorn src.main:app --reload

    python -m uvicorn src.main:app --reload

# Docs
