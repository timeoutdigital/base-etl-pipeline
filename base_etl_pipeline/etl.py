import abc

from base_etl_pipeline import logs


class TOETLPipeline(metaclass=abc.ABCMeta):

    def __init__(self, app_name, env, gcp_credentials, aws_session):

        self.app_name = app_name

        self.gcp_credentials = gcp_credentials

        self.aws_session = aws_session

        self.logger = logs.Client(self.app_name).logger

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def cleanup(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):

        try:
            self.run(*args, **kwargs)
        finally:
            self.cleanup()
