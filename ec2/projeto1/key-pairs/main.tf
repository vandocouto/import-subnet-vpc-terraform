data "terraform_remote_state" "vpc" {
  backend = "local"

  config {
    path = "../../../vpc/terraform.tfstate"
  }
}
resource "null_resource" "key-create" {
  provisioner "local-exec" {
    command = "ssh-keygen -b 4096 -t rsa -N '' -C projeto1 -f projeto1.pem"
  }
}