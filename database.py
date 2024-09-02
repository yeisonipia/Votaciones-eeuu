import pandas as pd
import sqlite3


def insertar_datos_elections():

    datos = pd.read_json('elections.json')

    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        i = 0
        for d in datos['year']:

            cursor.execute('''
            INSERT INTO Election(year, democrat, republic, other, code_county)
            VALUES(?,?,?,?,?)
            ''', (
                int(datos['year'][i]),
                int(datos['democrat'][i]),
                int(datos['republic'][i]),
                int(datos['other'][i]),
                int(datos['codecounty'][i])
                )
            )

            i+=1
        
        conn.commit()

#insertar_datos_elections()

def insertar_datos_counties():
    with sqlite3.connect('database.db') as conn:
        datos = pd.read_excel('datoslimpios.xlsx')
        cursor = conn.cursor()
        i = 0
        for d in datos['codecounty']:
            cursor.execute(
                '''
                INSERT INTO County(code_county, county, population, area)
                VALUES(?,?,?,?)
                ''', (
                    str(datos['codecounty'][i]),
                    str(datos['county'][i]),
                    float(datos['population'][i]),
                    float(datos['area'][i])
                    )
            )

            i+=1

        conn.commit()


#insertar_datos_counties()