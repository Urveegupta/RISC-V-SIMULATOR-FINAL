# RISCV-Simulator

Done by:
Aarushi 2019CSB1059
Karan deep 2019CSB1093
Kshitiz Arora 2019CSB1095
Urvee Gupta 2019CSB1128
Yash Priyadarshi 2019CSB1133

=============================================
Functional Simulator for RISC Processor
=============================================

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
      |- temp3.py(containing whole code to run on terminal)
      |- final1.py(containing whole code to run on gui window)
  |- doc
      |
      |- design-doc.docx
  |- README.md
      |
  |- test
      |-input_fib11.mc
	  |-input_fact10.mc
	  |-input_bubble.mc
      |-inp.mc

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
 	| If you want to run the code step by step:-
	| >>>>Click on Step button on the gui 
	|	-There is a Registers Button and a Memory Button.
	|	-The Registers Button shows all the registers and the values in them
	|	-The Memory Button shows all the data stored at different addresses in the memory
	|	-There are three more buttons which show the Heap and Stack Memory.
	|
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
--It will show PC and the Machine Code
--Fetched Instruction,Instruction type, Operation, Execute, Memory accessed and the Registers Updated

Open data.mc button
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
 

