""" Módulo RETORNO
Descrição: Este módulo provê funções de retorno em tempo discreto e contínuo.
Autor: Nelson Seixas dos Santos
Data: 15/12/2016
Versão: 0.0.1
""

########## Importação de módulos
import numpy as np

########## Função Retorno Contínuo
def retorno_continuo(preco):
# A variável 'preco' deve ser um numpy array.
    i = 0
    retcont = np.insert(np.array([np.log(preco[i+1]/preco[i]) for i in range(len(preco)-1)]), 0, 0)
    return retcont    


########## Função Retorno Discreto
def retorno_discreto(preco):
# A variável 'preco' deve ser um numpy array.
   i = 0
    retdisc = np.insert(np.array([(preco[i + 1]/preco[i] -1) for i in range(len(preco)-1)]),0, 0) 
    return retdisc 
 
 
 
 



