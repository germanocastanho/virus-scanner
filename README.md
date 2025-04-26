# 🦠 Virus Scanner

Script simples em Python para **escanear arquivos** - e futuramente, quem sabe, URLs! - em busca de vírus e outras espécies de malwares. Este projeto é uma demonstração do potencial da API do [**VirusTotal**](https://www.virustotal.com/), que contando com a análise de inúmeros antivírus, proporciona alta confiabilidade dos resultados. 🔍

# 🚀 Funcionalidades

- **Scanner de Arquivos**: 🕵️ Escaneamento de arquivos em busca de vírus e outras espécies de malwares.
- **Alta Confiabilidade**: 🎯 Análise realizada por mais de 70 antivírus e ferramentas de segurança.
- **Interface Simples**: 🎨 Interação através de linha de comando, proporcionando praticidade às análises.

# ✅ Pré-requisitos

- Python 3.12 ou superior, disponível através do [**site oficial**](https://www.python.org/downloads/).
- Chave API do VirusTotal, acessível através da [**plataforma**](https://www.virustotal.com/gui/my-apikey).
- Arquivo `.env` com a variável `VT_API_KEY` configurada.

# 🛠️ Instalação Local

```bash
# Clone o repositório
git clone https://github.com/germanocastanho/virus-scanner.git

# Acesse o diretório
cd virus-scanner

# Configure um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o script "main.py"
python3 main.py
```

# 📜 Software Livre

Distribuído sob a [Licença GPLv3](LICENSE), garantindo liberdade de uso, modificação e redistribuição do software, desde que preservadas estas liberdades em quaisquer versões derivadas. Utilizando ou contribuindo, você apoia a filosofia de **software livre** e auxilia a construção de um ambiente tecnológico libertário! ✊
