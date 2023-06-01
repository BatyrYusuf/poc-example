from huaweicloudsdkas.v1 import *
from huaweicloudsdkas.v1.region.as_region import AsRegion
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from config import AK,SK

def scale_out():
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
        request = ShowScalingGroupRequest()
        request.scaling_group_id = as_id
        response = client.show_scaling_group(request)
        data = response.to_json_object()
        desire_state = data["scaling_group"]["desire_instance_number"]
        min_state = data["scaling_group"]["min_instance_number"]
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)

    try:
        request = UpdateScalingGroupRequest()
        request.scaling_group_id = as_id
        request.body = UpdateScalingGroupOption(
            max_instance_number=100,
            desire_instance_number=(desire_state+1),
            min_instance_number=(min_state + 1)
        )
        response = client.update_scaling_group(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)

def scale_in():
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
        request = ShowScalingGroupRequest()
        request.scaling_group_id = as_id
        response = client.show_scaling_group(request)
        data = response.to_json_object()
        desire_state = data["scaling_group"]["desire_instance_number"]
        min_state = data["scaling_group"]["min_instance_number"]
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)

    try:
        request = UpdateScalingGroupRequest()
        request.scaling_group_id = as_id
        request.body = UpdateScalingGroupOption(
            max_instance_number=100,
            desire_instance_number=(desire_state - 1),
            min_instance_number=(min_state - 1)
        )
        response = client.update_scaling_group(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
