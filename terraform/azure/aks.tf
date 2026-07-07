resource "azurerm_kubernetes_cluster" "main" {
  name                = "cloud-url-shortener-aks"
  location            = "North Europe"
  resource_group_name = azurerm_resource_group.main.name

  dns_prefix = "cloudurlshortener"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "standard_ec2as_v5"

    vnet_subnet_id = azurerm_subnet.aks.id
  }

  identity {
    type = "SystemAssigned"
  }

  network_profile {
    network_plugin    = "azure"
    load_balancer_sku = "standard"
    service_cidr   = "10.2.0.0/16"
    dns_service_ip = "10.2.0.10"
  }
}