""" Programa CAPM
Descrição: Este programa implementa o modelo de
apreçamento de ativos de Sharpe (1964).
Autor: Nelson Seixas dos Santos
Data: 15/12/2016
Versão: 0.0.1
""

########## Importação de módulos
import math as mt
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mp
import retorno as ret

########## Definição de classes





########## Definição de funções
def beta(acao):
    preco = np.array([])
    b = np.cov(retorno_continuo(preco), retorno_continuo(market_portfolio_value))
    return b
