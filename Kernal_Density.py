#------------------------------------------------------------------------------------------
# Name:        verma_priyanka_07
# Purpose:     ArcGIS Toolbox creates a heat map using Kernal Density Tool in ArcGIS
#              Clips the heat map to borough boundaries shapefile
#              to exclude areas outside of NYC from final output raster.
#              Uses data of injuries in NYC Streets from 2009-2015 in Vector(Points) format
# Author:      pverma
# Created:     10/20/2015
# Copyright:   (c) pverma 2015
#-------------------------------------------------------------------------------------

import arcpy
import os
import sys
from arcpy import env


env.workspace = arcpy.GetParameterAsText(2) #get workspace as folder
env.overwriteOutput = True

# Variables
inFeatures = arcpy.GetParameterAsText(0)
populationField = "NONE"
outputFile = "kd_injuries"
Rectangle = "-74.2571589747994 40.4959922059092 -73.6992151836567 40.9155675849701" # X-Minimum, Y-Minimum, X-Maximum, Y-Maximum
clipFile = arcpy.GetParameterAsText(1)
finalOutput = "kd_clip"
cellSize = "1.65196575079179E-03"

try:

    # KernelDensity 
    outKernelDensity = arcpy.sa.KernelDensity(inFeatures, populationField, cellSize,"", "SQUARE_MAP_UNITS")

    #Save raster created
    outKernelDensity.save(env.workspace +"\kd_injuries")

    #clip raster to NYC Bounds
    arcpy.Clip_management(outputFile, Rectangle, finalOutput, clipFile, "", "ClippingGeometry", "NO_MAINTAIN_EXTENT")

except Exception as e:
    # Displays messages in ArcGIS output
    arcpy.AddMessage(e)


