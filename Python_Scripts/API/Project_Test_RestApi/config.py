import os
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))
params = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};SERVER=GSESPHV3S1R\SQL2012;DATABASE=Package_Manager_API;Trusted_Connection=yes;')
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params