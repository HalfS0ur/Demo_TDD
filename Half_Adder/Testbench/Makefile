# Makefile
export PYTHONPATH := $(PWD):$(PYTHONPATH)

TOPLEVEL_LANG = verilog

VERILOG_SOURCES = $(PWD)/../*.sv

TOPLEVEL = half_adder

MODULE = half_adder_tb

WAVES = 1

include $(shell cocotb-config --makefiles)/Makefile.sim