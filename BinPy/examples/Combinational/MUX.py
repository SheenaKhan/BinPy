from BinPy.Combinational.combinational import *
""" Examples for MUX class """
print "\n---Initializing the MUX class--- "
print "mux = MUX(0, 1)"
mux = MUX(0, 1)
print "\n---Put select lines---"
print "mux.selectLines(0)"
mux.selectLines(0)
print "\n---Output of mux"
print "mux.output()"
print mux.output()
print "\n---Input changes---"
print "mux.setInput(1, 0) #Input at index 1 is changed to 0"
mux.setInput(1, 0)
print "\n---New Output of the mux---"
print mux.output()
print "\n---Changing the number of inputs---"
print "No need to set the number, just change the inputs"
print "Input must be power of 2"
print "mux.setInputs(1, 0, 0, 1)"
mux.setInputs(1, 0, 0, 1)
print "\n---To get the input states---"
print "mux.getInputStates()"
print mux.getInputStates()
print "\n---New output of mux---"
print mux.output()
print "\n\n---Using Connectors as the input lines---"
print "Take a Connector"
print "conn = Connector()"
conn = Connector()
print "\n---Set Output of mux to Connector conn---"
print "mux.setOutput(conn)"
mux.setOutput(conn)
print "\n---Put this connector as the input to gate1---"
print "gate1 = AND(conn, 0)"
gate1 = AND(conn, 0)
print "\n---Output of the gate1---"
print "gate1.output()"
print gate1.output()
print "\n---Changing select lines---"
print "mux.selectLine(0, 1) #selects input line 2"
mux.selectLine(0, 1)
print "---New output of mux---"
print mux.output()
