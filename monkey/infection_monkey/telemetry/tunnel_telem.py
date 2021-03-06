from common.common_consts.telem_categories import TelemCategoryEnum
from infection_monkey.control import ControlClient
from infection_monkey.telemetry.base_telem import BaseTelem


class TunnelTelem(BaseTelem):
    def __init__(self):
        """
        Default tunnel telemetry constructor
        """
        super(TunnelTelem, self).__init__()
        self.proxy = ControlClient.proxies.get("https")

    telem_category = TelemCategoryEnum.TUNNEL

    def get_data(self):
        return {"proxy": self.proxy}
