# Projeto de Pesquisa e Desenvolvimento

## Simulação Multimodal e Avaliação Heurística de Cenários de Mobilidade Urbana: Um Estudo de Caso no Corredor Zona Sul–UFS São Cristóvão

**Área:** Inteligência Artificial, Sistemas Inteligentes e Mobilidade Urbana  
**Local de estudo:** Aracaju e São Cristóvão, Sergipe  
**Plataforma principal:** Eclipse SUMO  
**Linguagem principal:** Python  
**Interface de controle:** TraCI / libsumo  
**Perspectiva de publicação:** Artigo científico no formato SBC

---

## 1. Resumo

Este projeto propõe o desenvolvimento de uma plataforma experimental para simulação e avaliação de diferentes cenários de mobilidade urbana aplicados ao corredor entre a Zona Sul de Aracaju e o Campus da Universidade Federal de Sergipe, em São Cristóvão.

A proposta combina simulação microscópica multimodal de tráfego com técnicas clássicas de Inteligência Artificial, particularmente algoritmos de busca heurística, modelagem baseada em agentes e métodos de otimização. O objetivo inicial não é reproduzir integralmente o sistema viário de Aracaju, mas construir um estudo de caso controlado e progressivamente refinável capaz de investigar os efeitos de diferentes políticas de mobilidade.

O ambiente de simulação escolhido é o Eclipse SUMO (Simulation of Urban MObility), plataforma de código aberto voltada à simulação microscópica e multimodal de tráfego. O SUMO permite representar veículos individuais, transporte público, bicicletas e pedestres, além de importar redes viárias provenientes do OpenStreetMap. A plataforma também oferece mecanismos de roteamento, visualização, cálculo de emissões e controle externo por meio da interface TraCI. 

A arquitetura proposta utiliza Python como camada de orquestração, permitindo executar experimentos, modificar parâmetros da simulação, coletar métricas e posteriormente implementar algoritmos de Inteligência Artificial para tomada de decisão e otimização.

O projeto será desenvolvido de maneira incremental. A primeira etapa será dedicada à construção e validação de um cenário-base. Posteriormente serão introduzidos cenários hipotéticos de mobilidade, busca heurística multimodal, agentes com diferentes funções de utilidade, otimização de controle semafórico e, eventualmente, modelos de linguagem ou visão-linguagem como ferramentas auxiliares de interpretação dos resultados.

A metodologia prioriza reprodutibilidade, controle experimental e documentação adequada, permitindo que o projeto seja desenvolvido inicialmente como estudo exploratório e posteriormente evolua para uma investigação científica formal.

---

# 2. Contextualização

A mobilidade urbana constitui um problema complexo envolvendo infraestrutura, comportamento humano, transporte coletivo, transporte individual, circulação de bicicletas e pedestres, controle semafórico e distribuição espacial da demanda.

Em uma cidade real, alterações em uma determinada política de transporte podem produzir efeitos indiretos em diferentes regiões e modos de transporte. Uma intervenção que reduz o tempo de viagem de automóveis, por exemplo, pode não necessariamente produzir melhoria equivalente para usuários de transporte coletivo ou bicicleta.

A utilização de simulação computacional permite investigar esses efeitos sem a necessidade de modificar fisicamente a infraestrutura urbana.

Nesse contexto, a Inteligência Artificial oferece ferramentas para representar problemas de decisão e otimização associados ao transporte. Algoritmos de busca podem determinar rotas segundo diferentes funções de custo; sistemas baseados em agentes podem representar usuários com diferentes preferências; e algoritmos de otimização podem procurar configurações mais eficientes de infraestrutura ou controle.

O projeto propõe utilizar Aracaju e São Cristóvão como estudo de caso, inicialmente concentrando-se no deslocamento entre a região sul de Aracaju e o Campus da Universidade Federal de Sergipe.

A escolha de um corredor específico reduz o escopo inicial e permite que a metodologia seja validada antes de uma eventual expansão para uma área urbana maior.

---

# 3. Problema de Pesquisa

O problema central pode ser formulado da seguinte maneira:

> Como diferentes políticas hipotéticas de mobilidade urbana alteram o desempenho de um corredor multimodal entre a Zona Sul de Aracaju e o Campus da UFS em São Cristóvão, e como técnicas clássicas de Inteligência Artificial podem auxiliar na escolha de rotas, representação de usuários e otimização dessas políticas?

A pergunta envolve duas dimensões.

### 3.1 Dimensão de simulação

Investigar os efeitos de alterações na infraestrutura e na demanda sobre:

- tempo de viagem;
- tempo de espera;
- atraso;
- velocidade média;
- congestionamento;
- utilização da infraestrutura;
- desempenho do transporte coletivo;
- utilização de bicicletas;
- emissões, quando aplicável.

### 3.2 Dimensão de Inteligência Artificial

Investigar como:

- busca em grafos;
- busca heurística;
- funções de custo;
- agentes;
- otimização;

podem ser utilizados para representar e solucionar problemas de decisão dentro do ambiente simulado.

---

# 4. Hipóteses de Trabalho

O projeto inicialmente considera as seguintes hipóteses.

### H1 — Alterações na distribuição modal produzem efeitos mensuráveis no desempenho do corredor

A redução da participação do transporte individual e o aumento da participação de modos coletivos ou ativos devem alterar o congestionamento, o tempo de viagem e a utilização da infraestrutura.

### H2 — A função de custo utilizada no roteamento influencia significativamente as rotas escolhidas

Uma rota que minimiza exclusivamente o tempo de viagem não necessariamente será a mesma rota que minimiza uma função combinando tempo, distância, número de transferências e outros fatores.

### H3 — Usuários com diferentes funções de utilidade produzem diferentes padrões de utilização da rede

A introdução de agentes com preferências distintas deverá modificar a distribuição dos modos de transporte e, consequentemente, o comportamento global do sistema.

### H4 — Estratégias adaptativas de controle semafórico podem melhorar determinadas métricas do sistema

O controle baseado no estado atual da simulação poderá apresentar desempenho diferente daquele obtido com planos semafóricos fixos.

### H5 — A avaliação de políticas deve considerar múltiplos objetivos

O cenário com menor tempo médio de viagem não necessariamente será o cenário globalmente mais desejável. A análise deverá considerar possíveis trade-offs entre diferentes modos e métricas.

---

# 5. Objetivos

## 5.1 Objetivo Geral

Desenvolver uma plataforma experimental baseada em simulação multimodal para investigar, de maneira quantitativa e reproduzível, diferentes cenários hipotéticos de mobilidade urbana no corredor Zona Sul–UFS São Cristóvão, utilizando técnicas de Inteligência Artificial para roteamento, tomada de decisão e otimização.

## 5.2 Objetivos Específicos

1. Construir uma representação computacional do corredor estudado.
2. Importar e adaptar a infraestrutura viária a partir de dados do OpenStreetMap.
3. Modelar veículos individuais, transporte coletivo e modos ativos.
4. Construir uma demanda inicial de viagens.
5. Estabelecer e validar um cenário-base.
6. Definir métricas quantitativas de avaliação.
7. Implementar algoritmos de Dijkstra e A* para problemas de roteamento.
8. Desenvolver funções de custo multimodais.
9. Modelar agentes com diferentes preferências.
10. Criar cenários hipotéticos de mobilidade.
11. Investigar estratégias de controle semafórico adaptativo.
12. Avaliar métodos de otimização aplicados ao sistema.
13. Automatizar a execução e análise dos experimentos.
14. Manter todos os experimentos documentados e reprodutíveis.
15. Avaliar a possibilidade de utilização de modelos de linguagem ou visão-linguagem como ferramentas auxiliares de interpretação.

---

# 6. Escopo Inicial

O projeto não pretende inicialmente simular toda a cidade de Aracaju.

O primeiro estudo será restrito ao corredor:

**Zona Sul de Aracaju → Campus UFS São Cristóvão**

A delimitação definitiva deverá ser estabelecida após a inspeção da rede viária e dos principais caminhos utilizados pelo tráfego.

Entre os corredores viários candidatos estão:

- Avenida Beira Mar;
- Avenida Tancredo Neves;
- Avenida Melício Machado;
- Avenida Marechal Rondon;
- acessos ao Campus da UFS.

Essas vias constituem inicialmente referências para a delimitação do estudo, não sendo assumido neste estágio que todas deverão necessariamente fazer parte da rede final.

---

# 7. Ambiente de Simulação

## 7.1 Eclipse SUMO

O Eclipse SUMO será utilizado como simulador principal.

O SUMO é um simulador microscópico e multimodal capaz de representar individualmente veículos, transporte público, bicicletas e pedestres. A plataforma também oferece ferramentas para importação de redes, geração de demanda, roteamento, visualização e cálculo de emissões.

A rede viária poderá ser obtida inicialmente através do OpenStreetMap e convertida para o formato utilizado pelo SUMO. A documentação do SUMO apresenta mecanismos específicos para importação de dados OSM e tratamento de interseções e semáforos.

## 7.2 Python

Python será utilizado como linguagem principal para:

- execução dos experimentos;
- controle da simulação;
- implementação dos algoritmos de IA;
- geração da demanda;
- processamento dos resultados;
- análise estatística;
- geração de gráficos;
- gerenciamento dos cenários.

## 7.3 TraCI

A comunicação entre Python e SUMO será realizada inicialmente através do TraCI (Traffic Control Interface).

TraCI permite consultar o estado de objetos da simulação e modificar seu comportamento durante a execução. A API disponibiliza domínios para veículos, pessoas, arestas, faixas, semáforos, pontos de ônibus, rotas e outros componentes.

Isso possibilita uma arquitetura em ciclo:

```text
SUMO
  ↓
estado da simulação
  ↓
Python / algoritmo
  ↓
decisão
  ↓
TraCI
  ↓
SUMO
```

Posteriormente, caso o custo computacional se torne relevante, a implementação poderá migrar para libsumo, que possui as mesmas assinaturas de API do TraCI e evita a comunicação por socket.

---

# 8. Arquitetura Conceitual

A arquitetura geral proposta é:

```text
                  ┌──────────────────────┐
                  │    OpenStreetMap     │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Construção da Rede   │
                  │       SUMO           │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Modelo de Demanda    │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │       SUMO           │
                  │ Simulação Microscóp. │
                  └──────────┬───────────┘
                             │
                       estado atual
                             │
                             ▼
                  ┌──────────────────────┐
                  │       Python         │
                  │  IA / Controle /    │
                  │     Análise         │
                  └──────────┬───────────┘
                             │
                         decisão
                             │
                             ▼
                  ┌──────────────────────┐
                  │       TraCI          │
                  └──────────┬───────────┘
                             │
                             ▼
                        SUMO continua
```

A arquitetura permite separar claramente:

1. infraestrutura;
2. demanda;
3. simulação;
4. inteligência;
5. avaliação.

Essa separação será importante para garantir reprodutibilidade.

---

# 9. Modelagem da Rede

A rede deverá ser obtida inicialmente a partir do OpenStreetMap.

O processo previsto é:

```text
OpenStreetMap
      ↓
dados OSM
      ↓
conversão para SUMO
      ↓
rede viária
      ↓
correções manuais
      ↓
validação
      ↓
rede experimental
```

A importação não deverá ser considerada automaticamente como uma representação perfeita da infraestrutura real.

Deverão ser avaliados:

- interseções;
- sentidos das vias;
- número de faixas;
- limites de velocidade;
- semáforos;
- conexões;
- permissões por tipo de veículo;
- ciclovias;
- calçadas;
- pontos de ônibus;
- conexões entre diferentes modos.

A própria documentação do SUMO alerta para problemas que podem surgir quando interseções próximas não são representadas adequadamente durante a importação OSM, podendo resultar em baixo fluxo, congestionamentos ou deadlocks.

Portanto, a construção da rede será considerada uma etapa de modelagem e não apenas uma operação de conversão.

---

# 10. Modelagem da Demanda

A demanda constitui um dos principais desafios científicos do projeto.

A simulação deverá representar, tanto quanto possível, uma distribuição plausível de viagens.

Serão investigados:

- origem;
- destino;
- horário de partida;
- modo;
- frequência;
- distribuição temporal;
- distribuição modal.

A demanda poderá inicialmente ser construída de maneira sintética, desde que suas hipóteses sejam explicitamente documentadas.

Posteriormente, poderão ser incorporadas informações observacionais ou estatísticas disponíveis.

A estratégia será:

### Versão inicial

Demanda sintética controlada.

### Versão intermediária

Demanda baseada em estimativas e informações disponíveis.

### Versão avançada

Demanda calibrada com dados observacionais.

Essa progressão permite iniciar o projeto sem depender imediatamente da disponibilidade de um conjunto de dados perfeito.

---

# 11. Cenário de Referência

O **Cenário 0 (C0)** representará a configuração de referência.

O objetivo não será afirmar que o modelo reproduz perfeitamente o trânsito real, mas estabelecer uma base experimental contra a qual as demais configurações possam ser comparadas.

O C0 deverá conter:

- tráfego individual;
- transporte coletivo;
- infraestrutura cicloviária disponível;
- semáforos;
- velocidades;
- capacidade das vias;
- demanda temporal;
- rotas iniciais.

A validade do cenário deverá ser discutida considerando as limitações dos dados disponíveis.

---

# 12. Cenários Hipotéticos

## C0 — Referência

Representação da configuração atual aproximada.

Objetivo:

> estabelecer a linha de base.

---

## C1 — Prioridade ao Transporte Coletivo

Possíveis intervenções:

- faixas exclusivas;
- aumento da frequência de ônibus;
- alteração da capacidade viária;
- prioridade semafórica;
- alteração de pontos de parada.

Objetivo:

> avaliar o efeito da priorização do transporte coletivo.

---

## C2 — Cenário Cicloviário

Possíveis intervenções:

- expansão da infraestrutura cicloviária;
- aumento da conectividade;
- redução de conflitos;
- conversão modal hipotética.

A conversão modal deverá ser parametrizada.

Por exemplo:

\[
p_{bike}\in
\{0.1,0.2,0.3,0.4,0.5,\ldots\}
\]

em vez de assumir diretamente uma conversão fixa de 50% ou 70%.

Objetivo:

> determinar como diferentes níveis hipotéticos de adoção da bicicleta modificam o comportamento do sistema.

---

## C3 — Restrição ao Transporte Individual

Em vez de considerar somente "carros proibidos" ou "carros permitidos", poderão ser analisados diferentes níveis:

\[
r\in\{0,0.25,0.50,0.75,1.00\}
\]

onde \(r\) representa a proporção hipotética de redução da demanda individual.

Objetivo:

> investigar a sensibilidade do sistema à redução do transporte individual.

---

## C4 — Controle Semafórico Adaptativo

O controle semafórico será alterado dinamicamente de acordo com o estado observado da simulação.

TraCI permite modificar o estado dos semáforos durante a simulação, possibilitando a implementação de controladores externos.

Exemplo conceitual:

```text
estado do cruzamento
        ↓
fila por aproximação
        ↓
demanda do transporte coletivo
        ↓
controlador
        ↓
nova duração/fase
        ↓
SUMO
```

---

# 13. Inteligência Artificial

## 13.1 Busca em Grafos

A rede urbana poderá ser representada como um grafo:

\[
G=(V,E)
\]

onde:

- \(V\) representa nós ou estados;
- \(E\) representa conexões entre estados.

Cada aresta poderá possuir atributos como:

- distância;
- tempo;
- velocidade;
- modo;
- custo;
- risco;
- necessidade de transferência.

---

# 14. Dijkstra

O algoritmo de Dijkstra será utilizado como método de referência para obtenção do caminho de menor custo quando os custos forem não negativos.

O objetivo não será apenas implementar o algoritmo, mas comparar sua solução com outras funções de custo e com A*.

Métricas possíveis:

- custo final;
- distância;
- tempo computacional;
- número de estados expandidos.

---

# 15. A*

O algoritmo A* será implementado utilizando:

\[
f(n)=g(n)+h(n)
\]

onde:

- \(g(n)\) representa o custo acumulado;
- \(h(n)\) representa a estimativa do custo restante.

A qualidade da heurística será investigada experimentalmente.

Uma heurística simples poderá ser baseada na distância geométrica até o destino.

Posteriormente poderão ser estudadas heurísticas específicas para o problema multimodal.

---

# 16. Função de Custo Multimodal

Uma das principais contribuições potenciais do projeto será a construção de uma função de custo capaz de representar diferentes objetivos.

Uma formulação inicial poderá ser:

\[
C =
w_tT+
w_dD+
w_bB+
w_{tr}N_{tr}+
w_cC
\]

onde:

- \(T\): tempo de viagem;
- \(D\): distância;
- \(B\): penalidade associada ao modo bicicleta;
- \(N_{tr}\): número de transferências;
- \(C\): custo associado à viagem;
- \(w_i\): pesos definidos experimentalmente.

A função poderá posteriormente ser expandida.

O objetivo será investigar como alterações nos pesos modificam as rotas escolhidas.

---

# 17. Roteamento Multimodal

O próprio SUMO possui mecanismos de roteamento intermodal e permite representar viagens envolvendo diferentes modos. A documentação descreve o uso de viagens de pessoas e mudanças de modo, incluindo caminhada e transporte público.

O projeto, entretanto, poderá utilizar uma camada própria de IA para estudar funções de custo diferentes das utilizadas pelo roteamento padrão.

O experimento poderá comparar:

```text
SUMO / roteamento padrão
        ×
Dijkstra próprio
        ×
A* próprio
```

sob diferentes funções de custo.

---

# 18. Sistemas Baseados em Agentes

Os passageiros poderão ser representados por agentes com diferentes preferências.

Exemplos:

### Agente orientado a tempo

\[
U=-T
\]

### Agente sensível a transferências

\[
U=-T-\lambda N_{tr}
\]

### Agente sensível ao custo

\[
U=-T-\lambda C
\]

### Agente favorável à bicicleta

\[
U=-T+\lambda P_{bike}
\]

Cada agente poderá escolher uma alternativa de transporte de acordo com sua função de utilidade.

O objetivo será estudar como decisões individuais podem produzir efeitos emergentes no comportamento global da rede.

---

# 19. Otimização

Em uma etapa posterior, o projeto poderá utilizar métodos de otimização.

Duas alternativas inicialmente consideradas são:

- Hill Climbing;
- Algoritmos Genéticos.

Um possível problema de otimização seria:

> encontrar parâmetros de controle semafórico que minimizem o tempo total de viagem e o congestionamento sem prejudicar excessivamente os demais modos.

Uma função objetivo simplificada poderia ser:

\[
J =
w_1T+
w_2W+
w_3L+
w_4E
\]

onde:

- \(T\): tempo total;
- \(W\): tempo de espera;
- \(L\): perda de tempo/congestionamento;
- \(E\): emissões.

A formulação definitiva deverá ser estabelecida somente após a validação do cenário-base.

---

# 20. Avaliação Multiobjetivo

Um princípio fundamental do projeto será evitar a definição de "melhor cenário" baseada em uma única métrica.

Um cenário pode:

- reduzir congestionamento;
- aumentar tempo de ônibus;
- melhorar bicicleta;
- piorar automóveis.

Portanto, os resultados deverão ser avaliados considerando múltiplas dimensões.

Uma função agregada poderá ser utilizada experimentalmente:

\[
J =
w_1T+
w_2W+
w_3E+
w_4C+
w_5I
\]

onde \(I\) poderá representar algum indicador de distribuição ou equidade.

Os pesos deverão ser explicitamente documentados.

---

# 21. Métricas

As principais métricas inicialmente consideradas são:

### Mobilidade

- tempo médio de viagem;
- tempo total de viagem;
- distância média;
- velocidade média.

### Congestionamento

- tempo de espera;
- perda de tempo;
- comprimento de filas;
- ocupação;
- throughput.

### Transporte coletivo

- tempo médio de viagem;
- atraso;
- tempo parado;
- frequência;
- tempo de transferência.

### Bicicletas

- distância;
- tempo;
- conectividade;
- quantidade de viagens.

### Sistema

- número de viagens concluídas;
- viagens interrompidas;
- tempo computacional;
- estabilidade dos resultados.

O SUMO fornece mecanismos de consulta e coleta dessas informações por meio de suas APIs e arquivos de saída.

---

# 22. Repetibilidade

Simulações de tráfego podem possuir componentes estocásticos.

Portanto, cada cenário deverá ser executado múltiplas vezes com diferentes sementes ou condições controladas.

Para uma métrica \(X\), será possível calcular:

\[
\bar{X}=
\frac{1}{N}
\sum_{i=1}^{N}X_i
\]

e:

\[
\sigma_X=
\sqrt{
\frac{1}{N-1}
\sum_{i=1}^{N}(X_i-\bar X)^2
}
\]

Os resultados deverão ser apresentados preferencialmente como:

\[
\bar{X}\pm\sigma_X
\]

ou através de intervalos de confiança apropriados.

Isso evita que uma única execução seja interpretada como evidência definitiva.

---

# 23. Análise de Sensibilidade

Os parâmetros mais importantes deverão ser submetidos a variações controladas.

Exemplos:

- demanda;
- proporção modal;
- frequência de ônibus;
- capacidade viária;
- percentual de redução de automóveis;
- percentual de conversão para bicicleta;
- pesos da função de custo;
- duração dos ciclos semafóricos.

A análise de sensibilidade será importante para distinguir:

> resultados robustos

de:

> resultados dependentes de uma configuração específica.

---

# 24. Validação

A validação deverá ocorrer em diferentes níveis.

### Validação estrutural

Verificar se:

- as vias estão conectadas;
- os sentidos estão corretos;
- os semáforos funcionam;
- os veículos conseguem completar suas rotas.

### Validação comportamental

Verificar se o comportamento produzido pelo modelo é plausível.

### Validação quantitativa

Quando dados reais estiverem disponíveis, comparar determinadas métricas simuladas com valores observados ou estimados.

O objetivo não será afirmar que o simulador reproduz perfeitamente a cidade, mas identificar em que medida o modelo é adequado para os experimentos propostos.

---

# 25. Modelos de Linguagem e Visão-Linguagem

A utilização de LLMs/VLMs será tratada como uma extensão experimental e não como fundamento da validação científica.

A arquitetura potencial seria:

```text
              SUMO
                │
                ▼
       métricas quantitativas
                │
                ▼
             Python
                │
        ┌───────┴────────┐
        ▼                ▼
     gráficos          mapas
        │                │
        └───────┬────────┘
                ▼
             LLM/VLM
                │
                ▼
       interpretação textual
```

O modelo poderá receber:

- tabelas;
- gráficos;
- mapas;
- estatísticas;
- comparações entre cenários.

Sua função seria:

- identificar padrões;
- auxiliar na interpretação;
- sugerir hipóteses;
- produzir análises qualitativas.

O LLM não deverá ser utilizado como autoridade para determinar qual política é "correta".

A decisão científica continuará baseada nas métricas e nos critérios definidos previamente.

---

# 26. Reprodutibilidade

O projeto deverá ser desenvolvido desde o início considerando sua eventual publicação científica.

Todos os experimentos deverão possuir:

- configuração;
- parâmetros;
- sementes;
- versão do simulador;
- versão das bibliotecas;
- dados de entrada;
- scripts;
- resultados;
- documentação.

Cada cenário deverá poder ser reproduzido através de configuração explícita.

Uma possível organização será:

```text
aracaju-mobility/
│
├── data/
│   ├── osm/
│   ├── demand/
│   └── external/
│
├── sumo/
│   ├── network/
│   ├── routes/
│   ├── scenarios/
│   └── tls/
│
├── src/
│   ├── simulation/
│   ├── routing/
│   ├── agents/
│   ├── optimization/
│   └── analysis/
│
├── experiments/
│
├── results/
│
├── figures/
│
├── docs/
│
├── tests/
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

# 27. Pipeline Experimental

A execução completa poderá seguir:

```text
[1] Dados geográficos
        ↓
[2] Construção da rede
        ↓
[3] Validação da rede
        ↓
[4] Construção da demanda
        ↓
[5] Cenário-base
        ↓
[6] Execução repetida
        ↓
[7] Coleta das métricas
        ↓
[8] Análise estatística
        ↓
[9] Cenários hipotéticos
        ↓
[10] Algoritmos de IA
        ↓
[11] Otimização
        ↓
[12] Comparação
        ↓
[13] Visualização
        ↓
[14] Discussão
```

---

# 28. Cronograma Incremental

O projeto não possui prazo rígido e será desenvolvido paralelamente às disciplinas obrigatórias.

## Fase I — Fundamentação

- estudar SUMO;
- estudar TraCI;
- compreender redes e demanda;
- revisar busca em grafos;
- revisar A* e Dijkstra.

## Fase II — Protótipo mínimo

- instalar SUMO;
- criar uma rede pequena;
- executar uma simulação;
- controlar a simulação com Python.

## Fase III — Estudo de caso

- obter rede de Aracaju/São Cristóvão;
- delimitar o corredor;
- corrigir a rede;
- criar demanda inicial.

## Fase IV — Baseline

- construir C0;
- executar múltiplas simulações;
- coletar métricas;
- validar comportamento.

## Fase V — Cenários

- C1;
- C2;
- C3.

## Fase VI — IA

- Dijkstra;
- A*;
- função de custo multimodal;
- comparação dos métodos.

## Fase VII — Agentes

- definição de perfis;
- funções de utilidade;
- escolha modal;
- experimentos.

## Fase VIII — Otimização

- Hill Climbing;
- algoritmo genético;
- controle semafórico.

## Fase IX — Extensões

- LLM/VLM;
- avaliação multiobjetivo;
- análise de robustez.

## Fase X — Publicação

- consolidação dos experimentos;
- análise;
- documentação;
- artigo SBC.

---

# 29. Riscos e Limitações

## 29.1 Qualidade dos dados

A rede do OpenStreetMap pode não representar perfeitamente a situação observada.

## 29.2 Demanda

A ausência de dados completos de origem-destino pode exigir hipóteses sintéticas.

## 29.3 Calibração

Uma simulação plausível não implica automaticamente que ela esteja calibrada para reproduzir a cidade real.

## 29.4 Complexidade

A combinação de simulação, agentes, busca, otimização e modelos de linguagem pode aumentar excessivamente o escopo.

Por esse motivo, o projeto será desenvolvido de forma modular.

## 29.5 Generalização

Resultados obtidos no corredor estudado não deverão ser automaticamente generalizados para toda a cidade.

A generalização será considerada uma hipótese futura, não uma premissa.

---

# 30. Estratégia de Controle de Escopo

Uma regra fundamental do projeto será:

> **Cada etapa deverá produzir um resultado útil independentemente das etapas seguintes.**

Assim:

```text
SUMO básico
      ↓
resultado válido
      ↓
rede real
      ↓
resultado válido
      ↓
cenários
      ↓
resultado válido
      ↓
A*
      ↓
resultado válido
      ↓
agentes
      ↓
resultado válido
      ↓
otimização
```

Se o projeto precisar ser interrompido em determinada etapa devido às demandas acadêmicas, ainda haverá um produto técnico e científico utilizável.

Essa estratégia também evita que uma extensão experimental comprometa todo o projeto.

---

# 31. Possíveis Contribuições Científicas

Dependendo dos resultados, o projeto poderá produzir contribuições em diferentes níveis.

### Contribuição 1

Uma metodologia reproduzível para simulação de cenários hipotéticos de mobilidade no corredor Aracaju–São Cristóvão.

### Contribuição 2

Uma análise quantitativa dos efeitos de diferentes políticas de mobilidade.

### Contribuição 3

Uma comparação entre algoritmos de busca aplicados ao roteamento multimodal.

### Contribuição 4

Uma função de custo multimodal capaz de representar diferentes preferências.

### Contribuição 5

Uma modelagem baseada em agentes para representar heterogeneidade dos usuários.

### Contribuição 6

Um método de otimização de controle semafórico.

### Contribuição 7

Uma análise experimental da utilização de LLM/VLM como ferramenta auxiliar de interpretação.

As contribuições finais dependerão dos experimentos efetivamente realizados.

---

# 32. Perspectiva de Publicação

O projeto deverá ser estruturado desde o início de maneira compatível com posterior transformação em artigo científico.

Uma estrutura potencial será:

1. Introdução;
2. Trabalhos relacionados;
3. Fundamentação teórica;
4. Metodologia;
5. Área de estudo;
6. Construção da rede;
7. Modelagem da demanda;
8. Cenários experimentais;
9. Métodos de Inteligência Artificial;
10. Métricas;
11. Resultados;
12. Discussão;
13. Limitações;
14. Conclusão.

O primeiro artigo não precisa necessariamente conter todas as extensões previstas.

Uma primeira publicação poderia concentrar-se em:

> **simulação multimodal + cenários + avaliação quantitativa.**

Uma versão posterior poderia incorporar:

> **busca heurística + agentes + otimização.**

---

# 33. Perspectiva de Generalização

Após a validação do estudo de caso, a metodologia poderá ser generalizada.

Possíveis extensões:

- outros corredores de Aracaju;
- outros municípios de Sergipe;
- comparação entre diferentes cidades;
- diferentes matrizes de demanda;
- diferentes políticas de transporte;
- diferentes redes semafóricas.

A generalização deverá ocorrer somente depois da demonstração de que a metodologia funciona adequadamente no estudo de caso inicial.

---

# 34. Estado Inicial do Projeto

O projeto encontra-se atualmente na fase de **concepção e definição metodológica**.

Ainda não devem ser considerados definidos:

- corredor definitivo;
- matriz de demanda;
- parâmetros de tráfego;
- número de veículos;
- distribuição modal;
- funções de custo finais;
- interseções selecionadas;
- algoritmo de otimização definitivo;
- utilização efetiva de LLM/VLM.

Esses elementos deverão ser definidos experimentalmente durante o desenvolvimento.

---

# 35. Princípios Metodológicos

O projeto seguirá os seguintes princípios:

### 1. Incrementalidade

Novas funcionalidades somente serão adicionadas após a validação das anteriores.

### 2. Reprodutibilidade

Experimentos deverão ser reproduzíveis a partir de dados, parâmetros e código documentados.

### 3. Separação entre hipótese e resultado

Parâmetros hipotéticos deverão ser claramente distinguidos de dados observados.

### 4. Avaliação quantitativa

As conclusões principais deverão ser baseadas em métricas mensuráveis.

### 5. Análise de incerteza

Resultados deverão considerar variações e possíveis fontes de incerteza.

### 6. Transparência

Todas as premissas relevantes deverão ser documentadas.

### 7. Controle de escopo

Extensões não deverão comprometer o núcleo funcional do projeto.

---

# 36. Visão de Longo Prazo

A visão de longo prazo é desenvolver uma plataforma experimental capaz de responder perguntas do tipo:

> "O que aconteceria se determinada política de mobilidade fosse aplicada neste corredor?"

A plataforma poderá receber:

```text
rede
+
demanda
+
política
+
parâmetros
```

e produzir:

```text
simulação
+
métricas
+
comparações
+
visualizações
+
análise
```

Em uma versão mais avançada:

```text
                POLÍTICA
                   │
                   ▼
            ┌──────────────┐
            │  Otimizador  │
            └──────┬───────┘
                   │
                   ▼
             ┌───────────┐
             │   SUMO    │
             └─────┬─────┘
                   │
                   ▼
              RESULTADOS
                   │
          ┌────────┴────────┐
          ▼                 ▼
     Estatística        Visualização
          │                 │
          └────────┬────────┘
                   ▼
             INTERPRETAÇÃO
```

Essa arquitetura permitiria que o projeto evoluísse de um simples estudo de simulação para uma plataforma experimental de **Inteligência Artificial aplicada à mobilidade urbana**.

---

# 37. Conclusão

O projeto propõe investigar cenários hipotéticos de mobilidade urbana utilizando uma combinação de simulação microscópica, modelagem multimodal e Inteligência Artificial.

A escolha do Eclipse SUMO fornece uma base adequada para o desenvolvimento porque a plataforma suporta redes importadas do OpenStreetMap, múltiplos modos de transporte, roteamento, visualização e interação externa através de TraCI.

A utilização de Python permite integrar o simulador a algoritmos próprios de busca, agentes, otimização e análise estatística. O TraCI também permite que algoritmos externos observem o estado da simulação e modifiquem elementos durante sua execução, incluindo rotas, veículos e semáforos.

A principal estratégia metodológica será iniciar com um problema pequeno e controlado — o corredor Zona Sul–UFS São Cristóvão — e ampliar gradualmente sua complexidade.

O núcleo mínimo do projeto será constituído por:

\[
\boxed{
\text{SUMO}
+
\text{Rede real}
+
\text{Demanda}
+
\text{Cenários}
+
\text{Métricas}
}
\]

A primeira camada de Inteligência Artificial será:

\[
\boxed{
\text{Dijkstra}
+
A^*
+
\text{Função de custo multimodal}
}
\]

Posteriormente poderão ser adicionados:

\[
\boxed{
\text{Agentes}
+
\text{Otimização}
+
\text{Controle adaptativo}
}
\]

e, como extensão experimental:

\[
\boxed{
\text{LLM/VLM}
}
\]

Essa organização permite que o projeto seja desenvolvido de maneira independente do calendário das disciplinas obrigatórias, sem estabelecer a necessidade de concluir todas as extensões para que exista um resultado científico válido.

A perspectiva final é que o projeto produza não apenas uma simulação específica, mas uma metodologia documentada, reprodutível e extensível para investigar políticas de mobilidade urbana por meio de Inteligência Artificial e simulação computacional.