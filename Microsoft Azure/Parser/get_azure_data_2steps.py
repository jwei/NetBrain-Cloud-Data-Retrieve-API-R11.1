## Description

The get_azure_data_2steps function supports two steps (i.e., POST + GET) methods to get data tables of Azure resources. This function performs the following two steps to retrieve the data:

1. It sends a POST request which returns a table URL in the HTTP response location header.
2. It sends a subsequent GET request to get the table data from the returned URL.
