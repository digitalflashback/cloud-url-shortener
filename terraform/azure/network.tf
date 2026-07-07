resource "azurerm_virtual_network" "main" {
  name                = "cloud-url-shortener-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = "North Europe"
  resource_group_name = azurerm_resource_group.main.name
}


resource "azurerm_subnet" "aks" {
  name                 = "aks-subnet"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.0.1.0/24"]
}


resource "azurerm_subnet" "database" {
  name                 = "database-subnet"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.0.2.0/24"]
}