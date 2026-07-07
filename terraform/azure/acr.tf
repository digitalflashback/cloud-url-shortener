resource "azurerm_container_registry" "main" {
  name                = "cloudurlshortacr"
  resource_group_name = azurerm_resource_group.main.name
  location            = "North Europe"

  sku = "Basic"

  admin_enabled = false
}