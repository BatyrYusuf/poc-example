from obs import ObsClient
from config import AK,SK
obsClient = ObsClient(
    access_key_id=AK,
    secret_access_key=SK,
    server="obs.ap-southeast-3.myhuaweicloud.com",
)


def callback(transferredAmount, totalAmount, transferSpeed):
    print(
        "\rProgress: %.2f%%; Speed: %.2f MB/s; Transferred: %.2f MB"
        % (
            transferredAmount * 100.0 / totalAmount,
            transferSpeed / 1024.0 / 1024.0,
            transferredAmount / 1024.0 / 1024.0,
        ),
        end=" ",
    )


def upload_to_obs(data):
    uploadFile = str(data)
    taskNum = 2
    partSize = 10 * 1024 * 1024
    enableCheckpoint = True
    try:
        resp = obsClient.uploadFile(
            "bipmeet-demo",
            f"./{uploadFile}",
            uploadFile,
            partSize,
            taskNum,
            enableCheckpoint,
            progressCallback=callback,
        )
        if resp.status < 300:
            print("requestID:", resp.requestId)
        else:
            print("errorCode:", resp.errorCode)
            print("errorMessage:", resp.errorMessage)
    except Exception as e:
        print("error:", e)
        import traceback

        print("traceback.format_exc():\n%s" % traceback.format_exc())
