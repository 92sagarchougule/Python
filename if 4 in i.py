import arcpy
from arcpy import env
env.workspace = r'D:\Villages'
flist = arcpy.ListFeatureClasses()
for i in flist:
    if('4.shp' in i):
        print(i)
        
for i in flist:
    if('20' in i):
        print(i)
        

