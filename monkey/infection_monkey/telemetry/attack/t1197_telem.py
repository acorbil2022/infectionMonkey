from infection_monkey.telemetry.attack.victim_host_telem import VictimHostTelem


class T1197Telem(VictimHostTelem):
    def __init__(self, status, machine, usage):
        # TODO: rename parameter "usage" to avoid confusion with parameter "usage" in UsageTelem
        #  techniques
        """
        T1197 telemetry.
        :param status: ScanStatus of technique
        :param machine: VictimHost obj from model/host.py
        :param usage: Usage string
        """
        super(T1197Telem, self).__init__("T1197", status, machine)
        self.usage = usage

    def get_data(self):
        data = super(T1197Telem, self).get_data()
        data.update({"usage": self.usage})
        return data
