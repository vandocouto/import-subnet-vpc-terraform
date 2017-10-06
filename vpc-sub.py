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
file.close()

# generate subnets.tf
json_data=open("sn/aws-sn.json").read()
data = json.loads(json_data)

num=(len(data["Subnets"]))
count=0
list=[]
subnets=""
while ( count < num ):
   subnets+= '"%s", '  %(str((data["Subnets"][count]["SubnetId"])))
   count = count + 1

file = open(DirProjSUB, "w")
file.write('variable "subnet" {\n\
type = "list"\n\
default = [%s]\n\
}\n\
' %(subnets[0:-2]
   ))
file.close()


print subnets[0:-2]


