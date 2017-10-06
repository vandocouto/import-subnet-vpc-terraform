import subprocess
import re
import json
import os

# execute bash
os.system('aws ec2 describe-subnets > sn/aws-sn.json')
os.system('aws ec2 describe-vpcs > vpc/aws-vpc.json')

# VPC Default = 0
VPCiD=0
# Directory do Project EC2
DirProjVPC="ec2/projeto1/vpc.tf"
DirProjSUB="ec2/projeto1/subnets.tf"

# generate vpc.tf
json_data=open("vpc/aws-vpc.json").read()
data = json.loads(json_data)
vpc='"%s"' %data["Vpcs"][VPCiD]["VpcId"]
print vpc


file = open(DirProjVPC, "w")
file.write('variable "vpcid" {\n\
type = "list"\n\
default = [%s]\n\
}\n\
' %(vpc
   ))

# generate subnets.tf
json_data=open("sn/aws-sn.json").read()
data = json.loads(json_data)
subnets='"%s", "%s", "%s", "%s"' \
        %(data["Subnets"][VPCiD]["SubnetId"], data["Subnets"][1]["SubnetId"], data["Subnets"][2]["SubnetId"], data["Subnets"][3]["SubnetId"])
print subnets


file = open(DirProjSUB, "w")
file.write('variable "subnet" {\n\
type = "list"\n\
default = [%s]\n\
}\n\
' %(subnets
   ))