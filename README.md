Extração de XML
Ferramenta web para extrair arquivos XML de uma pasta (incluindo subpastas) e compactá-los automaticamente em um arquivo .zip para download.
O que faz
O usuário seleciona uma pasta pelo navegador. A ferramenta varre todos os arquivos, filtra apenas os .xml e gera um resultado.zip pronto para baixar — tudo isso sem precisar instalar nada.
Linguagens e tecnologias

HTML, CSS e JavaScript — interface e lógica no navegador
JSZip — biblioteca para compactação dos arquivos no frontend
Python com Flask — versão alternativa com processamento no servidor

Para quem é feito
Voltado para operadores e gestores de PDV (Ponto de Venda) que precisam reunir arquivos XML fiscais (como NF-e e NFC-e) espalhados em pastas e subpastas, de forma rápida e sem conhecimento técnico.

🗂️ Estrutura do Projeto
projeto/
│
├── templates/
│   └── index.html       # Interface web (frontend)
│
├── index.py             # Servidor Flask (backend)
├── uploads/             # Pasta temporária de processamento (gerada automaticamente)
└── README.md

👤 Autor
Desenvolvido por Igor.
