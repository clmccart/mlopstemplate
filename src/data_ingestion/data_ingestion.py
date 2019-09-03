class DataIngestor:
    def __init__(self, desired_file=None, secret_provider=None, service=None):
        self.service = service(desired_file, secret_provider) 

    def get_df(self):
        return self.service.get_df()