"""
Contains a Pulumi ComponentResource for creating an EKS cluster.
"""
import json
from typing import Any, Mapping, Optional, Sequence, Union, overload

import pulumi
from pulumi import ResourceOptions
from pulumi_aws import cloudwatch, config, ec2, iam
import pulumi_eks as eks




class EksClusterArgs:
    """
    The arguments necessary to construct a `Eks` resource.
    """

    def __init__(self,
                description: str,
                vpc_id: str
                ):
                #  base_tags: Mapping[str, str],
                #  availability_zone_names: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        Constructs a EksClusterArgs.

        :param description: A human-readable description used to construct resource name tags.
    
        """
        self.description = description
        self.vpc_id = vpc_id
        # self.base_tags = base_tags
        # self.availability_zone_names = availability_zone_names


class EksCluster(pulumi.ComponentResource):
    """
    Creates an EKS cluster using Pulumi. The EKS cluster consists of:

      - DHCP options for the given private hosted zone name
      - An Internet gateway
      - Subnets of appropriate sizes for public and private subnets, for each availability zone specified
      - A route table routing traffic from public subnets to the internet gateway
      - NAT gateways (and accoutrements) for each private subnet, and appropriate routing
      - Optionally, S3 and DynamoDB endpoints
    """

    def __init__(self,
                 name: str,
                 args: EksClusterArgs,
                 opts: ResourceOptions = None):
        """
        Constructs a Vpc.

        :param name: The Pulumi resource name. Child resource names are constructed based on this.
        :param args: A EksClusterArgs object containing the arguments for EksCluster construction.
        :param opts: A pulumi.ResourceOptions object.
        """
        super().__init__('EksCluster', name, None, opts)

        # Make base info available to other methods
        self.name = name
        self.description = args.description
        # self.base_tags = args.base_tags
        # self.availability_zone_names = args.availability_zone_names
        self.arn = "1"
        # # # Create VPC and Internet Gateway resources
        role0 = create_role("example-role0")
        role1 = create_role("example-role1")
        role2 = create_role("example-role2")

        cluster_args = eks.ClusterArgs(
            p
        )

        # Create an EKS cluster.
        cluster = eks.Cluster(f"{name}-cluster",
                            vpc_id=args.vpc_id,
                            skip_default_node_group=True,
                            instance_roles=[role0, role1, role2],
                            
                            opts=ResourceOptions(parent=self))

def create_role(name: str) -> iam.Role:
    
    managed_policy_arns = [
        "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
        "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
        "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
    ]

    role = iam.Role(name, assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowAssumeRole",
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com",
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }))

    for i, policy in enumerate(managed_policy_arns):
        # Create RolePolicyAttachment without returning it.
        rpa = iam.RolePolicyAttachment(f"{name}-policy-{i}",
            policy_arn=policy,
            role=role.id)

    return role