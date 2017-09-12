""" Módulo RETORNO
Descrição: Este módulo provê funções de retorno em tempo discreto e contínuo.
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

########## Função Retorno Contínuo
def retorno_continuo(preco):
    i = 0
    retcont = [mt.mt.log(preco[i+1]/preco[i]) for i in range(length(preco))]
    return retcont    


########## Função Retorno Discreto
def retorno_discreto(preco, preco_anterior):
    retdisc = [[preco[i + 1]/preco[i] -1 for in in range(preco)]
    return retdisc 
 
 
 
 





########## Processamento de dados

betas =
residuos =





########## Saída de dados
