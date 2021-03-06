# CloudFormation Templates

Miscellaneous CloudFormation templates with a description and launch link.  Unless otherwise noted, they should work in all regions.

## NFS Templates

This is a set of CloudFormation templates that will bring up an instance, configure an NFS server, and export it out to the chosen CIDR block with the given NFS options.  There are several options and features to each of the templates, and they should be used as a starting point to configure you own templates.

###  NFS Server using EBS on ZFS

Description | JSON File | Launch
----------- | --------- | ------
Launch NFS server using EBS on ZFS | [EBS_NFS_Server_on_zfs.json](https://github.com/awslabs/aws-cfn-control/blob/master/cloudformation/json/EBS_NFS_Server_on_zfs.json) | [![cloudformation-launch-stack](/images/deploy_to_aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=ebs-nfs-server-on-zfs&templateURL=https://s3.amazonaws.com/cfn-control-public/EBS_NFS_Server_on_zfs.json) |

**Details:**
* REQUIRES Internet access (direct or NAT GW) for initial setup
* Launch instance with latest RHEL or CentOS
* Attach 10 EBS volumes (size determined from input)
* Install ZFS packages and dependencies
* Create RAID6 ZFS pool
* Create ZFS file system
* Setup NFS and export ZFS FS over NFS
* Example mount command shown in stack output




---







