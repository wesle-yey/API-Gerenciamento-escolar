#!/usr/bin/env python3
"""
Script para executar testes localmente
"""
import os
import sys
import subprocess
import argparse

def setup_environment():
    """Configura variáveis de ambiente para testes"""
    env_vars = {
        'DATABASE_URL': 'sqlite:///:memory:',
        'SECRET_KEY': 'test_secret_key_for_local_testing',
        'ALGORITHM': 'HS256',
        'ENVIRONMENT': 'test',
        'CORS_ORIGINS': 'http://localhost:3000,http://localhost:8000'
    }
    
    for key, value in env_vars.items():
        os.environ[key] = value
        print(f"✅ {key} = {value}")

def run_tests(test_type="all", verbose=False):
    """Executa os testes"""
    setup_environment()
    
    cmd = ["python", "-m", "pytest"]
    
    if verbose:
        cmd.append("-v")
    
    if test_type == "simple":
        cmd.append("tests/test_simple.py")
    elif test_type == "api":
        cmd.append("tests/test_api.py")
    else:
        cmd.append("tests/")
    
    print(f"🚀 Executando: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True)
        print("✅ Testes executados com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Testes falharam com código {e.returncode}")
        return False

def run_security_checks():
    """Executa verificações de segurança"""
    print("🔒 Executando verificações de segurança...")
    
    # Bandit
    try:
        subprocess.run(["bandit", "-r", ".", "-ll"], check=True)
        print("✅ Bandit: Nenhum problema de segurança encontrado")
    except subprocess.CalledProcessError:
        print("⚠️ Bandit: Problemas de segurança encontrados")
    except FileNotFoundError:
        print("❌ Bandit não encontrado. Instale com: pip install bandit")
    
    # Safety
    try:
        subprocess.run(["safety", "check", "-r", "requirements.txt"], check=True)
        print("✅ Safety: Nenhuma vulnerabilidade encontrada")
    except subprocess.CalledProcessError:
        print("⚠️ Safety: Vulnerabilidades encontradas")
    except FileNotFoundError:
        print("❌ Safety não encontrado. Instale com: pip install safety")

def main():
    parser = argparse.ArgumentParser(description="Script de teste local")
    parser.add_argument("--type", choices=["all", "simple", "api"], default="all",
                       help="Tipo de teste a executar")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Modo verboso")
    parser.add_argument("--security", action="store_true",
                       help="Executar verificações de segurança")
    
    args = parser.parse_args()
    
    print("🧪 Sistema de Gerenciamento Escolar - Testes Locais")
    print("=" * 50)
    
    if args.security:
        run_security_checks()
        print()
    
    success = run_tests(args.type, args.verbose)
    
    if success:
        print("\n🎉 Todos os testes passaram!")
        sys.exit(0)
    else:
        print("\n💥 Alguns testes falharam!")
        sys.exit(1)

if __name__ == "__main__":
    main()
