
Examples for FourBitLoadRegister class
--------------------------------------

.. code:: python

    from __future__ import print_function
    from BinPy.Sequential import *
.. code:: python

    # Initialise clock c = Clock(1, 500)"
    
    c = Clock(1, 500)
    c.start()
.. code:: python

    # Initializing the FourBitLoadRegister class
    # Input is of the form (A0, A1, A2, A3, CLOCK, CLEAR, LOAD
    
    fr = FourBitLoadRegister(1, 0, 1, 1, c, 1, 1)
.. code:: python

    # Output of the register
    print (fr.output())

.. parsed-literal::

    [1, 0, 1, 1]


.. code:: python

    # Input changes
    # Input at index 1 is changed to 0
    fr.setInput(1, 0)
    
    # New Output of the register
    print (fr.output())

.. parsed-literal::

    [1, 0, 1, 1]


.. code:: python

    # Changing the inputs all at once
    # No need to set the number, just change the inputs
    
    fr.setInputs(1, 1, 1, 1)
    
    # Changing the load value
    
    fr.setLoad(0)
    
    # New Output of the register
    
    print (fr.output())

.. parsed-literal::

    [1, 0, 1, 1]


.. code:: python

    # To get the input states
    
    print (fr.getInputStates())

.. parsed-literal::

    [1, 1, 1, 1]


.. code:: python

    # New output of the register
    
    print (fr.output())

.. parsed-literal::

    [1, 0, 1, 1]


.. code:: python

    # Using Connectors as the input lines
    
    # Take a Connector
    
    conn = Connector()
    
    # Set Output of gate to Connector conn
    
    fr.setOutput(2, conn)
    
    # Put this connector as the input to gate1
    
    gate1 = AND(conn, 0)
    # Output of the gate1
    
    print (gate1.output())

.. parsed-literal::

    0

