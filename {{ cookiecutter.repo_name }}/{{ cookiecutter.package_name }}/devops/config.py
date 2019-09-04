# -*- coding: utf-8 -*-

from configirl import ConfigClass, Constant, Derivable


class Config(ConfigClass):
    METADATA = Constant(default=dict())

    PROJECT_NAME = Constant()
    PROJECT_NAME_SLUG = Derivable()

    @PROJECT_NAME_SLUG.getter
    def get_project_name_slug(self):
        return self.PROJECT_NAME.get_value().replace("_", "-")

    STAGE = Constant()  # example dev / test / prod

    ENVIRONMENT_NAME = Derivable()

    @ENVIRONMENT_NAME.getter
    def get_ENVIRONMENT_NAME(self):
        return "{}-{}".format(self.PROJECT_NAME_SLUG.get_value(self), self.STAGE.get_value())
