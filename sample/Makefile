TOPLEVEL_LANG ?= verilog
SIM ?= verilator

VERILOG_SOURCES = $(shell pwd)/sample.sv

MODULE = test_sample
TOPLEVEL = fake_crypto

include $(shell cocotb-config --makefiles)/Makefile.sim
