from manage_db import load_tags, load_row


class Record:
    def __init__(self, reid, retype, repath, desc, theme, source, date) -> None:
        self.id = reid
        self.type = retype
        self.path = repath
        self.description = desc
        self.theme = theme
        self.source = source
        self.date = date
        self.tags = None
    
    @classmethod
    def from_database(cls, reid):
        args = load_row(reid)
        return cls(reid, *args)

    def set_tags(self):
        self.tags = load_tags(self.id)

    def __str__(self) -> str:
        pass


def create_records(id_list):
    records = []
    for res_id in id_list:
        record = Record(res_id)
        record.set_tags()
        records.append(record)
