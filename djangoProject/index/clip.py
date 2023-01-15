# -*- coding: utf-8 -*-
import os
import numpy as np
from osgeo import gdal, gdalnumeric, ogr, osr, gdal_array
gdal.UseExceptions()

def world2Pixel(geoMatrix, x, y):
  """
  Uses a gdal geomatrix (gdal.GetGeoTransform()) to calculate
  the pixel location of a geospatial coordinate
  """
  ulX = geoMatrix[0]
  ulY = geoMatrix[3]
  xDist = geoMatrix[1]
  yDist = geoMatrix[5]
  rtnX = geoMatrix[2]
  rtnY = geoMatrix[4]
  pixel = int((x - ulX) / xDist)
  line = int((ulY - y) / xDist)
  return (pixel, line)

#
#  EDIT: this is basically an overloaded
#  version of the gdal_array.OpenArray passing in xoff, yoff explicitly
#  so we can pass these params off to CopyDatasetInfo
#
def OpenArray( array, prototype_ds = None, xoff=0, yoff=0 ):
    # ds = gdal.Open( gdalnumeric.GetArrayFilename(array))
    ds = gdal_array.OpenArray(array)

    if ds is not None and prototype_ds is not None:
        if type(prototype_ds).__name__ == 'str':
            prototype_ds = gdal.Open( prototype_ds )
        if prototype_ds is not None:
            gdalnumeric.CopyDatasetInfo( prototype_ds, ds, xoff=xoff, yoff=yoff )
    return ds


def write_img(filename,im_proj,im_geotrans,im_data):
    if 'int8' in im_data.dtype.name:
        datatype = gdal.GDT_Byte
    elif 'int16' in im_data.dtype.name:
        datatype = gdal.GDT_UInt16
    else:
        datatype = gdal.GDT_Float32

    if len(im_data.shape) == 3:
        im_bands, im_height, im_width = im_data.shape
    else:
        im_bands, (im_height, im_width) = 1,im_data.shape

    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(filename, im_width, im_height, im_bands, datatype)

    dataset.SetGeoTransform(im_geotrans)
    dataset.SetProjection(im_proj)
    if im_bands == 1:
        dataset.GetRasterBand(1).WriteArray(im_data)
    else:
        for i in range(im_bands):
            dataset.GetRasterBand(i+1).WriteArray(im_data[i])

    del dataset

def shpClipRaster(raster_path, save_path,shapefile_path):
    # Load the source data as a gdalnumeric array
    # srcArray = gdalnumeric.LoadFile(raster_path)

    # Also load as a gdal image to get geotransform
    # (world file) info
    srcImage = gdal.Open(raster_path)
    geoTrans = srcImage.GetGeoTransform()
    geoProj = srcImage.GetProjection()

    # Create an OGR layer from a boundary shapefile
    shapef = ogr.Open(shapefile_path)
    lyr = shapef.GetLayer( os.path.split( os.path.splitext( shapefile_path )[0] )[1] )
    poly = lyr.GetNextFeature()

    # Convert the layer extent to image pixel coordinates
    minX, maxX, minY, maxY = lyr.GetExtent()
    ulX, ulY = world2Pixel(geoTrans, minX, maxY)
    lrX, lrY = world2Pixel(geoTrans, maxX, minY)

    # Calculate the pixel size of the new image
    pxWidth = int(lrX - ulX)
    pxHeight = int(lrY - ulY)

    # clip = srcArray[:, ulY:lrY, ulX:lrX]
    clip = srcImage.ReadAsArray(ulX,ulY,pxWidth,pxHeight)   #***只读要的那块***

    #
    # EDIT: create pixel offset to pass to new image Projection info
    #
    xoffset =  ulX
    yoffset =  ulY
    print ("Xoffset, Yoffset = ( %f, %f )" % ( xoffset, yoffset ))

    # Create a new geomatrix for the image
    geoTrans = list(geoTrans)
    geoTrans[0] = minX
    geoTrans[3] = maxY

    write_img(save_path, geoProj, geoTrans, clip)
    gdal.ErrorReset()

    return clip

if __name__ == "__main__":
    shp = "test.shp"
    img = "2020_clip.tif"
    out = "2020_clip_clip.tif"

    shpClipRaster(img, out, shp)
