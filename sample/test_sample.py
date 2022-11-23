import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock


@cocotb.test()
async def sample_simple_test(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    await FallingEdge(dut.clk)              # Synchronize with the clock

    dut.input_.value = 0b11100111

    await Timer(100, 'us')
    dut.input_.value = 0x21
    await Timer(100, 'us')
    assert dut.output_.value == (~0x21 & 0xff)

    dut._log.info("out is %s", dut.output_.value)
