import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def prueba_a0_b0(dut):
    dut.a_i.value = 0
    dut.b_i.value = 0

    suma = (0 ^ 0)
    carry = (0 & 0)

    await Timer(1, units='ns')

    assert dut.sum_o.value == suma, f"El valor de sum_o esperado es {suma}, se recibió {dut.sum_o.value}"
    assert dut.carry_o.value == carry, f"El valor de carry_o esperado es {carry}, se recibió {dut.carry_o.value}"


@cocotb.test()
async def prueba_a1_b0(dut):
    dut.a_i.value = 1
    dut.b_i.value = 0

    suma = (1 ^ 0)
    carry = (1 & 0)

    await Timer(1, units='ns')

    assert dut.sum_o.value == suma, f"El valor de sum_o esperado es {suma}, se recibió {dut.sum_o.value}"
    assert dut.carry_o.value == carry, f"El valor de carry_o esperado es {carry}, se recibió {dut.carry_o.value}"


@cocotb.test()
async def prueba_a0_b1(dut):
    dut.a_i.value = 0
    dut.b_i.value = 1

    suma = (0 ^ 1)
    carry = (0 & 1)

    await Timer(1, units='ns')

    assert dut.sum_o.value == suma, f"El valor de sum_o esperado es {suma}, se recibió {dut.sum_o.value}"
    assert dut.carry_o.value == carry, f"El valor de carry_o esperado es {carry}, se recibió {dut.carry_o.value}"


@cocotb.test()
async def prueba_a1_b1(dut):
    dut.a_i.value = 1
    dut.b_i.value = 1

    suma = (1 ^ 1)
    carry = (1 & 1)

    await Timer(1, units='ns')

    assert dut.sum_o.value == suma, f"El valor de sum_o esperado es {suma}, se recibió {dut.sum_o.value}"
    assert dut.carry_o.value == carry, f"El valor de carry_o esperado es {carry}, se recibió {dut.carry_o.value}"

