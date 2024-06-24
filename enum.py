from azure.identity import DefaultAzureCredential
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.mgmt.resource import ResourceManagementClient
import os

# Authenticate using managed identity
credential = DefaultAzureCredential()

# Replace with your subscription ID
subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')

if not subscription_id:
    raise ValueError("Please set the AZURE_SUBSCRIPTION_ID environment variable.")

# Initialize Resource Management Client
resource_client = ResourceManagementClient(credential, subscription_id)

# Initialize KeyVault Management Client
keyvault_client = KeyVaultManagementClient(credential, subscription_id)

# Replace with your resource group name
resource_group_name = 'your-resource-group-name'

# Function to list all Key Vaults in a resource group
def list_keyvaults_in_resource_group(resource_group_name):
    keyvaults = keyvault_client.vaults.list_by_resource_group(resource_group_name)
    keyvault_names = [kv.name for kv in keyvaults]
    return keyvault_names

if __name__ == "__main__":
    # Get and print Key Vault names in the specified resource group
    keyvault_names = list_keyvaults_in_resource_group(resource_group_name)
    print(f"Key Vaults in resource group '{resource_group_name}':")
    for name in keyvault_names:
        print(name)
