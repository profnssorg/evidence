#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classe CAPM
Description: This class represents the capital asset pricing model due to 
Sharpe (1964). It also has methods to price asset in accordance with 
Black (1972).

References:
BLACK, F. (1972). "Capital Market Equilibrium with Restricted Borrowing".
Journal of Business, 45. pp 444-454.

Sharpe, W.(1964)."Capital Asset Prices: a theory of market equilibrium under
conditions of risk". Journal of Finance, 19, pp. 425-442. 

Author: Nelson Seixas dos Santos
Date: 15/12/2016
Versão: 0.0.1
"""




import numpy as np
import pandas as pd
from scipy import stats

bovespa = pd.Series()
cdi = pd.Series()


log_bovespa = np.log(bovespa) 
return_bovespa = log_bovespa.diff()
risk_premium = return_bovespa - cdi


class Capm(asset):
    def __init__(self, asset):
        self.asset = asset
        self.risk_premium = risk_premium
    
    def beta_Sharpe():
        beta_Sharpe = stats.lin(a)
        
    def alpha_Jensen():
        alpha_Jensen = stats.lin(a)
    
    def 
        


########## Importação de módulos
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels as sm




########## Class definition

class Capm:
	def Sharpe(asset_return, risk_free, market_return):
    """ Retorna o valor do coeficiente beta do CAPM de Sharpe (1964).
    Suas entradas são, respectivamente, a séries de retornos do ativo, da taxa de juros livre de risco
    e do retorno da carteira de mercado.  As séries são estrutura de dados Pandas. """
    asset_return = pd.Series()
    risk_free = pd.Series()
    market_return = pd.Series()
    excess_return = asset_return - risk_free
    risk_premium = market_return - risk_free
    beta = linregress(excess_return, risk_premium)
    alpha = linregress(excess_return, risk_premium)
    epsilon = pd.Series()
    sigma = 
    return(beta)





def black():
    """Retorna o valor do coeficiente beta do CAPM de Black (1972).
    Suas entradas são, respectivamente, as séries de de retornos do ativo e do retorno da carteira de
    mercado.  As sérias são estrutura de dados Pandas. """


       
        