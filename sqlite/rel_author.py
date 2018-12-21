import pandas as pd
import ast
import string
import sqlite3

def make_rel_author(tablename, dbcur, df):
	dbcur.execute("drop table if exists " + tablename)
	dbcur.execute("create table " + tablename + " ("
			+ "recipe_id INTEGER,"
			+ "author TEXT)")
	for i, row in df.iterrows():
		author = ast.literal_eval(row['author'])['name']
		dbcur.execute("insert into " + tablename + " values("
				+ str(row['recipe_id']) + ','
				+ '"' + author + '")')