from azure.identity import ManagedIdentityCredential
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.core.exceptions import HttpResponseError

# Replace these with your Azure subscription ID and resource group name
subscription_id = ''
resource_group_name = ''

try:
    # Authenticate using managed identity
    credential = ManagedIdentityCredential()

    # Create a KeyVaultManagementClient instance
    keyvault_client = KeyVaultManagementClient(credential, subscription_id)

    # List all key vaults in the specified resource group
    key_vaults = keyvault_client.vaults.list_by_resource_group(resource_group_name)

    # Print the details of each key vault
    vaults_found = False
    for kv in key_vaults:
        vaults_found = True
        print(f"Key Vault Name: {kv.name}")
        print(f"Location: {kv.location}")
        print(f"Resource ID: {kv.id}")
        print("------")

    if not vaults_found:
        print(f"No Key Vaults found in the specified resource group '{resource_group_name}'.")

except HttpResponseError as e:
    print(f"HTTP response error: {e.message}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
