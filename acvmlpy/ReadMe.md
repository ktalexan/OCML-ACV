<style type='text/css'>
h1 {color: brown; font-weight: bold;}
h2 {
	color: DarkBlue;
	background-color: LightSkyBlue;
	padding: 10px;
	font-weight: bold;
}
h2.toc {color: brown; background-color: transparent;}
h2.function {color: darkgreen; background-color:limegreen; padding:10px;}
h3 {color: green;}
ol li {list-style-type: decimal; color: gray;}
ftype {display:block; padding-left:2em;}
ftype:before {content: 'Type: '; color: green; font-weight:bold;}
fdesc {display:block; padding-left:2em;}
fdesc:before {content: 'Description: '; color:green; font-weight:bold;}
farg {display:block; padding-left:2em;}
farg:before {content: 'Arguments: '; color:green; font-weight: bold;}
fvar {display:block; padding-left:6em; text-indent:-4em}
fvar.head{display: inline-block; color:purple; font-style:italic;}
fret {display:block; padding-left:2em;}
fret:before {content: 'Returns: '; color:green; font-weight: bold;}
fnote {display:block; padding-left:2em;}
fnote:before {content: 'Notes: '; color: green; font-weight:bold}
fpy {color: green; font-style: italic;}
fpy:before {content: '(';}
fpy:after {content: ')';}
div {display: block;}
div.ClassName {color: darkblue; background-color:lightblue; padding: 10px; font-size: xx-large; font-weight:bold; border-bottom: 2px solid darkblue;}
div.ClassName arg {font-weight:normal;}
div.ClassName:before {content: 'Class: ';}
div.ClassBody {background-color: #EBF3FE; padding: 10px 20px;}
div.FunctionName {position: relative; width: 90%; left: 5%; color: darkgreen; background-color: transparent; padding:10px; font-size:x-large; font-weight:bold; border-bottom: 2px solid darkgreen;}
div.FunctionName arg {font-weight:normal;}
div.FunctionBody {position: relative; width: 90%; left: 5%; background-color: #DDFEBB; padding: 20px 25px;}
</style>


# Visual Studio ACV Project Python Class Documentation

<br>

<h2 class='toc'>Table of Contents</h2>

* [**Class: acvml**](#acvml)
    1. [**Class Initialization**](#initml)
    2. [**CheckDegrees**](#checkdegrees)
    3. [**CheckCardinality**](#checkcardinality)
    4. [**GetDirection**](#getdirection)
    5. [**ConvertStatePlane**](#convertstateplane)
    6. [**TimestampConvert**](#timestampconvert)
    7. [**CheckBlobContainer**](#checkblobcontainer)
    8. [**CheckBlobMetadata**](#checkblobmetadata)
    9. [**GetBlobList**](#getbloblist)
    10. [**GetObjectBounds**](#getobjectbounds)
    11. [**DrawBoundingBoxes**](#drawboundingboxes)
    12. [**WriteJSONFile**](#writejsonfile)
    13. [**UpdateBlobMetadata**](#updateblobmetadata)
    14. [**ProcessCardinalImages**](#processcardinalimages)
    15. [**GeoJSONFromCardinals**](#geojsonfromcardinals)
 * [**Class: acvgis**](#acvgis)
    1. [**CreateDomains**](#createdomains)
    2. [**CreateDatasets**](#createdatasets) 
    3. [**AddGeoJSON**](#addgeojson)
    4. [**ProcessFeature**](#processfeature)
    5. [**PopulateObjectList**](#populateobjectlist)
    6. [**CreateCardinalFeatures**](#createcardinalfeatures)
    5. [**MergeAreas**](#mergeareas)
    8. [**ProcessDetections**](#processdetections)
    9. [**CreatePointClusters**](#createpointclusters)
    10. [**GenerateClusterUUID**](#generateclusteruuid)
    11. [**GenerateObjectDirections**](#generateobjectdirections)
    12. [**DetectObjectCoordinates**](#detectobjectcoordinates)
    13. [**CreateObjectFeatureClass**](#createobjectfeatureclass)
<br><br>

<div style="page-break-after: always;"></div>

<div id='acvml' class='ClassName'>acvml<arg>(object)</arg></div>
<div class='ClassBody'>
<ftype>Python Class</ftype>
<fdesc>This class contains a number of functions, methods, and processes for ML object classification analysis using the Azure Cognitive Services Computer Vision API.</fdesc>
<farg></farg>
	<fvar><fvar class='head'>blobAccount:</fvar> the name of the Azure blob storage account.</fvar>
	<fvar><fvar class='head'>blobAccount:</fvar> the name of the Azure blob storage account.</fvar>
	<fvar><fvar class='head'>blobKey:</fvar> the API key of the Azure blob storage account.</fvar>
	<fvar><fvar class='head'>apiKey:</fvar> the Azure Cognitive Services Computer Vision API key (from Azure portal).</fvar>
   <fvar><fvar class='head'>containerName:</fvar> the base container name of the Azure blob storage account containing the photosphere images.</fvar>
	<fvar><fvar class='head'>metadata:</fvar> the name of the metadata (csv) file containing the Trimble GPS centimeter coordinates.</fvar>

```Python
Example class initialization:
   az = acvml(blobAccount, blobKey, apiRegion, apiKey, containerName, metadata)
```

</div><br>


<div id='initml' class='FunctionName'>__init__<arg>(self, blobAccount, blobKey, apiRegion, apiKey, containerName, metadata)</arg></div>
<div class='FunctionBody'>
	<ftype>Function class initialization</ftype>
	<fdesc>Returns an Azure Cognitive Services Computer Vision object (REST API) using a region and key.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>blobAccount:</fvar> the name of the Azure blob storage account (string).</fvar>
		<fvar><fvar class='head'>blobKey:</fvar> the API key of the Azure blob storage account (string).</fvar>
		<fvar><fvar class='head'>apiRegion:</fvar> the region of the Azure Cognitive Services Computer Vision API (e.g., 'westus') (string).</fvar>
		<fvar><fvar class='head'>apiKey:</fvar> the Azure Cognitive Services Computer Vision API key (from azure portal) (string).</fvar>
		<fvar><fvar class='head'>containerName:</fvar> the base container name of the Azure blob storage account containing the area's photosphere images (string).</fvar>
		<fvar><fvar class='head'>metadata:</fvar> the name of the metadata (csv) file containing the gps attributes from the Trimble sensor (path/filename/string).</fvar>
	<fret></fret>
		<fvar><fvar class='head'>client:</fvar> a Computer Vision API object <fpy>class object</fpy>.</fvar>
	<fnote>This function runs on instantiation of the class.</fnote>
</div><br>

<div style="page-break-after: always;"></div>

<div id='checkdegrees' class='FunctionName'>CheckDegrees<arg>(x, y)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc> Checks and obtains degrees based on addition. This function cycles degrees from 0&deg; to 360&deg; based on mathematical addition. Given an initial starting degree (x), we calculate the sum between x and y. If x + y exceeds 360&deg;, the function resets the value to accomodate radial consistency.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>x:</fvar> initial (starting) degrees <fpy>float</fpy></fvar>
		<fvar><fvar class='head'>y:</fvar> degrees to be added <fpy>float</fpy></fvar>
	<fret></fret>
	<fvar><fvar class='head'>sumdeg:</fvar> the sum of degrees between 0 and 360&deg; <fpy>float</fpy></fvar>
</div><br>


<div id='checkcardinality' class='FunctionName'>CheckCardinality<arg>(value)</arg></div>
<div class = 'FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Returns a cardinal direction from a dictionary. This function checks a direction values (in degrees) against a cardinal direction dictionary. It returns a cardinal direction class in which the direction value belongs to.</fdesc>
	<farg></farg>
	<fvar><fvar class='head'>value:</fvar> the direction value in degrees <fpy>float</fpy></fvar>
	<fret></fret>
	<fvar><fvar class='head'>cardinalDir:</fvar> the cardinal direction class label <fpy>string</fpy></fvar>
</div><br>


<div id='getdirection' class='FunctionName'>GetDirection<arg>(x, y)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Calculates direction from State Plane coordinates. This function calculates the direction (angle in degrees from true north) from Easting and Northing coordinates expressed in State Plane, California Zone 6 (NAD84) coordinate system</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>x:</fvar> Easting coordinate value in NAD84 <fpy>float</fpy></fvar>
		<fvar><fvar class='head'>y:</fvar> Northing coordinate value in NAD84 <fpy>float</fpy></fvar>
	<fret></fret>
		<fvar><fvar class='head'>degout:</fvar> direction in degrees (always positive, reverses if negative) <fpy>float</fpy></fvar>
</div><br>

<div style="page-break-after: always;"></div>

<div id='convertstateplane' class='FunctionName'>ConvertStatePlane<arg>(xin, yin, zin)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Converts State Plane coordinates (NAD84) to Lat/Lon degrees (WGS84). This function converts coordinates from State Plane coordinate system CA zone 6 (NAD84, espg:2230) to default ESRI and ArcGIS online Lat/Lon degrees (WGS84, espg:4326).</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>xin, yin, zin:</fvar> Easting, Northing and Elevation coordinates respectively in NAD84 <fpy>float</fpy></fvar>
	<fret></fret>
		<fvar><fvar class='head'>xout, yout, zout:</fvar> Longitude, Latitude, and Elevation coordinates respectively in WGS84 <fpy>float</fpy></fvar>
</div><br>


<div id='timestampconvert' class='FunctionName'>TimestampConvert<arg>(imgname, timestamp)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Converts image timestamp string to native datetime format. This function takes as an input the string timestamp epich from metatada (Trimble GPS sensor) and converts them to a native (local) datetime format. This function provides functionality required for ArcGIS geodatabase field type (ArcGIS datetime format).</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>imgname:</fvar> the name of the image to be converted <fpy>string</fpy></fvar>
		<fvar><fvar class='head'>timestamp:</fvar> the string timestamp input to be converted <fpy>string</fpy></fvar>
	<fret></fret>
		<fvar><fvar class='head'>dtobjpst:</fvar> a datetime object <fpy>datetime</fpy></fvar>
</div><br>


<div id='checkblobcontainer' class='FunctionName'>CheckBlobContainer<arg>(containerName=None, create=True, publicAccess='blob')</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Checks for the presence of a blob container in the Azure account. This function checks if a container (folder) exists or not. If it exists, the publicAccess setting is set to the value of the function. If it does not exist and create=True (default), then the folder is created and publicAccess is set. If it does not exist and create=False, nothing is done.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>containerName:</fvar> the name of the blob container (folder) to be checked (optional, otherwise it checks the main) <fpy>string</fpy></fvar>
		<fvar><fvar class='head'>create (=True by default):</fvar> whether or not to create a new container <fpy>boolean</fpy></fvar>
		<fvar><fvar class='head'>publicAccess (='blob' by default):</fvar> level of public access to URL <fpy>'blob'/'container'</fpy></fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar> Returns nothing. Performs operations in Microsoft Azure Storage on the cloud.</fbar>
</div><br>

<div style="page-break-after: always;"></div>

<div id='checkblobmetadata' class='FunctionName'>CheckBlobMetadata<arg>()</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Checks the metadata of the blob container. This function checks and ensures that the original metadata in the excel file corresponds exactly to the photospheres contained in the blob container (mathcing them image-by-image).</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>None:</fvar> uses the default container defined in the class initialization.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar> Returns nothing. Just a statement containing how many photospheres are matched.</fvar>
</div><br>


<div id='getbloblist' class='FunctionName'>GetBlobList<arg>(containerName=None)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Lists all blobs in Azure storage blob. This function obtains a list of all files in an Azure storage blob (by container folder name).</fdesc>
	<farg></farg>
	   <fvar><fvar class='head'>containerName (optional):</fvar> if containerName=None, the function uses the default Azure storage blob container name (from the class initalization). Otherwise, if containerName is not None, the function uses the defined Azure storage blob container instead <fpy>string</fpy>.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>blobList:</fvar> a python list of all files in the Azure blob container <fpy>string list</fpy>.</fvar>
</div><br>


<div id='getobjectbounds' class='FunctionName'>GetObjectBounds<arg>(jsonstring)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Obtains detected object bounds from bounding box coordinates. This function returns bounding coordinates for a detected object from Azure Cognitive Vision JSON response string.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>jsonstring:</fvar> the JSON detection response from Azure Cognitive Vision containing the detected object <fpy>JSON string</fpy>.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>bounds:</fvar> the set of bounds expressed in bounding box coordinates (x, y, w, h) <fpy>integer list</fpy>.</fvar>
</div><br>

<div style="page-break-after: always;"></div>

<div id='drawboundingboxes' class='FunctionName'>DrawBoundingBoxes<arg>(image, bounds)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Draws annotation boxes in image. This function uses the bound coordinates to draw annotation boxes around photosphere images.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>image:</fvar> the photosphere image (cardinal) to be annotated (string).<br>
		_bounds_: the bounding box coordinates of the detected object(s) <fpy>integer list</fpy>.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>image:</fvar> the annotated image <fpy>image object</fpy>.</fvar>
</div><br>


<div id='writejsonfile' class='FunctionName'>WriteJSONFile<arg>(name, data)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Writes detection output into a JSON file structure. This function outputs (writes to disk) the processed results of the Azure Cognitive Vision detection process into a JSON file.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>name:</fvar> the name of the JSON to be saved as a .json file (string). <br>
		_data_: the JSON string response data to be included <fpy>JSON string object</fpy>.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar> Returns nothing. The JSON file is saved using the name provided.</fvar>
</div><br>


<div id='updateblobmetadata' class='FunctionName'>UpdateBlobMetadata<arg>()</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Uploads and updates blob metadata from excel file metadata file. This function will upload and update the blob metadata, based on the metadata file stored in the image.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>None:</fvar> Uses the metadata file defined in the class initialization function.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar> Returns nothing. Performs the operation in the blob container.</fvar>
</div><br>

<div style="page-break-after: always;"></div>

<div id='processcardinalimages' class='FunctionName'>ProcessCardinalImages<arg>(blob)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Processes cardinal images from the original photospheres. This function obtains 8 cardinal images (1000 x 1000 pixels) from the original photospheres, by cropping a region between 1550 and 2550 pixels of the original image, i.e., from (x1=0, y1=1550) to (x2=8000, y2=2550) vertically. The function returns a list with 8 cardinal images from left to right, each image covering a 45&deg; vision span.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>blob:</fvar> the blob object (photosphere image) to be processed <fpy>string</fpy>.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar> Returns nothing. The results are processed and saved in the cardinal output container of the storage blob.</fvar>
</div><br>


<div id='geojsonfromcardinals' class='FunctionName'>GeoJSONFromCardinals<arg>()</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Generates a GeoJSON string object from cardinal photosphere image analysis. This function follows the *ProcessCardinalImages* class function after the cardinal images are generated, their object detection process from Azure Cognitive Services Computer Vision is completed, and the cardinal images have been annotated and taged.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>None:</fvar> The function uses the Azure blob storage container from the class initialization function.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>fcresponse:</fvar> A geoJSON feature collection containing all features and geopoings with all the analysis results of the AI detection <fpy>geoJSON string object</fpy>.</fvar>
</div><br><br>



<div style="page-break-after: always;"></div>


<div id='acvgis' class='ClassName'>acvgis<arg>(object)</arg></div>
<div class='ClassBody'>
	<ftype>Python Class</ftype>
	<fdesc>This class performs: (a) basic functions in the ArcGIS Pro project, including setting up domains and datasets; (b) functions, methods and processes for post-processing ML object classification analysis using ArcGIS Pro (arcpy) and ArcGIS Python API (arcgis) operations.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>fclist:</fvar> the namesof each of the sub-datasets in an area to be processed (names of feature classes).</fvar>
		<fvar><fvar class='head'>area:</fvar> the name of the area to be processed (e.g., 'North Tustin')</fvar>
		<fvar><fvar class='head'>prjdata:</fvar> the folder path containing the project data and the geoJSON files (e.g., ACVMLPhotospheres)</fvar>
	   <fvar><fvar class='head'>prjagp:</fvar> the folder path containing the ArcGIS Pro project structure (e.g., ACVML).</fvar>
	   <fvar><fvar class='head'>agpname:</fvar> the name of the ArcGIS Pro project.</fvar>
	   <fvar><fvar class='head'>projection:</fvar> the projection file location (WGS84) to be used.</fvar>

```Python
Example class initialization:
	ast = acvgis(prjagp, agpname, projection)
```

</div><br>


<div id='initgis' class='FunctionName'>__init__<arg>(self, fclist, area, prjdata, prjagp, agpname, projection)</arg></div>
<div class='FunctionBody'>
	<ftype>Function class initialization</ftype>
	<fdesc>Returns a set of global class variables for processing.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>fclist:</fvar> the namesof each of the sub-datasets in an area to be processed (names of feature classes).</fvar>
		<fvar><fvar class='head'>area:</fvar> the name of the area to be processed (e.g., 'North Tustin')</fvar>
		<fvar><fvar class='head'>prjdata:</fvar> the folder path containing the project data and the geoJSON files (e.g., ACVMLPhotospheres)</fvar>
	   <fvar><fvar class='head'>prjagp:</fvar> the folder path containing the ArcGIS Pro project structure (e.g., ACVML).</fvar>
	   <fvar><fvar class='head'>agpname:</fvar> the name of the ArcGIS Pro project.</fvar>
	   <fvar><fvar class='head'>projection:</fvar> the projection file location (WGS84) to be used.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>client:</fvar> a class object <fpy>class object</fpy>.</fvar>
	<fnote>This function runs on instantiation of the class.</fnote>
</div><br>

<div style="page-break-after: always;"></div>

<div id='createdomains' class='FunctionName'>CreateDomains<arg>()</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Creates domains in geodatabase. This function creates baseline coded value domains in the project's geodatabase.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>None:</fvar> uses the project and geodatabase settings from the class initialization.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar> returns nothing. Performs geodatabase operations.</fvar>
</div><br>


<div id='createdatasets' class='FunctionName'>CreateDatasets<arg>()</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Creates feature datasets in geodatabase. This function creates the necessary feature datasets in the project's geodatabase to be populated with the analysis data.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>None:</fvar> uses the project and geodatabase settings from the class initialization.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar> returns nothing. Performs geodatabase operations.</fvar>
</div><br>


<div id='addgeojson' class='FunctionName'>AddGeoJSON<arg>()</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Creates a feature class from geoJSON string. This function adds the geoJSON data to the project's geodatabase and creates a feature class in the Photospheres feature dataset.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>None:</fvar>uses the saved geoJSON file and the project's geodatabase structure.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar>returns nothing. Performs geodatabase operations.</fvar>
</div><br>

<div style="page-break-after: always;"></div>

<div id='processfeature' class='FunctionName'>ProcessFeature<arg>()</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Process new feature attributes. This function performs basic geoprocessing operations to the newly added feature class (from the *AddGeoJSON* function), i.e., adding alias names, adding extra fields, and assign coded domain values to fields.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>None:</fvar>uses the selected geodatabase feature class and performs geoprocessing operations.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar>returns nothing. Performs geodatabase operations on feature class.</fvar>
</div><br>


<div id='populateobjectlist' class='FunctionName'>PopulateObjectList<arg>()</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Populates rows on selected feature class fields. This function calculates and populates all rows on certain fields based on SQL queries (using *UpdateCursor* arcpy method).</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>None:</fvar>uses the selected feature class in the project's geodatabase.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar>returns nothing. Performs geodatabase operations on feature class.</fvar>
</div><br>


<div id='createcardinalfeatures' class='FunctionName'>CreateCardinalFeatures<arg>()</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Creates a new feature class for first cardinal directions. This function creates a new feature class for cardinal direction 1 from photosphere feature class (in the Cardinal feature dataset of the geodatabase).</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>None:</fvar>uses the selected feature class in the projects' geodatabase.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar>returns nothing. Performs geodatabase operations on feature class.</fvar>
</div><br>

<div style="page-break-after: always;"></div>

<div id='mergeareas' class='FunctionName'>MergeAreas<arg>()</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Merging feature classes in area list. This function uses all the photosphere and cardinal area groups of feature classes to generate merged feature classes (one per area).</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>None:</fvar> uses area feature classes in project's geodatabase.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar> returns nothing. Performs geoprocessing operations in the project's default geodatabase.</fvar>
</div><br>


<div id='processdetections' class='FunctionName'>ProcessDetections<arg>()</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Creates new feature classes for object detections. This function create new feature classes containing ony detections (for stop signs and fire hydrants).</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>None:</fvar> uses the merged area feature classes in the project geodatabase.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar>  returns nothing. Performs geodatabase operations in the project's default geodatabase.</fvar>
</div><br>


<div id='createpointclusters' class='FunctionName'>CreatePointClusters<arg>(fcdataset, fcname)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Finds point clusters in feature class. This function creates (finds) point clusters using the 'FindPointClusters' arcpy function in the merged areas feature classes of the geodatabase.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>fcdataset:</fvar> the name of the geodatabase feature dataset where the feature class is located (e.g., StopSigns) <fpy>String</fpy>.</fvar>
		<fvar><fvar class='head'>fcname:</fvar> the name of the feature class to be procesed <fpy>String</fpy>.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>fpc:</fvar> returns the name of the newly created point cluster feature class <fpy>String</fpy>.</fvar>
</div><br>

<div style="page-break-after: always;"></div>

<div id='generateclusteruuid' class='FunctionName'>GenerateClusterUUID<arg>(fpc)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Creates unique cluster UUIDs for a point cluster feature class. This function returns a list of unique clusters (with UUID) in a point cluster feature class.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>fpc:</fvar> the name of the point cluster feature class to be processed<fpy>String</fpy>.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar> returns nothing. Performs geodatabase operations to the attribute table of the geodatabase's feature class.</fvar>
</div><br>


<div id='generateobjectdirections' class='FunctionName'>GenerateObjectDirections<arg>(fpc)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Generates and populate directions for detected objects. This function adds new fields for detected objects and populates the object direction field.</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>fpc:</fvar> the name of the point cluster feature class to be processed<fpy>String</fpy>.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar>returns nothing. Performs geodatabase operations in the selected point cluster feature class of the geodatabase.</fvar>
</div><br>


<div id='detectobjectcoordinates' class='FunctionName'>DetectObjectCoordinates<arg>(fpc)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc>Detects and computes object coordinates from cluster pairs. This function calculates object coordinates from clusters combinatorial pairs and their statistics (mean and standard deviations).</fdesc>
	<farg></farg>
		<fvar><fvar class='head'>fpc:</fvar> the name of the point cluster feature class to be processed <fpy>String</fpy>.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>response:</fvar> returns the table of the detected objects and their attributes in the feature class <fpy>Dictionary List</fpy>.</fvar>
</div><br>

<div style="page-break-after: always;"></div>

<div id='createobjectfeatureclass' class='FunctionName'>CreateObjectFeatureClass<arg>(fpc, data)</arg></div>
<div class='FunctionBody'>
	<ftype>Python class function</ftype>
	<fdesc></fdesc>
	<farg></farg>
		<fvar><fvar class='head'>fpc:</fvar> the name of the point cluster feature class to be processed <fpy>String</fpy>.</fvar>
		<fvar><fvar class='head'>data:</fvar> the response data from the <i>DetectObjectCoordinates()</i> function <fpy>Dictionary List</fpy>.</fvar>
	<fret></fret>
		<fvar><fvar class='head'>Null:</fvar> returns nothing. Generates new feature class with the detected object locations in the project's geodatabase.</fvar>
</div><br>

