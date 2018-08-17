import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

requires = [
    "docopt",
    "ascii-table>=0.0.2"
]

packages = [
    "aqa_assembly_simulator",
    "aqa_assembly_simulator.virtual_machine",
    "aqa_assembly_simulator.virtual_machine.config",
    "aqa_assembly_simulator.parser",
    "aqa_assembly_simulator.lexer",
    "aqa_assembly_simulator.helpers",
    "aqa_assembly_simulator.error",
    "aqa_assembly_simulator.commands",
    "aqa_assembly_simulator.commands.config"
]

setuptools.setup(
    name="aqa-assembly-simulator",
    version="0.0.2",
    author="Alistair O'Brien",
    author_email="alistair.o'brien@ellesmere.com",
    description="A virtual machine for the AQA assembly instruction set.",
    long_description=long_description,
    include_package_data=True,
    long_description_content_type="text/markdown",
    url="https://github.com/johnyob/AQA-Assembly-Simulator",
    packages=packages,
    install_requires=requires,
    entry_points={
        "console_scripts": [
            "aqa-assembly-simulator=aqa_assembly_simulator.__main__:main"
        ]
    }
)