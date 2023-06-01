import os
import socket

from flask import Flask
from flask import render_template
from flask import request
from huaweicloudsdkas.v1 import *
from huaweicloudsdkas.v1.region.as_region import AsRegion
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions

from asconf import scale_in
from asconf import scale_out
from getinstanceid import get_instance_id
from obsbucket import upload_to_obs
from protectinstance import protect, unprotect
import time

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def data_page():
    hostname = socket.gethostname()
    if request.method == "POST":
        instance_id = get_instance_id(hostname)
        protect(instance_id)
        scale_out()
        filesDict = request.files.to_dict()
        uploadData = request.files["media"]
        data_file_name = uploadData.filename
        upload_to_obs(data_file_name)
        time.sleep(60)
        unprotect(instance_id)
        scale_in()
    return render_template("upload.html", hostname=hostname)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
