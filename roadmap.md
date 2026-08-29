# Roadmap de Desenvolvimento: Simulação Multimodal e IA (Aracaju–São Cristóvão)

Este documento detalha o roadmap de desenvolvimento do projeto, baseado nas fases incrementais definidas na pesquisa. O projeto foi estruturado para ser construído em módulos, de modo que cada fase entregue um produto validável e útil.

## Fase I — Fundamentação
- [ ] Estudo da documentação do Eclipse SUMO e da interface TraCI.
- [ ] Compreensão da modelagem de redes viárias e geração de demanda.
- [ ] Revisão dos algoritmos clássicos de busca em grafos, com foco em A* e Dijkstra.
- [ ] Entendimento das métricas de mobilidade a serem coletadas (tempo de viagem, atraso, throughput, emissões).

## Fase II — Protótipo mínimo
- [ ] Instalação e configuração do ambiente Eclipse SUMO e dependências em Python.
- [ ] Criação de uma rede viária de testes em escala reduzida.
- [ ] Configuração de um cenário básico de simulação.
- [ ] Implementação de um script Python para controlar e interagir com a simulação via TraCI.

## Fase III — Estudo de caso (Modelagem da Rede)
- [ ] Delimitação exata do corredor de estudo (Zona Sul de Aracaju → Campus UFS São Cristóvão).
- [ ] Extração dos dados da malha viária a partir do OpenStreetMap.
- [ ] Conversão dos dados OSM para o formato do SUMO e correções manuais de interseções e permissões.
- [ ] Criação de uma demanda sintética controlada inicial para a rede modelada.

## Fase IV — Baseline (Cenário 0 - Referência)
- [ ] Construção final do Cenário 0, representando a configuração viária atual de forma aproximada.
- [ ] Execução de múltiplas rodadas de simulação controladas para gerar estabilidade estatística.
- [ ] Coleta e tabulação das métricas estabelecidas para criar a linha de base.
- [ ] Validação estrutural e comportamental do cenário.

## Fase V — Cenários Hipotéticos
- [ ] **C1:** Implementação do cenário de prioridade ao Transporte Coletivo (faixas exclusivas, aumento de frequência, prioridade semafórica).
- [ ] **C2:** Implementação do cenário Cicloviário (expansão da infraestrutura, introdução de conversão modal parametrizada).
- [ ] **C3:** Implementação do cenário de Restrição ao Transporte Individual (testes com diferentes níveis de redução da demanda de carros).
- [ ] Validação cruzada e análise de sensibilidade de cada cenário contra a baseline.

## Fase VI — Inteligência Artificial e Roteamento Multimodal
- [ ] Modelagem da rede como um grafo para problemas de busca ($G=(V,E)$).
- [ ] Implementação do algoritmo de Dijkstra próprio integrado ao estado da simulação.
- [ ] Implementação do algoritmo A* com o desenvolvimento de heurísticas.
- [ ] Construção da função de custo multimodal ponderando tempo, distância, transferências e penalidades.
- [ ] Comparação de resultados entre os algoritmos customizados e o roteamento padrão do SUMO.

## Fase VII — Sistemas Baseados em Agentes
- [ ] Definição de perfis e funções de utilidade (orientado a tempo, sensível a transferências, sensível a custo, favorável a modos ativos).
- [ ] Integração do processo de tomada de decisão e escolha modal dos agentes ao início e durante as viagens.
- [ ] Experimentos focados nos comportamentos globais emergentes gerados por preferências heterogêneas.

## Fase VIII — Otimização e Controle
- [ ] Modelagem de um problema de otimização focado no controle semafórico (redução de tempo total, filas e emissões).
- [ ] Implementação de algoritmo Hill Climbing.
- [ ] Implementação de Algoritmos Genéticos.
- [ ] Desenvolvimento de um controlador semafórico adaptativo dinâmico que atua via TraCI.

## Fase IX — Extensões (Modelos de Linguagem e IA Generativa)
- [ ] Implementação do pipeline de dados exportando métricas, tabelas e gráficos para interpretação.
- [ ] Integração com Modelos de Linguagem (LLM) ou Visão-Linguagem (VLM) para análises descritivas.
- [ ] Definição de métricas de avaliação multiobjetivo para determinar trade-offs (e.g. transporte coletivo vs carros).
- [ ] Análise aprofundada de robustez e estabilidade estatística dos dados.

## Fase X — Documentação e Publicação
- [ ] Consolidação final de todos os experimentos.
- [ ] Estruturação formal do banco de dados de simulações.
- [ ] Escrita de artigo científico nos moldes de publicação SBC, com foco na contribuição sobre Simulação Multimodal + Avaliação de Cenários (Fases I a V), ou com expansão para os métodos de IA.
