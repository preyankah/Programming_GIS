#------------------------------------------------------------------------------------------
# Name:        verma_priyanka_04
# Purpose:     Uses data of injuries in NYC Streets from 2009-2015 in Vector(Points) format
#              Creates a heat map using Kernal Density Tool in ArcGIS
#              Clips the heat map to borough boundaries shapefile
#              to exclude areas outside of NYC from final output raster
# Author:      pverma
# Created:     10/20/2015
# Copyright:   (c) pverma 2015
#-------------------------------------------------------------------------------------

import arcpy
from arcpy import env
from arcpy.sa import *

#Edit Path to Data
env.workspace = "C:\Users\pverma\Desktop\Verma_Priyanka_06\Data"

# Variables
inFeatures = "injury_all_monthly.shp"
populationField = "NONE"
outFile = "kd_injuries"
Rectangle = "-74.2571589747994 40.4959922059092 -73.6992151836567 40.9155675849701" # X-Minimum, Y-Minimum, X-Maximum, Y-Maximum
clipFile = "nybb.shp"
inFile2 = "kd_injuries"
finalOutput = "kd_clip"


# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")
print("Exists")

# KernelDensity
outKernelDensity = KernelDensity(inFeatures, populationField)
print("Heat Map Created")

# Save the output
outKernelDensity.save(env.workspace+ "\kd_injuries")
print("Heat Map Saved")

arcpy.Clip_management(inFile2, Rectangle, finalOutput, clipFile, "", "ClippingGeometry", "NO_MAINTAIN_EXTENT")
print("Heat Map Clipped")
