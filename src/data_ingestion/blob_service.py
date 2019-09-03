from azure.storage.blob import BlockBlobService

class BlobService(iService):
    
    def get_df(self):
        self.set_up_secrets()
        self.connect_to_blob()
        self.pull_file()
        return self.df
    
    def connect_to_blob(self):
        pass
    
    def pull_file(self):
        pass