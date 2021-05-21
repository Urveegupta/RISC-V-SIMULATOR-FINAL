# RISCV-Simulator Phase 2 

=============================================
Functional Simulator for RISC Processor
=============================================

Done by:
Aarushi 2019CSB1059
Karan deep 2019CSB1093
Kshitiz Arora 2019CSB1095
Urvee Gupta 2019CSB1128
Yash Priyadarshi 2019CSB1133

Table of contents:-
1. Directory Structure 
2. How to execute
3. Some assumptions
4. GUI Structure

======================
Directory Structure:-
======================

RISCV-Simulator
  |
  |- src
      |
      |- main.py(containing whole code to run)
      |- ph1gui.py(containing the code for gui non pipelined)
      |- ph2gui.py(containing the code for gui pipelined)
      |- pipelining.py (implementation of pipelined execution)
      |- temp3.py (non pipelined implementation)
      |- test.txt (a test case)

  |- doc
      |
      |- design-doc.docx
  |- README.md
      |
  |- test
      |- input_fib11.mc
      |- input_fact10.mc
      |- bubble_inp.mc

==============
How to run
==============
	|
	Running on Spyder
	|
	|_ _(With GUI)-
	|	|
	|	| 
	| A window will appear
	| Select the knobs as per choice
 	| >>>> For pipelined implementation, click yes, else No
	|
	| >>>>Click on Step button on the gui for cycle by cycle execution
	|	-There is a Registers Button and a Memory Button.
	|	-The Registers Button shows all the registers and the values in them
	|	-The Memory Button shows all the data stored at different addresses in the memory
	|	-There are three more buttons which show the Heap and Stack Memory.
	|
	| >>>>There are buttons for enabling data forwarding and Stalling
	|
	| >>>>There is an additonal text box here which will tell you what cycle is going on for the instruction
	| If you want to run the whole code together:- Click on the Run Button
	|
	|	
	|	

		
================
Assumptions
================
Delimiter-text_end


==================
More About GUI
==================
Output  
--While proceeding with step button
--It will show the buffers
--It will show PC,Machine Code and the current cycle of the current instruction (current buffer being used)

Input files (".mc" files in test folder)
--This is the input file containing all the machine codes
------text instructions format:-
	PC<space>MachineInstruction
------Delimiter(text_end)
------Data instructions format:-
	MemoryLocation<space>ByteValue
	Our memory is Byte Addressable

Step and Run button
--Function already explained above

Register
--Shows value of all the registers

Memory
--Shows value of memory byte by byte
