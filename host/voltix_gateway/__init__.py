"""Voltix Gateway Python package"""

__version__ = "1.0.0"

import base64
import numpy as np

from voltix_gateway.client import GatewayClient
from voltix_gateway.packet_model import PacketApiSend
from voltix_gateway.transceiver import Transceiver


def base64_to_numpy(data_b64: bytes, dtype=np.uint8):
    data_bin = base64.urlsafe_b64decode(data_b64)
    data_np = np.frombuffer(data_bin, dtype)
    if len(data_np) == 1:
        return data_np[0]
    return data_np


def base64_to_devid(dev_id_b64: bytes) -> int:
    return int(base64_to_numpy(dev_id_b64, np.uint32))


def base64_to_str(data_b64: bytes):
    data_bin = base64.urlsafe_b64decode(data_b64)
    return str(data_bin)
