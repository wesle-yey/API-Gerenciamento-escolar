.PHONY: help install test test-cov lint security clean docker-build docker-run docker-push

help: ## Mostra esta ajuda
	@echo "Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Instala dependências do projeto
	pip install -r requirements.txt
	pip install pytest pytest-cov bandit safety

test: ## Executa testes básicos
	pytest tests/ -v

test-cov: ## Executa testes com cobertura
	pytest tests/ -v --cov=. --cov-report=html --cov-report=term-missing

lint: ## Executa verificação de código
	@echo "Verificando estilo de código..."
	@echo "Instale flake8 para linting: pip install flake8"
	@echo "Execute: flake8 ."

security: ## Executa verificações de segurança
	bandit -r . -f json -o bandit-report.json
	safety check -r requirements.txt --json --output safety-report.json

clean: ## Limpa arquivos temporários
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -delete
	rm -rf .coverage htmlcov/
	rm -rf build/ dist/

docker-build: ## Constrói imagem Docker
	docker build -t gerenciamento-escolar:latest .

docker-run: ## Executa container Docker
	docker run -p 8000:8000 gerenciamento-escolar:latest

docker-push: ## Faz push para Docker Hub (requer login)
	@echo "Fazendo login no Docker Hub..."
	docker login
	@echo "Fazendo push da imagem..."
	docker tag gerenciamento-escolar:latest $(DOCKER_USERNAME)/gerenciamento-escolar:latest
	docker push $(DOCKER_USERNAME)/gerenciamento-escolar:latest

dev: ## Inicia ambiente de desenvolvimento
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

setup: ## Configura ambiente inicial
	python -m venv venv
	@echo "Ative o ambiente virtual: source venv/bin/activate"
	@echo "Instale as dependências: make install"
	@echo "Configure o arquivo .env baseado em env.example"

ci: ## Executa pipeline de CI localmente
	make test-cov
	make security
	make docker-build
	@echo "✅ Pipeline de CI executado com sucesso!"

.PHONY: help install test test-cov lint security clean docker-build docker-run docker-push dev setup ci
