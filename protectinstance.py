import os
import socket

from huaweicloudsdkas.v1 import *
from huaweicloudsdkas.v1.region.as_region import AsRegion
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from config import AK,SK

def protect(instance_id):
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
        request = BatchProtectScalingInstancesRequest()
        request.scaling_group_id = as_id
        listInstancesIdbody = [instance_id]
        request.body = BatchProtectInstancesOption(
            action="PROTECT", instances_id=listInstancesIdbody
        )
        response = client.batch_protect_scaling_instances(request)
        return "Instance is now protected"
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
        return "Instance is not protected"


def unprotect(instance_id):
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
        request = BatchUnprotectScalingInstancesRequest()
        request.scaling_group_id = as_id
        listInstancesIdbody = [instance_id]
        request.body = BatchUnprotectInstancesOption(
            action="UNPROTECT", instances_id=listInstancesIdbody
        )
        response = client.batch_unprotect_scaling_instances(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
