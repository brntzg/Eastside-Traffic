# Eastside Traffic Count Analysis
## Abstract
This project is an exploratory spatial data analysis and mapping of annual average daily traffic (AADT) around the City of Redmond in Washington State from 2022 and 2024.<br><br>
The output files include a map of the study area's AADT, a kernel density estimation and network centrality analysis. A recommendation section is included to identify possible follow-up analysis to determine any hostpots and spatial outlier (i.e., Global/Local Moran's *I* and Getis-Ord Gi*). I also enumerated nearby points-of-interest () that would generate trafffic which might affect Redmond's own count observations. This should be considered in future spatial data analysis reports--as well as social impacts of high volumes of traffic generate noise, air and ground pollution and would negatively affect parks, recreational areas, bodies of water and residents.
## Methodology
In ArcGIS Pro, I loaded the City of Redmond 'Citylimit' and 'Centerline' vector files, which I had downloaded from its GIS Open Data webpage [**Endnote 1**]. They are saved in the 'SourceShapefiles' folder in this workspace's file directory.<br><br>
As the City does not have its Annual Average Daily Traffic counts already available in a table or another structured format, I had to use the Traffic Counts maps for 2022 and 2024 [**Endnote 2**]. I clipped a copy of each file and I saved one version for the downtown map inset and a second version for the citywide map as PNG files; then I loaded them as raster feature layers in ArcGIS Pro. Although the vector data that I had downloaded were already set to the approporiate projection ('NAD 1983 HARN StatePlane Washington North FIPS 4601'), the raster files had no assigned spatial reference system. Therefore, each raster was georeferenced using control points to align with the 'Citylimit' and 'Centerline' vector layers. ArcGIS Pro created a PGWX file for the transformation's 6 parameters; each PGWX file contains 6 floats that can be intepreted by a software program to correctly map the rasters. This is done later by using the pythonic library rasterio. Note that each PNG file is in the GeoreferencedRasters directory with the 'PGWX' and related 'PNG.OVR' and 'PNG.AUX.XML' files. <br><br>
The next step, although technically simple, required a lot of repetitive manual editing and data entry. In ArcGIS Pro, I added a point feature layer of the sites where the the traffic counts were recorded. Then in its attribute table, I entered the 2022 and 2024 AADT values that were recorded on the rasters.<br><br> 
Despite easily finding the vector data for Bellevue, King Count and the State's transportation department ('WSDOT'), I realized that I forgot to look up published traffic counts by the cities of Kirkland and Sammamish. Both of which are adjacent to Redmond; their roadways form a inter-municipal network. Although Issaquah, Newcastle, Mercer Island, Medina, Clyde Hill, Yarrow Point and Hunts Point are resoanbly nearby and a part of the Eastside, I decided not to look for their own data as they do not border Redmond. Moreover, WSDOT has traffic count sites along the major travel corridors--I90, I40, SR202 and SR520--that bisect these constituencies. Initially I had loaded Seattle's data as it is the largest city (by size and population) in King County, but a comparative study is not necessary for now. The scope of the study is specific to traffic flows in the City of Redmond. Therefore, Seattle's data were excluded. King County was also excluded from the analysis as I could only find data between 1996 and 2020. This is unfortunate as the area to the northeast of Redmond is unincorporated--therefore the juridcition is the County's. Thus the neighboring area cannot be compared like Kirkland, Bellevue and Sammamish can be to Redmond. However, as there are sites along most of the inter-municipal roadways near the northern and the eastern boundaries of the City, traffic flows between both jurisdictions were still measured.<br><br>
While the City of Sammamish's published data [**Endnote 3**] are formatted similarly to Redmond's (as a PDF of the points with the counts included as annotated labels), the City of Kirkland has a webmap of the sites [**Endnote 4**]. The records are viewable in a pop-up table and in a a tabular structure as a PDF. The method to transfer the data and their formatting was more complicated. I repeated the same georeferencing workflow that I outlined above for Sammamish's data. For Kirkland, it was similar with an additional step of cross-referencing the webmap's data and the PDF before transcribing the traffic count values into the attribute table. Note: the georeferenced rasters can be seen in the Raster ESD Mapping Jupyter Notebook.<br><br>
The vector data published by Bellevue and WSDOT each required a unique workflow.



Finally, to ensure the points were snapped to the roads, I ran the ArcGIS Pro 'Snap' geoprocessing tool to the nearest edge (i.e., centerline). Afterwhich, I added two fileds to the attribute table for the x- and y-coordinates, which are automatically updated after I used the ArcGIS Pro tool to calculate the point features gemoetries.



# Exploratory Spatial Data Analysis
As mentioned above, the georeferenced/affine-transformed raster data can be reviewed in the Jupyter Notebook 'raster_esd_mapping'.
# 
# Network Analysis
Although the 

# Recommendations
Further analysis can be done to determine spatial autocorrelation using Global Moran's *I*. Local Moran's *I* alongside Getis-Ord Gi* can be used to identify statistically significant hot spots and cold spots as well as spatial outliers (i.e., roadways with AADT obervations that are statistically higher than nearby raodways--and conversely low-high juxtapositions.) Once these spatial outliers are identified, additional mapping of the natural and built environment could reveal explanations--such as school zones, hospitals, parks, strip malls, airports, transit centers and parks business. For example--due to my knowledge of the area-- I would suspect that nearby Overlake Hospital, Bellevue Square, Crossroads and Factoria Mall, Marymoor Park, Sammamish State Park, the Microsoft Campus, Costco's headquarters and even the wineries in Woodinville generate traffic, which cause bottlenecks. The traffic data can also be inform any environmental matters as traffic-related pollutants near parks, ponds, streams and lakes would be negatively affected.


## Endnote References
**1**   [City of Redmond's GIS Open Data webpage](https://www.redmond.gov/424/Data-Downloads)
**2**   [City of Redmond's Traffic Counts webpage](https://www.redmond.gov/863/Traffic-Counts)
**3**   [City of Sammamish's Traffic Counts webpage](https://www.sammamish.us/government/public-works/traffic-engineering/citywide-traffic-counts/)
**4**   [City of Kirkland's Annual Average Daily webmap](https://experience.arcgis.com/experience/6107b9c27c1b43718e685a73307281c4)
**5**   [City of Kirkland's Traffic Count Summary PDF](https://www.kirklandwa.gov/files/sharedassets/public/v/3/public-works/aadt2024webpage02032025.pdf)




* 'WSDOT - Traffic Counts (AADT) Current' --> downloaded as GeoJSON
    URL: https://geo.wa.gov/datasets/WSDOT::wsdot-traffic-counts-aadt-current/about

* 'WSDOT - Historic Traffic Counts 2022' --> downloaded as GeoJSON
    https://geo.wa.gov/datasets/WSDOT::wsdot-historic-traffic-counts-2022/about


* King County

https://gis-kingcounty.opendata.arcgis.com/datasets/kingcounty::cities-and-unincorporated-king-county/about

City of Bellevue, WA Traffic Analysis Reports (TAR)
https://bellevuewa.gov/city-government/departments/transportation/safety-and-maintenance/traffic-safety/traffic-analysis-reports

