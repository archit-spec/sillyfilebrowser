class Video:
    def __init__(self, id, uploader_id, date_of_uplaod, video_length, meta_data):
        self.id = id
        self.uploader_id = uploader_id
        self.date_of_uplaod = date_of_uplaod
        self.video_length = video_length
        self.meta_data = meta_data
    

    def get_metadata(self):
        return self.extra_info

