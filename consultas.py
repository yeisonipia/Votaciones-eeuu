import sqlite3
import pandas as pd

with sqlite3.connect('database.db') as conn:
    
    cursor = conn.cursor()

    #--¿Cuál fue el año en que se realizaron más votaciones?
    consulta1 ='''
        SELECT year, 
        sum(democrat) + sum(republic) +sum(other) as votes_total
        FROM Election
        GROUP BY year
        '''

    datos1 = pd.read_sql_query(consulta1,conn)
    datos1.to_excel('año + votaciones.xlsx')

    #¿Cuál fue el condado con menos votaciones en el 2008?
    consulta2 = '''
    SELECT c.county,
    sum(e.republic) + sum(e.democrat) + sum(e.other) as votes
    FROM Election e
    JOIN County c
    ON c.code_county = e.code_county
    WHERE e.year = 2008
    GROUP BY c.code_county
    ORDER BY votes
    LIMIT 4
    '''
    datos2 = pd.read_sql_query(consulta2, conn)
    datos2.to_excel('condado - votaciones 2008.xlsx')

    #Cuáles fueron los 3 condados que tuvieron más votaciones por el partido demócrata en los años del 2000 al 2008?

    consulta3 = '''
    SELECT c.county,
    sum(e.democrat) as votes
    FROM Election e
    JOIN County c
    ON c.code_county = e.code_county
    WHERE e.year BETWEEN 2000 AND 2008 
    GROUP BY c.code_county
    ORDER BY votes DESC
    LIMIT 3

    '''
    
    datos3 = pd.read_sql_query(consulta3, conn)
    datos3.to_excel('3 condados + votos democratas.xlsx')

    #votaciones totales

    consulta4 = '''
    SELECT year,
    sum(democrat) as Democrat,
    sum(republic) as Republic,
    sum(other) as Others,
    sum(democrat) + sum(republic) +sum(other) as votes_total
    FROM Election
    GROUP BY year
    '''
    
    datos4 = pd.read_sql_query(consulta4, conn)
    datos4.to_excel('votos totales.xlsx')

