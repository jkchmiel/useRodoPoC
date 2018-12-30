import json

class JSONSerializable:
    def to_json(self):
        return json.dumps(self, default=lambda o: vars(o), sort_keys=True)

    def __repr__(self):
        return self.to_json()