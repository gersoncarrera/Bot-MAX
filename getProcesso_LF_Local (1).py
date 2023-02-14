import PIconnect as PI
import pandas as pd
import requests as req
from datetime import datetime
import json
import time
import pyodbc


#def getProcesso_LF():
#    data = datetime.now()
#    data_hora_atual = data.strftime('%d/%m/%Y %H:%M:%S')
#
#    list_number = ['ID_grupo1','ID_grupo2']
#
#    list_group = ['name_grupo1', 'name_grupo2']
#   
#
#    url = 'https://v5.chatpro.com.br/chatpro-fz3tdgy4xu/api/v1/send_message'

#    Headers = {'accept': 'application/json',
#               'Authorization': '759bpq7z1gt0meo61157lt2b7z44q0',
#               'Content-Type': 'application/json'
#               }    
   

with PI.PIServer('FLIPTOP72') as server:

    # fabrica 1
    PRODUCAO_DIGESTOR = server.search('121FIX001')[0].current_value
    PRODUCAO_BRANQUEAMENTO = server.search('124FQ023D')[0].current_value
    KAPPA_DIGESTOR = server.search('123AT004B1.1')[0].current_value
    KAPPA_DESLI_in = server.search('123AT004C1.1')[0].current_value
    KAPPA_DESLI_out = server.search('123AT004D1.1')[0].current_value
    VISCOSIDADE_DIGESTOR = server.search('CV208108')[0].current_value
    VISCOSIDADE_DESLI = server.search('OV171108')[0].current_value
    VISCOSIDADE_PA = server.search('BV43108')[0].current_value
    ALVURA_ENTR_BQTO = server.search('125AT019A2.1')[0].current_value
    ALVURA_ESTAG_EOP = server.search('125AT019B2.1')[0].current_value
    ALVURA_ESTAG_D1 = server.search('125AT019C1.1')[0].current_value
    NIVEL_BLOW = server.search('122LT009')[0].current_value
    CARGA_ALCALINA_TOTAL_DIG = server.search('121AIC748')[0].current_value
    CAT_ClO2 = server.search('125AIC001D')[0].current_value
    CARGA_H2O2_H1 = server.search('S125CA043')[0].current_value
    TEOR_REJEITOS_DIG = server.search('S121MA004')[0].current_value
    PALITOS_26_DEP = server.search('122SU026419')[0].current_value
    PALITOS_27_DEP = server.search('122SU027419')[0].current_value
    PALITOS_28_DEP = server.search('122SU028419')[0].current_value
    PALITOS_29_DEP = server.search('122SU029419')[0].current_value
    PALITOS_62_DEP = server.search('122SU062419')[0].current_value
    KAPPA_PRE_BRANQ = server.search('123AT004C1.1')[0].current_value 
    #    
    # fabrica 2
    PRODUCAO_DIGESTOR2 = server.search('321ACTPROD')[0].current_value
    PRODUCAO_BRANQUEAMENTO2 = server.search('325FY124')[0].current_value
    KAPPA_DIGESTOR2 = server.search('321AI110')[0].current_value
    KAPPA_DESLI_in2 = server.search('322AI005')[0].current_value
    KAPPA_DESLI_out2 = server.search('324AI005')[0].current_value
    VISCOSIDADE_DIGESTOR2 = server.search('L2-321HS501108')[0].current_value
    VISCOSIDADE_DESLI2 = server.search('L2-322HS008108')[0].current_value
    VISCOSIDADE_PA2 = server.search('BV92108')[0].current_value
    ALVURA_ENTR_BQTO2 = server.search('322AI005B')[0].current_value
    ALVURA_ESTAG_EOP = server.search('325ALV_EST_EOP')[0].current_value
    ALVURA_ESTAG_D1 = server.search('325AI051A')[0].current_value
    NIVEL_BLOW2 = server.search('331LT200')[0].current_value
    CARGA_ALCALINA_TOTAL_DIG2 = server.search('321SUMAW')[0].current_value
    CAT_ClO2_2 = server.search('ESP_CLO2LG')[0].current_value
    CARGA_H2O2_H2 = server.search('ESP_H2O2LG')[0].current_value
    TEOR_REJEITOS_DIG = server.search('S321MA011')[0].current_value
    PALITOS_401_DIGESTOR = server.search('L2-324ED4014019')[0].current_value
    PALITOS_402_DIGESTOR = server.search('L2-324ED4024019')[0].current_value
    
     print('PRODUCAO_DIGESTOR')      