# ⚽ Dashboard da Copa do Mundo FIFA

Um painel interativo de visualização de dados construído com **Python**, **Dash** e **Plotly**. Esta aplicação fornece uma análise abrangente das partidas da Copa do Mundo da FIFA de 1930 a 2022, apresentando tendências históricas, métricas de desempenho de seleções e comparações diretas (confrontos).

## 📊 Funcionalidades

O dashboard está organizado em quatro abas principais:

1.  **Visão Geral (World Cup Overview)**:
    * Visualização do total de gols por edição da Copa.
    * Agregação de gols por década.
    * Filtro interativo por intervalo de anos.
2.  **Desempenho da Seleção (Team Performance)**:
    * Linha do tempo detalhada de uma seleção específica (Vitórias, Empates, Derrotas).
    * Análise de gols (Gols Pró vs. Gols Contra).
    * Desempenho por fase do torneio (Oitavas, Quartas, Final, etc.).
3.  **Confronto Direto (Head-to-Head)**:
    * Comparação direta entre duas seleções selecionadas.
    * Gráficos de pizza para Vitórias/Derrotas/Empates.
    * Histórico de resultados e placares das partidas.
4.  **Análise de Gols (Goals Analysis)**:
    * Comparação de tendências de gols entre múltiplas seleções.
    * Média de gols por partida em cada edição da Copa.

**✨ Extra:** Alternância de tema Claro/Escuro (Temas Pulse e Cyborg do Bootstrap).

## 🛠️ Tecnologias Utilizadas

* **[Dash](https://dash.plotly.com/)**: Framework principal para a aplicação web.
* **[Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)**: Para layout responsivo e estilização.
* **[Plotly Express](https://plotly.com/python/plotly-express/)**: Para a criação dos gráficos interativos.
* **[Pandas](https://pandas.pydata.org/)**: Para manipulação e processamento dos dados.

## 📂 Estrutura do Projeto

```text
├── matches_1930_2022.csv   # O arquivo de dados (Obrigatório)
├── app.py                  # Script principal da aplicação
├── requirements.txt        # Dependências do Python (Opcional)
└── README.md               # Documentação do projeto
```

## 🚀 Como Executar
Pré-requisitos
Certifique-se de ter o Python instalado (versão 3.7 ou superior).

1. **Instalar Dependências**
Você pode instalar todas as bibliotecas necessárias executando o seguinte comando no terminal
```bash
pip install dash dash-bootstrap-components dash-bootstrap-templates pandas numpy plotly
```
2. **Configuração dos Dados**
Certifique-se de que o arquivo matches_1930_2022.csv esteja localizado na mesma pasta onde está o script Python (app.py).

3. **Executar a Aplicação**
Execute o script principal:
```bash
python app.py
```
