def getSqlQueryString(sqlFilePath):
    ## Lit un fichier SQL et retourne la requete sous le format d'une string
    with open(sqlFilePath, 'r', encoding='utf-8') as myFile:
        sql_query = myFile.read()

    return sql_query
