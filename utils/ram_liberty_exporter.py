#!/usr/bin/env python3

from liberty_exporter import LibertyExporter


class RAMLibertyExporter(LibertyExporter):
    """RAM Liberty Exporter"""

    def __init__(self, memory):
        """Initializer"""
        LibertyExporter.__init__(self, memory)

    def write_cell(self, out_fh):
        """
        Writes the Liberty cell

        Difference is that we pass True to the rw_pin_set writer to indicate
        that this is a RAM.
        """

        name = self._memory.get_name()
        self.write_memory_section(out_fh)
        for i in range(0, self._memory.get_num_rw_ports()):
            suffix = chr(ord("a") + i)
            self.write_rw_pin_set(out_fh, name, suffix, True)
        self.write_clk_pin(out_fh)

    def write_memory_section(self, out_fh):
        """Writes the memory section to the output stream"""

        out_fh.write("    memory() {\n")
        out_fh.write("        type : ram;\n")
        out_fh.write("        address_width : %d;\n" % self._memory.get_addr_width())
        out_fh.write("        word_width : %d;\n" % self._memory.get_width())
        out_fh.write("    }\n")
