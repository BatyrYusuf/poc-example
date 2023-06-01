import os
import socket

from huaweicloudsdkas.v1 import *
from huaweicloudsdkas.v1.region.as_region import AsRegion
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from config import AK,SK

def get_instance_id(hostname):
    ak = AK
    sk = SK
    as_id = ""
    credentials = BasicCredentials(ak, sk)
    client = (
        AsClient.new_builder()
        .with_credentials(credentials)
        .with_region(AsRegion.value_of("ap-southeast-3"))
        .build()
    )

    try:
        request = ListScalingGroupsRequest()
        response = client.list_scaling_groups(request)
        data = response.to_json_object()
        scaling_groups = data["scaling_groups"]
        if scaling_groups:
            as_id = scaling_groups[0]["scaling_group_id"]
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


    try:
        request = ListScalingInstancesRequest()
        request.scaling_group_id = as_id
        response = client.list_scaling_instances(request)
        data = response.to_json_object()
        for v in data["scaling_group_instances"]:
            if v.get("instance_name").lower() == hostname:
                instance_id = v.get("instance_id")
                break
        if instance_id:
            return instance_id
        else:
            return "Instance not found"
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
        return e.status_code
