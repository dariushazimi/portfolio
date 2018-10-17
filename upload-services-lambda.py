import boto3
from io import BytesIO
import zipfile
import mimetypes


#s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
s3 = boto3.resource('s3')
service_bucket = s3.Bucket('services.readspeech.com')
build_bucket = s3.Bucket('servicesbuild.readspeech.com')
service_zip = BytesIO()
build_bucket.download_fileobj('servicesbuild.zip', service_zip)

with zipfile.ZipFile(service_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        service_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
        service_bucket.Object(nm).Acl().put(ACL='public-read')