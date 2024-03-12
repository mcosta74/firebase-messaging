import sys
import json

import firebase_admin
from firebase_admin import project_management, credentials


class WebApp:
    def __init__(self, app_id, service) -> None:
        self._app_id = app_id
        self._service = service

    @property
    def app_id(self):
        return self._app_id

    def get_metadata(self):
        return self._service.get_web_app_metadata(self._app_id)

    def get_config(self):
        return self._service.get_web_app_config(self._app_id)


class WebAppsService(project_management._ProjectManagementService):
    WEB_APPS_RESOURCE_NAME = 'webApps'
    WEB_APP_IDENTIFIER_NAME = 'displayName'

    def __init__(self, app):
        super().__init__(app)

    def list_web_apps(self) -> list[WebApp]:
        return self._list_apps(
            platform_resource_name=WebAppsService.WEB_APPS_RESOURCE_NAME,
            app_class=WebApp
        )

    def create_web_app(self, display_name) -> WebApp:
        return self._create_app(
            platform_resource_name=WebAppsService.WEB_APPS_RESOURCE_NAME,
            identifier_name=WebAppsService.WEB_APP_IDENTIFIER_NAME,
            identifier=display_name,
            display_name=None,
            app_class=WebApp)

    def get_web_app_metadata(self, app_id):
        path = '/v1beta1/projects/-/{0}/{1}'.format(
            WebAppsService.WEB_APPS_RESOURCE_NAME,
            app_id,
        )
        return self._make_request('get', path)

    def get_web_app_config(self, app_id):
        path = '/v1beta1/projects/-/{0}/{1}/config'.format(
            WebAppsService.WEB_APPS_RESOURCE_NAME,
            app_id,
        )
        return self._make_request('get', path)


def main(args: list[str]):
    creds = None
    if len(args) > 0:
        with open(args[0], 'r') as conf_file:
            creds = credentials.Certificate(json.load(conf_file))

    app = firebase_admin.initialize_app(creds)

    svc = WebAppsService(app=app)
    app = svc.create_web_app('foo-app')
    print('Metadata:', app.get_metadata())
    print('Config:', app.get_config())


if __name__ == '__main__':
    main(sys.argv[1:])
