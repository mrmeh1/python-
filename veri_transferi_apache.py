#!/usr/bin/env python
# coding: utf-8

# In[ ]:


cpVar = 'mssql-jdbc-6.2.1.jre7.jar:' + "mssql-jdbc-6.2.1.jre7.jar"
# sql server için gerekli jar dosyası 


# In[ ]:


cpVar2 = 'postgresql-42.2.20.jar:' 
# postgresql için gerekli jar dosyası 


# In[ ]:


import os 
import pandas as pd 
from pyspark.sql import SparkSession 


# In[ ]:


# oturum nesnesini oluşturma 


# In[ ]:


spark = SparkSession     .builder     .master("local[*]")     .config("spark.driver.extraClassPath", cpVar)     .config("spark.executorEnv.CLASSPATH", cpVar)     .appName("Spark Veri Gönderme")     .getOrCreate()


# In[ ]:


# csv dosyasını okuma 


# In[ ]:


df = spark.read.format("csv").option("delimiter", ";").load("file.csv")
df.show()


# In[ ]:


df = df.withColumnRenamed("_c0","column1")     .withColumnRenamed("_c1","column2")     .withColumnRenamed("_c2","column3")     .withColumnRenamed("_c3","column4")     .withColumnRenamed("_c4","column5")     .withColumnRenamed("_c5","column6")
df.show()


# In[ ]:


# veri setinin veri tabanları ortamına eklenmesi 


# In[ ]:


df.write.format("jdbc")     .mode("append")     .option("url", f"jdbc:sqlserver://xxx.xx.xx.xx\\ServerName:Port;databaseName=
DBname")     .option("dbtable", "TableName")     .option("user", "userName")     .option("password", "pass")     .save()


# In[ ]:


df.write.format('jdbc').options(
url='jdbc:postgresql://localhost:port/test?currentSchema=schema',
driver='org.postgresql.Driver',
dbtable='table_name',
user='postgres',
password='Password').mode('append').save()


# In[ ]:




