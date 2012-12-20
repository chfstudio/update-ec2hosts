Yet another python script for update internal ip address after EC2 Instance reboot/shutdown. 
It uses the "Name" tag into AMI to get all meta data.

Remember: set valid and unique tag name into EC2 Management Console for every Instance.

To install:

1) Insert your AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and your current AWS_REGION. [https://portal.aws.amazon.com/gp/aws/securityCredentials]
2) copy the script into /usr/local/bin/update-hosts.py 
3) insert crontab rule (as root user) like: 
* * * * * * /usr/local/bin/update-hosts.py > /dev/null 2>&1
4) set execution permission: chmod +x /usr/local/bin/update-hosts.py 
5) Check your updated /etc/hosts file
6) Repeat for all Instances

Copyright (c) 2012 Mochunk srl [http://www.mochunk.com] <support@mochunk.com>

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


