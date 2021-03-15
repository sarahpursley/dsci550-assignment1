#!/usr/bin/env python

import requests
import base64
import ee

class geengine():
    def __init__(self):
        # Authenticate Earth Engine API
        ee.Authenticate()
        # Initialize Earth Engine API
        ee.Initialize()
        self.ee = ee
        # Define available GEE collections
        self.collections = {
            'population_density': {
                'name': 'CIESIN/GPWv411/GPW_Population_Density',
                'startdate': '2000-01-01T00:00:00',
                'enddate': '2020-01-01T00:00:00',
                'url': 'https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Population_Density',
                'description': 'The Gridded Population of World Version 4 (GPWv4), Revision 11 models the distribution of global human population for the years 2000, 2005, 2010, 2015, and 2020 on 30 arc-second (approximately 1km) grid cells. Population is distributed to cells using proportional allocation of population from census and administrative units. Population input data are collected at the most detailed spatial resolution available from the results of the 2010 round of censuses, which occurred between 2005 and 2014. The input data are extrapolated to produce population estimates for each modeled year. These population density grids contain estimates of the number of persons per square kilometer consistent with national censuses and population registers. There is one image for each modeled year.'
            },
            'population_count': {
                'name': 'CIESIN/GPWv411/GPW_Population_Count',
                'startdate': '2000-01-01T00:00:00',
                'enddate': '2020-01-01T00:00:00',
                'url': 'https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Population_Count',
                'description': 'The Gridded Population of World Version 4 (GPWv4), Revision 11 models the distribution of global human population for the years 2000, 2005, 2010, 2015, and 2020 on 30 arc-second (approximately 1km) grid cells. Population is distributed to cells using proportional allocation of population from census and administrative units. Population input data are collected at the most detailed spatial resolution available from the results of the 2010 round of censuses, which occurred between 2005 and 2014. The input data are extrapolated to produce population estimates for each modeled year. These population count grids contain estimates of the number of persons per 30 arc-second grid cell consistent with national censuses and population registers. There is one image for each modeled year.'
            },
            'raw_land': {
                'name': 'LANDSAT/LE07/C01/T1',
                'startdate': '1999-01-01T00:00:00',
                'enddate': '2021-02-13T00:00:00',
                'url': 'https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T1',
                'description': 'Landsat 7 Collection 1 Tier 1 DN values, representing scaled, calibrated at-sensor radiance. Landsat scenes with the highest available data quality are placed into Tier 1 and are considered suitable for time-series processing analysis. Tier 1 includes Level-1 Precision Terrain (L1TP) processed data that have well-characterized radiometry and are inter-calibrated across the different Landsat sensors. The georegistration of Tier 1 scenes will be consistent and within prescribed tolerances [<=12 m root mean square error (RMSE)]. All Tier 1 Landsat data can be considered consistent and inter-calibrated (regardless of sensor) across the full collection. See more information in the USGS docs.'
            },
            'country_boundaries': {
                'name': 'CIESIN/GPWv411/GPW_National_Identifier_Grid',
                'startdate': '2000-01-01T00:00:00',
                'enddate': '2020-01-01T00:00:00',
                'url': 'https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_National_Identifier_Grid',
                'description': 'The Gridded Population of World Version 4 (GPWv4), Revision 11 models the distribution of global human population for the years 2000, 2005, 2010, 2015, and 2020 on 30 arc-second (approximately 1km) grid cells. Population is distributed to cells using proportional allocation of population from census and administrative units. Population input data are collected at the most detailed spatial resolution available from the results of the 2010 round of censuses, which occurred between 2005 and 2014. The input data are extrapolated to produce population estimates for each modeled year. The National Identifier Grid Represents the Census Data Source Used to Produce the GPWv4 Populations estimates. Pixels that have the same value reflect the same data source, most often a country or territory.'
            }
        }

    def _rect_from_point(self, x, y, buffer=10):
        if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float) and type(buffer) == int:
            return [[x-buffer, y+buffer], [x+buffer, y-buffer]]
        else:
            raise TypeError('Point coordinates must be int or float, buffer must be int')

    def _download_from_url(self, url):
        # Request url
        r = requests.get(url, timeout=3000)
        # Raise an exception depending upon the status code
        r.raise_for_status()
        # If good status, return the response content
        return r.content

    def image_to_b64(self, imgbytes):
        return base64.b64encode(imgbytes)

    def b64_to_image(self, b64string):
        return base64.b64decode(b64string)

    def get_population_density_img(self, long, lat, startdate='2000-01-01', enddate='2020-01-01'):
        # Set point
        point = ee.Geometry.Point([long, lat])
        # Build area rectangle around point
        region = ee.Geometry.Rectangle(coords=self._rect_from_point(long, lat))
        # Get collection and filter by date
        #   TODO: Add date validation
        col = ee.ImageCollection('CIESIN/GPWv411/GPW_Population_Density').filterDate(startdate, enddate)
        # Get image
        image = col.mosaic()
        path = image.getThumbUrl({
            'min': 0,
            'max': 2000,
            'palette': [
                'ffffe7',
                'FFc869',
                'ffac1d',
                'e17735',
                'f2552c',
                '9f0c21'
            ],
            'region': region,
            'dimensions': 500,
            'format': 'png'
        })
        # Download image from url
        return self._download_from_url(path)

    def get_population_count_img(self, long, lat, startdate='2000-01-01', enddate='2020-01-01'):
        # Set point
        point = ee.Geometry.Point([long, lat])
        # Build area rectangle around point
        region = ee.Geometry.Rectangle(coords=self._rect_from_point(long, lat))
        # Get collection and filter by date
        #   TODO: Add date validation
        col = ee.ImageCollection('CIESIN/GPWv411/GPW_Population_Count').filterDate(startdate, enddate)
        # Get image
        image = col.mosaic()
        path = image.getThumbUrl({
            'min': 0,
            'max': 2000,
            'palette': [
                'ffffe7',
                '86a192',
                '509791',
                '307296',
                '2c4484',
                '000066'
            ],
            'region': region,
            'dimensions': 500,
            'format': 'png'
        })
        # Download image from url
        return self._download_from_url(path)

    def get_raw_land_img(self, long, lat, startdate='1999-01-01', enddate='2021-01-01'):
        # Set point
        point = ee.Geometry.Point([long, lat])
        # Build area rectangle around point
        region = ee.Geometry.Rectangle(coords=self._rect_from_point(long, lat))
        # Get collection and filter by date
        #   TODO: Add date validation
        col = ee.ImageCollection('LANDSAT/LE07/C01/T1').filterDate(startdate, enddate)
        # Get image
        image = col.mosaic()
        path = image.getThumbUrl({
            'bands': ['B1', 'B2', 'B3'],
            'gain': [1.4, 1.4, 1.1],
            'region': region,
            'dimensions': 500,
            'format': 'png'
        })
        # Download image from url
        return self._download_from_url(path)

    def get_country_boundaries_img(self, long, lat, startdate='2000-01-01', enddate='2000-01-01'):
        # Set point
        point = ee.Geometry.Point([long, lat])
        # Build area rectangle around point
        region = ee.Geometry.Rectangle(coords=self._rect_from_point(long, lat))
        # Get collection and filter by date
        #   TODO: Add date validation
        image = ee.Image('CIESIN/GPWv411/GPW_National_Identifier_Grid')
        # Get image
        path = image.getThumbUrl({
            'min': 4,
            'max': 1000,
            'palette': [
                '000000',
                'ffffff'
            ],
            'region': region,
            'dimensions': 500,
            'format': 'png'
        })
        # Download image from url
        return self._download_from_url(path)
