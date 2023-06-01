# coding: utf-8
from huaweicloudsdkas.v1 import *
from huaweicloudsdkas.v1.region.as_region import AsRegion
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions

if __name__ == "__main__":
    ak = "<YOUR AK>"
    sk = "<YOUR SK>"

    credentials = BasicCredentials(ak, sk)
    client = (
        AsClient.new_builder()
        .with_credentials(credentials)
        .with_region(AsRegion.value_of("tr-west-1"))
        .build()
    )

    try:
        request = ListScalingInstancesRequest()
        request.scaling_group_id = "asdasd"
        response = client.list_scaling_instances(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
