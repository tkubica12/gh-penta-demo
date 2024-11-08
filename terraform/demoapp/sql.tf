variable "sql_server_name" {
  type        = string
  default     = "gh-sql-server"
  description = "Name of the Azure SQL server."
}

variable "sql_admin_username" {
  type        = string
  default     = "sqladmin"
  description = "Admin username for the Azure SQL server."
}

variable "sql_admin_password" {
  type        = string
  description = "Admin password for the Azure SQL server."
}

variable "sql_database_name" {
  type        = string
  default     = "ghsqldb"
  description = "Name of the Azure SQL database."
}

resource "azurerm_sql_server" "main" {
  name                         = var.sql_server_name
  resource_group_name          = azurerm_resource_group.main.name
  location                     = azurerm_resource_group.main.location
  version                      = "12.0"
  administrator_login          = var.sql_admin_username
  administrator_login_password = var.sql_admin_password
}

resource "azurerm_sql_database" "main" {
  name                = var.sql_database_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  server_name         = azurerm_sql_server.main.name
  sku_name            = "Basic"
}

output "sql_connection_string" {
  value = "Server=${azurerm_sql_server.main.name}.database.windows.net;Database=${azurerm_sql_database.main.name};User Id=${azurerm_sql_server.main.administrator_login};Password=${azurerm_sql_server.main.administrator_login_password};"
}
