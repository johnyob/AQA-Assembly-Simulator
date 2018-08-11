import json

from aqa_assembly_simulator.helpers.Exceptions import AssemblySimulatorVMConfigException
from aqa_assembly_simulator.helpers.Constants import VM_CONFIG
from aqa_assembly_simulator.helpers.Util import read_file


class VirtualMachineConfig:

    @staticmethod
    def get_config():
        try:
            return json.loads(read_file(VM_CONFIG))
        except:
            raise AssemblySimulatorVMConfigException({
                "message": "virtual machine config not setup. Please use aqa-assembly-simulator config setup."
            })

    @staticmethod
    def get_memory_capacity():
        return VirtualMachineConfig.get_config()["memory capacity"]

    @staticmethod
    def get_registers():
        return VirtualMachineConfig.get_config()["registers"]

