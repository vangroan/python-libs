
check-venv:
ifndef VIRTUAL_ENV
	@echo "ERROR: No virtual environment activated."
	@exit 1
endif
ifdef VIRTUAL_ENV
	@echo "Virtual environment active."
endif

init: check-venv
	pip install -qU pip setuptools
	pip install -e libraries/logctx
