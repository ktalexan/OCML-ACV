###################################################################
#     ArcGIS Analysis for Azure Cognitive Vision Photospheres     #
# ---------------------- Anaheim Area ----------------------------#
# Version 3 for ArcGIS Pro (arcpy) and ArcGIS Python API (arcgis) #
###################################################################



#--------------- Reference Definitions ---------------#

# Importing project libraries
import os, arcpy, json, statistics
from tqdm import tqdm

# Define project directories for data, the ArcGIS Pro map, and the default project geodatabase
basename = os.environ['OneDriveConsumer']
prjdata = os.path.join(basename, r'Professional\Projects\OCPW\OCML\ACVML')
prjcode = os.path.join(prjdata, r'Programming\acvmlpy')
os.chdir(prjdata)
prjagp = os.path.join(basename, r'Professional\GIS Data\OCGIS\OCML\OCMLAnaheim')
agpname = 'OCMLAnaheim'
area = 'Anaheim'

# Importing the python ocml module library for the acvgis class (ocml.acvgis, must be in the same directory with this python file)
os.chdir(prjcode)
from ocml.acvgis import acvgis

# Setting the working directory at the data location, and defining the list of sub-areas for the focal processing area.
os.chdir(prjdata)
anaheimList = ['anaheim2018337p1', 'anaheim2018338p1', 'anaheim2018338p2']



#--------------- Geoprocessing Operations ---------------#

# Initialize the class object for the Anaheim area data
azg = acvgis(anaheimList, area, prjdata, prjagp, agpname)

# Create new domains in the project's geodatabase
azg.CreateDomains()

# Create feature datasets in the project's geodatabase
azg.CreateDatasets()

# Add the geoJSON strings from Azure's Cognitive Vision detection process (ocml.acvml) as a feature class in the geodatabase
azg.AddGeoJSON()

# Creating cardinal feature classes (for direction 1).
azg.CreateCardinalFeatures()

# Merge all the sub-area feature classes (photospheres and cardinals)
azg.MergeAreas()

# Identify features with stop signs and fire hydrants and generate feature classes containing only these points
azg.ProcessDetections()

# Create point cluster analyses (50 feet distance, at least 2 points per cluster, and DBSCAN algorithm) and return a response object containing all the point clusters containing stop signs and fire hydrands respectively.
responseStopSigns = azg.CreatePointClusters('StopSigns', 'AnaheimCardinals1StopSigns', 50)
responseFireHydrants = azg.CreatePointClusters('FireHydrants', 'AnaheimCardinals1FireHydrants', 50)

# Generate new object feature classes using the clustering response detections from the previous step
azg.CreateObjectFeatures('AnaheimCardinals1StopSignsFPC', responseStopSigns)
azg.CreateObjectFeatures('AnaheimCardinals1FireHydrantsFPC', responseFireHydrants)



