"""An AWS Python Pulumi program"""

import pulumi
import sys
from pulumi_aws import ec2
# the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py
sys.path.append('/Users/shagoy/code/srf/pulumi-k8s/python/')

import pvu_pulumi_k8s as k8s

vpc = ec2.get_vpc(tags={
        "Component": "landingzone",
    })

cluster_args = k8s.EksClusterArgs(description="test cluster", 
                                    vpc_id=vpc.id
                                    )

cluster = k8s.EksCluster(name="test-cluster", 
                        args=cluster_args
                        )

# Export the name of the bucket
pulumi.export('bucket_name', cluster.arn)
