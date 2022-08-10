# OCML Development Notes

## Python Development Documentation

### Notes 08-08-2022

* The python library _geojson_ does not work properly. It does not load even when it is installed via conda or pip.
* There is an update similar package called _geopandas_ (see [here](https://anaconda.org/conda-forge/geopandas) for the package, and also [read the guide](https://geopandas.org/en/stable/docs/user_guide/io.html)).

### Notes 10-08-2022

* Had to import the _piexif_ library from conda.
* New **azure-storage-blob** python library (v12 SDK):
  * [Documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=environment-variable-windows)
  * Storing and using credentials:
    a. Copy Connection String from Azure portal (under Key1)
    b. Using command line (windows), store the connection string as an environmental variable, after which restart programs.

  ```python
    setx AZURE_STORAGE_CONNECTION_STRING "<your connection string>"
  ```

  * Initiate the libraries:

  ```python
    import os, uuid
    from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
  ```

  * Obtain the connection string:

  ```python
    # Obtain the connection string
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
  ```

  * Get the blob service client:

  ```python
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
  ```

  * Get the list of the parent (root) containers:

  ```python
    L1containers = blob_service_client.list_containers(include_metadata=True)
    for container in L1containers:
      print(container['name'], container['metadata'])
