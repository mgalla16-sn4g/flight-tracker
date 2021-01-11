import yaml
from google.cloud import secretmanager

with open('config.yml') as file:
	settings_from_yml = yaml.load(file, Loader=yaml.FullLoader)

secrets = secretmanager.SecretManagerServiceClient()

settings_from_gcp = {
	'bucket-name': secrets.access_secret_version(request={"name": "projects/all-in-one-300017/secrets/bucket-name/versions/1"}).payload.data.decode("utf-8"),
	'object-name': secrets.access_secret_version(request={"name": "projects/all-in-one-300017/secrets/object-name/versions/1"}).payload.data.decode("utf-8")
	# 'bucket-name': secrets.get_secret(name="projects/all-in-one-300017/secrets/bucket-name"),
	# 'object-name': secrets.get_secret(name="projects/all-in-one-300017/secrets/object-name")
}

settings = {**settings_from_yml, **settings_from_gcp}
