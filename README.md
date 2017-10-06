

Passo 1 - Configure AccessKeys e SecretKeys

    aws configure

Passo 2 - Valide executando os comandos abaixo

    aws ec2 describe-subnets
    aws ec2 describe-vpcs

Passo 3 - Clone do projeto

    git clone https://github.com/vandocouto/import-subnet-vpc-terraform.git

Passo 4 - Acesso o projeto

    cd import-subnet-vpc-terraform

Passo 5 - Execute o script vpc-sub.py

    python vpc-sub.py

Passo 6 - Ajuste o arquivo de variávies

     cd ec2/projeto1/
     vim variables.tf

Passo 7 - Rode o terraform init - plan - apply para cria a chave pem

     cd key-pairs/
     terraform init
     terraform plan
     terraform apply

Passo 8 - Rode o terraform init - plan - apply para criar a instância EC2

     cd ..
     terraform init
     terraform plan
     terraform apply

Passo 10 - Para destruir o projeto execute o terraform destroy

    terraform destroy







