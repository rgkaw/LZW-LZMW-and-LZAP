# LZW-LZMW-and-LZAP
Implementation of LZW, LZW, and LZMW using Python.
this files is far from perfect, im focused on how to implementing the algoritm to actually give output 

there is no decoder yet. 

for output of all program, the first byte contain the bit length of 1 sequence, which is the length of bit of largest integer of output sequence.
the last byte contain the padding.

after some test, these methode were only effective if the input given is txt file. Three generated random binary file tested,
and the output size is 1.5 times larger than the input.
