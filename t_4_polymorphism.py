#!/bin/python3

class Tone:
	def frequency(self):
		return "Every tone is defined by some frequency."

class ToneC(Tone):
	def frequency(self):
		return 261.626

class ToneD(Tone):
	def frequency(self):
		return 293.665

class ToneE(Tone):
	def frequency(self):
		return 329.628

class ToneF(Tone):
	def frequency(self):
		return 349.228

class ToneG(Tone):
	def frequency(self):
		return 391.995

class ToneA(Tone):
	def frequency(self):
		return 440

class ToneH(Tone):
	def frequency(self):
		return 493.883

class Caller:
	def call(self, obj):
		print(obj.frequency())

if (__name__ == '__main__'): #main function
	tones = [Tone(), ToneC(), ToneD(), ToneE(), ToneF(), ToneG(), ToneA(), ToneH()]
	caller = Caller()
	
	for tone in tones:
		caller.call(tone)
