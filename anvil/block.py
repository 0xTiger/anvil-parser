from nbt import nbt
from frozendict import frozendict

class Block:
    def __init__(self, namespace: str, id: str, properties: dict=None):
        self.namespace = namespace
        self.id = id
        self.properties = properties or {}

    def name(self):
        return self.namespace + ':' + self.id

    def __repr__(self):
        return f'<Block({self.name()})>'

    def __eq__(self, other):
        if type(other) != Block: return False
        return self.namespace == other.namespace and self.id == other.id and self.properties == other.properties

    def __hash__(self):
        return hash(self.name()) ^ hash(frozendict(self.properties))

    @classmethod
    def from_name(cls, name: str, *args, **kwargs):
        """Creates a new Block from the block's name (namespace:id)"""
        namespace, id = name.split(':')
        return cls(namespace, id, *args, **kwargs)

    @classmethod
    def from_palette(cls, tag: nbt.TAG_Compound):
        """Creates a new Block from the tag format on Section.Palette"""
        name = tag['Name'].value
        properties = tag.get('Properties')
        if properties: properties = dict(properties)
        return cls.from_name(name, properties=properties)