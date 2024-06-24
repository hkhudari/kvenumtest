import logging
from azure.identity import ManagedIdentityCredential
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.core.exceptions import HttpResponseError

# Configure logging
logging.basicConfig(level=logging.INFO)

# Replace these with your Azure subscription ID and resource group name
subscription_id = 'your-subscription-id'
resource_group_name = 'your-resource-group-name'

try:
    # Authenticate using managed identity
    logging.info("Authenticating with Azure using managed identity...")
    credential = ManagedIdentityCredential()

    # Create a KeyVaultManagementClient instance
    logging.info("Creating KeyVaultManagementClient instance...")
    keyvault_client = KeyVaultManagementClient(credential, subscription_id)

    # List all key vaults in the specified resource group
    logging.info(f"Listing Key Vaults in resource group: {resource_group_name}...")
    key_vaults = keyvault_client.vaults.list_by_resource_group(resource_group_name)

    # Print the details of each key vault
    vaults_found = False
    for kv in key_vaults:
        vaults_found = True
        logging.info(f"Key Vault Name: {kv.name}")
        logging.info(f"Location: {kv.location}")
        logging.info(f"Resource ID: {kv.id}")
        logging.info("------")

    if not vaults_found:
        logging.info(f"No Key Vaults found in the specified resource group '{resource_group_name}'.")

except HttpResponseError as e:
    logging.error(f"HTTP response error: {e.message}")
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
