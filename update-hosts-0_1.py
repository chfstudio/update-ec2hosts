#!/usr/bin/env python

"""
Yet another python script for update internal ip address after EC2 Instance reboot/shutdown. 
It uses the "Name" tag into AMI to get all meta data.
Remember: set valid and unique tag name into EC2 Management Console for every Instance.

To install:
1) Insert your AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and your current AWS_REGION. [https://portal.aws.amazon.com/gp/aws/securityCredentials]
2) copy the script into /usr/local/bin/update-hosts.py 
3) insert crontab rule (as root user) like: 
# m h  dom mon dow   command
* * * * * /usr/local/bin/update-hosts.py > /dev/null 2>&1
4) set execution permission: chmod +x /usr/local/bin/update-hosts.py 
5) Check your updated /etc/hosts file
6) Repeat for all Instances
"""

__license__ = """\
Copyright (c) 2012 Mochunk srl <support@mochunk.com>

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.\
"""


AWS_SECRET_ACCESS_KEY='XXXXXXXXXXXXXXXXXX'
AWS_ACCESS_KEY_ID='XXXXXXXXXXXXXXX'
AWS_REGION='eu-west-1'

import boto
import boto.ec2
import shutil

ec2 = boto.ec2.connect_to_region(AWS_REGION,aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
instances=[]
for r in ec2.get_all_instances():
	 instances.extend(r.instances)

hosts=[]
ip=[]
for item in instances:
	hosts.append(item.tags['Name'])
	if not item.private_ip_address is None:	
	   ip.append(item.private_ip_address)
	else:
	   ip.append("")

myhost=open('/etc/hosts','r')
tmp=open('/tmp/htmp','w')

lines = myhost.readlines()

for host in lines:
	line=host.split()	 
	if len(line)>0:
		if line[1] in hosts:
	   		index=hosts.index(line[1])
			if ip[index] !="":
			  tmp.write(ip[index]+' '+hosts[index]+'\n')
			del hosts[index] 
			del ip[index]	
		else:
		  tmp.write(host)
	else:
	   tmp.write(host)

myhost.close()

for i in range(0,len(hosts)):
	if ip[i]!="":
	  tmp.write(ip[i]+" "+hosts[i]+"\n")

tmp.close()	   
								
shutil.copy2('/tmp/htmp','/etc/hosts')
