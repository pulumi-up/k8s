"""An AWS Python Pulumi program"""

import pulumi
import sys
from pulumi_aws import ec2
# the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py
sys.path.append('/Users/shagoy/code/srf/pulumi-eks/python/')

import patrickwolleb_pulumi_eks as eks

vpc = ec2.get_vpc(tags={
        "Component": "landingzone",
    })

cluster_args = eks.EksClusterArgs(description="test cluster", 
                                    vpc_id=vpc.id
                                    )

cluster = eks.EksCluster(name="test-cluster", 
                        args=cluster_args
                        )

# Export the name of the bucket
pulumi.export('bucket_name', cluster.arn)
