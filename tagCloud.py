class TagCloud:
    def __int__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0)+1


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")

print(cloud.tags)
