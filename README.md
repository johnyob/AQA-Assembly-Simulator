# AQA Assembly Simulator

> A simple virtual machine for the AQA assembly instruction set

This is an easy-to-use Python virtual machine for the AQA assembly instruction set. A Command Line Interface (CLI) is also used to configure and interact with the virtual machine.

## Features

- [x] Setup config for the virtual machine
- [x] Show config for the virtual machine
- [x] Execute AQA assembly programs

## Installation

To install *AQA Assembly Simulator* use:

```sh
python -m pip install --no-cache-dir --index-url https//test.pypi.org/simple/ aqa-assembly-simulator
```

## Usage

### Help
```sh
C:\>aqa-assembly-simulator -help
AQA Assembly Simulator

Usage:
  aqa-assembly-simulator config setup
  aqa-assembly-simulator config show
  aqa-assembly-simulator execute <file> [--trace]

Options:
  -h --help                 Show this screen.
  --version                 Show version.
  --trace                   Shows program counter, registers and memory during VM execution.

Help:
  For help, please see https://github.com/johnyob/AQA-Assembly-Simulator
```

### Config Setup

To setup the virtual machine config the command ``aqa-assembly-simulator config setup`` must be used. It should be noted that if the virtual machine config has not been setup using ``config setup`` and a different command is used then a ``AssemblySimulatorVMConfigException`` is raised.

```sh
C:\>aqa-assembly-simulator config setup
Enter number of registers in the virtual machine: 6
Enter number of addressable memory units in the virtual machine: 48

Virtual Machine Config
 +-----------------+-------+
 |      Name       | Value |
 +-----------------+-------+
 | registers       | 6     |
 | memory capacity | 48    |
 +-----------------+-------+

```

### Config Show

To display the virtual machine config the command ``aqa-assembly-simulator config show`` must be used.

```sh
C:\>aqa-assembly-simulator config show

Virtual Machine Config
 +-----------------+-------+
 |      Name       | Value |
 +-----------------+-------+
 | registers       | 6     |
 | memory capacity | 48    |
 +-----------------+-------+

```

### Execute

To execute AQA assembly programs on the virtual machine, the command ``aqa-assembly-simulator execute <file> [--trace]`` must be used, where `<file>` is the absolute file path for the file containing the AQA assembly instructions and `[--trace]` is an optional argument that indicates whether the program counter, register contents, comparison register contents and memory contents are printed after each instruction is executed.

Contents of asm:
```asm
LDR r1, 0
CMP r1, #0
BGT then
B endif
then:
  SUB r1, r1, #1
  STR r1, 0
endif:
  HALT
```

```sh
C:/>aqa-assembly-simulator execute asm

Program Counter: 9

Register
 +---+---+---+---+---+---+
 | 1 | 2 | 3 | 4 | 5 | 6 |
 +---+---+---+---+---+---+
 | 9 | 0 | 0 | 0 | 0 | 0 |
 +---+---+---+---+---+---+

Comparison Register
 +----+----+----+----+
 | EQ | NE | GT | LT |
 +----+----+----+----+
 | 0  | 1  | 1  | 0  |
 +----+----+----+----+

Memory
 +-----------+--------+
 | Addresses | Values |
 +-----------+--------+
 | 0         | 9      |
 | 1         | 0      |
 | 2         | 0      |
 | 3         | 0      |
 | 4         | 0      |
 | 5         | 0      |
 | 6         | 0      |
 | 7         | 0      |
 | 8         | 0      |
 | 9         | 0      |
 | 10        | 0      |
 | 11        | 0      |
 | 12        | 0      |
 | 13        | 0      |
 | 14        | 0      |
 | 15        | 0      |
 | 16        | 0      |
 | 17        | 0      |
 | 18        | 0      |
 | 19        | 0      |
 | 20        | 0      |
 | 21        | 0      |
 | 22        | 0      |
 | 23        | 0      |
 | 24        | 0      |
 | 25        | 0      |
 | 26        | 0      |
 | 27        | 0      |
 | 28        | 0      |
 | 29        | 0      |
 | 30        | 0      |
 | 31        | 0      |
 | 32        | 0      |
 | 33        | 0      |
 | 34        | 0      |
 | 35        | 0      |
 | 36        | 0      |
 | 37        | 0      |
 | 38        | 0      |
 | 39        | 0      |
 | 40        | 0      |
 | 41        | 0      |
 | 42        | 0      |
 | 43        | 0      |
 | 44        | 0      |
 | 45        | 0      |
 | 46        | 0      |
 | 47        | 0      |
 +-----------+--------+

```  

Note: *10* is stored in memory address *0* initially.

## Instruction Set

| Instruction | Description|
| --- | --- |
| LDR r_d, \<memory reference\> | Load the value stored in the memory location specified by **\<memory reference\>** into register **r_d**. |
| STR r_d, \<memory reference\> | Store the value that is in register **r_d** into the memory location specified by **\<memory reference\>**. |
| ADD r_d, r_n, \<operand 2\> | Add the value specified in **\<operand 2\>** to the value in register **r_n** and store the result in register **r_d**. |
| SUB r_d, r_n, \<operand 2\> | Subtract the value specified by **\<operand 2\>** from the value in register **r_n** and store the result in register **r_d**. |
| MOV r_d, \<operand 2\> | Copy the value specified by **\<operand 2\>** into register **r_d**. |
| CMP r_d, \<operand 2\> | Compare the value stored in register **r_d** with the value specified by **\<operand 2\>**. |
| B \<label\> | Always branch to the instruction at position **\<label\>** in the program. |
| B\<condition\> \<label\> | Conditionally branch to the instruction at position **\<label\>** in the program if the last comparison met the criteria specified by the **\<condition\>**. Possible values for **\<condition\>** and their meaning are: <ul><li>**EQ**: equal to</li><li>**NE**: not equal to</li><li>**GT**: greater than</li><li>**LT**: less than</li></ul> |
| AND r_d, r_n, \<operand 2\> | Perform a bitwise logical AND operation between the value in register **r_n** and the value specified by **\<operand 2\>** and store the result in register **r_d**. |
| ORR r_d, r_n, \<operand 2\> | Perform a bitwise logical OR operation between the value in register **r_n** and the value specified by **\<operand 2\>** and store the result in register **r_d**. |
| EOR r_d, r_n, \<operand 2\> | Perform a bitwise logical XOR operation between the value in register **r_n** and the value specified by **\<operand 2\>** and store the result in register **r_d**. |
| MVN r_d, \<operand 2\> | Perform a bitwise logical NOT operation on the value specified by **\<operand 2\>** and store the result in register **r_d**. |
| LSL r_d, r_n, \<operand 2\> | Logically shift left the value stored in register **r_n** by the number of bits specified by **\<operand 2\>** and store the result in register **r_d**. |
| LSR r_d, r_n, \<operand 2\> | Logically shift right the value stored in register **r_n** by the number of bits specified by **\<operand 2\>** and store the result in register **r_d**. |
| HALT | Stops the execution of the program. |

**<operand 2>** can be interpreted in two different ways, depending upon whether the first symbol is a *#* or an *r*:
- *#* - Use the decimal value (integer) specified after the *#*, e.g. **#25** means use the decimal value **25**.
- *rd* - Use the value stored in register **d**, e.g. **r4** means use the value stored in register **4**.

## Errors
If you discover an error within this package, please email [me](mailto:alistair.o'brien@ellesmere.com).

## Credits
- [Alistair O'Brien](https://github.com/johnyob)
