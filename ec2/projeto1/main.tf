resource "aws_key_pair" "key-public" {
  key_name = "${var.key}"
  public_key = "${file("key-pairs/projeto1.pem.pub")}"
}

resource "aws_security_group" "ec2" {
  //count = "${var.instance}"
  name = "${var.sg_name}"
  vpc_id = "${element(var.vpcid, count.index)}"
  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = [
      "0.0.0.0/0"]
  }

  ingress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = [
      "10.0.0.0/21"]
  }

  ingress {
    from_port = 8200
    to_port = 8200
    protocol = "tcp"
    cidr_blocks = [
      "0.0.0.0/0"]
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = [
      "0.0.0.0/0"]
  }
}

# deploy projeto1
resource "aws_instance" "ec2-projeto1" {
  count = "${var.instance}"
  subnet_id = "${element(var.subnet, count.index)}"
  instance_type = "${var.type}"
  ami = "${var.ami}"
  key_name = "${var.key}"
  security_groups = [
    "${aws_security_group.ec2.id}"]
  associate_public_ip_address = true

  root_block_device {
    volume_size = "${var.size_so}"
    volume_type = "${var.type_disk_so}"
  }

  tags {
    Name = "${var.tag}"
  }

  provisioner "remote-exec" {
    connection {
      user = "${var.ssh_user_name}"
      private_key = "${file("key-pairs/projeto1.pem")}"
    }

    inline = [
      "sudo apt-get update -y",
      "sudo apt-get install python-simplejson -y",
    ]
  }
}