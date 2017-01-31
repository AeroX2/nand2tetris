// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
@color
M=0

(BEGIN)
	@KBD
	D=M
	@BLACK
	D;JNE
	(WHITE)
		@color
		M=0

		@IF_END
		0;JMP
	(BLACK)
		D=-1
		@color
		M=D
	(IF_END)

	(FILL)
		@i
		M=0
		(FILL_LOOP)
			@8192
			D=A
			@i
			D=M-D
			@END_FILL
			D;JGE

			@i
			D=M
			@SCREEN
			D=A+D
			@R0
			M=D
			@color
			D=M
			@R0
			A=M
			M=D

			@i
			M=M+1

			@FILL_LOOP
			0;JMP
	(END_FILL)
@BEGIN
0;JMP
