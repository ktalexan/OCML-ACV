
# Importing the required libraries into the project
import os
from tqdm import tqdm

# Import local ACV class module
from acvml import acvml



# Get the paths to the project structure
basepath = os.environ['OneDriveConsumer']
pathprj = os.path.join(basepath, r'Professional\Projects\OCPW\2019_OCPW-ML\ML-Vision-Photospheres')
pathagp = os.path.join(basepath, r'Professional\GIS Data\OCGIS\OCML360ACV')
os.chdir(pathprj)



def azconfig(container):
    """Function that returns an acv class object instantiation
    The function uses the Azure blob storage and Azure Cognitive Vision account configuration
    along with the name of the storage container, and the metadata excel file to run a new
    class instantiation for the acv class.
    
    Arguments
        container: the name of the container in the blob storage
        
    Output
        response: the acv class instantiation object
    """
    
    # Setup account and key for the Azure blob storage, containing the photosphere images
    blobAccount = 'ocmlblobstorage'
    blobKey = '+jLL7LYXJrYREhBTsZ17Qj++3b+9RhoMYJ+IQMPGnH7OeyZ1PArC3+uUyyzXEC/ymxXy3bNplIO/kGWIJ9FeZg=='

    # Setup region and key for the Azure vision client API:
    apiRegion = 'westus2'
    apiKey = 'c3aeeac1c63d4a56a5f027ac9c268f7e'
    
    # Create a path variable of the photosphere metadata excel file (based on container name)
    metadata = os.path.join('PhotosphereMetadata', '{}.xlsx'.format(container))
    
    # Create a new acv class instantiation object
    response = acvml(blobAccount, blobKey, apiRegion, apiKey, container, metadata)
    
    return response




#---------- 4. Operations on Container 4 (ntustin2019088p2) ----------#

pid = 4
container = 'ntustin2019088p2'
cardinal = '{}-cardinal'.format(container)
fcout = 'fcjson_{}'.format(container)

# 1. Initialize: initialize the class and update metadata for container
print('\n{}.1. Initializing container {}'.format(pid, container))
az = azconfig(container)

# 2. Check Metadata: check the metadata file against the blobs in the container
print('\n{}.2. Checking metadata'.format(pid))
az.CheckBlobMetadata()

# 3. Update Image Metadata: update the metadata in photospheres for container
print('\n{}.3. Updating image metadata'.format(pid))
az.UpdateBlobMetadata()

# 4. Create Cardinal Container: create a cardinal blob container, and obtain the blob list of the photospheres for container
print('\n{}.4. Creating cardinal container'.format(pid))
az.CheckBlobContainer(cardinal)
blobs = az.GetBlobList()

# 5. Process Cardinal Blobs: create and process all cardinal images for blob container
print('\n{}.5. Processing cardinal blobs'.format(pid))
for blob in tqdm(blobs[8000:], desc='Processing Blob', unit='blob'):
    az.ProcessCardinalImages(blob)

# 6. Create geoJSON Features: create and process a geoJSON feature collection from cardinal images in blob container
print('\n{}.6. Creating geoJSON features'.format(pid))
fcjson = az.GeoJSONFromCardinals()

# 7. Write geoJSON to Disk: write and save the geoJSON cardinal feature collection to disk
print('\n{}.7. Writing geoJSON to disk'.format(pid))
az.WriteJSONFile(fcout, fcjson)

#print(json.dumps(fcjson12['features'][800], indent=4))

