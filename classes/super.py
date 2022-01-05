class Sink:
    def __init__(self, basin, nozzle):
        self.basin = basin
        self.nozzle = nozzle


class KitchenSink(Sink):
    def __init__(self, basin, nozzle, trash_compactor=None):
        super().__init__(basin, nozzle)
        if trash_compactor:
            self.trash_compactor = trash_compactor
