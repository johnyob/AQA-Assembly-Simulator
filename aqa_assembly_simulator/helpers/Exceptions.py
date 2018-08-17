class AssemblySimulatorVMConfigException(Exception):

    def __str__(self):
        return "[ERROR] Error: AssemblySimulatorConfigError, Response: {0}".format(super().__str__())
