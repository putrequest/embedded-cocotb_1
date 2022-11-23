# PUTrequest_ - Embedded Security, Intro to cocotb

This repository contains instructions and solutions for the workshop carried out on first meeting of Embbeded Security team that's a part of `PUTrequest_` academic circle at Poznań University of Technology.


# Prerequisites

This section contains information about software required to solve worskhop tasks.

## cocotb

Cocotb is a COroutine based COsimulation TestBench environment for verifying VHDL and SystemVerilog RTL using Python.

To install it, use pip:
```bash
pip install cocotb pytest
```
It is recommended to use virtual environment. For more information about installation follow [official guide](https://docs.cocotb.org/en/stable/index.html).

## Verilator

Cocotb cooperates with external simulators in order to simulate provided RTL code. In this case we will use Verilator which generated a C-equivalent code for RTL that can be later executed as a binary. Cocotb doesn't support versions newer than v4.106 so it's recommended to install this one.

```bash
git clone https://github.com/verilator/verilator
cd verilator
git checkout v4.106
autoconf            # Create ./configure script
export VERILATOR_ROOT=`pwd`
./configure         # Configure and create Makefile
make -j `nproc`     # Build Verilator itself (if error, try just 'make')
sudo make install
```
For more information about installation follow [official guide](https://verilator.org/guide/latest/install.html).

## GTKWave

Code simulated by Verilator can be traced and dumped into `.vcd` or `.fst` file. In order to view this, you need an external tool, e.g. GTKWave.

```bash
sudo apt install GTKWave
```


# Tasks

## Examples - Adder

Look at [cocotb/examples/adder](cocotb/examples/adder). It represents a module that is combinatorial and adds two 4-bit logic values.

**Task:**

Modify `adder.sv` and `test_adder.py` to make this module synchronous.

## Sample - add timer trigger

Look at [sample](sample). It represent a very simple module that inverts ("encrypts") input value and writes it to output.

**Task:**

Modify [sample.sv](sample/sample.sv) and [test_sample.py](sample/test_sample.py) to insert there a simple trojan that would trigger under a timer set to 2500 us. Note that clock period is set to 10 us. Add tests in your test bench to check if it works as intended.

**IMPORTANT:**

Do not modify module interface, all input and output signals must not be modified.

## Sample - add sequence trigger

Look at [sample](sample). It represent a very simple module that inverts ("encrypts") input value and writes it to output.

**Task:**
Modify [sample.sv](sample/sample.sv) and [test_sample.py](sample/test_sample.py) to insert there a simple trojan that would trigger under a following sequence on input: `0x21` -> `0xf1` -> `0x37`. Add tests in your test bench to check if it works as intended.


**IMPORTANT:**

Do not modify module interface, all input and output signals must not be modified.

**Possible enhancement:**

By default this this trojan will activate on a last value which means that the `0x37` will be provided to output. It wouldn't make sense in real world to pass a trigger to output. Modify the design to provide a next value after `0x37` on output signal. Keep in mind that the value might be changed after a random amount of time passed after trigger.
