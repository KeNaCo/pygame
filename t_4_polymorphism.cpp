/*****************************************************************************
 * Soubor:   c++.cpp
 * Datum:    
 * Autor:    Jan Porhincak, xporhi00@fit.vutbr.cz
 * Projekt:  
 * Verzia:
 * Komentar: 
 * Poznamka: 
 *****************************************************************************/

#include <iostream>

class Tone {
	public:
	virtual std::string frequency() {
		return "Every tone is defined by some frequency.";
	}
}

class ToneC(Tone) {
	std::string frequency() {
		return "261.626";
	}
}

class ToneD(Tone) {
	std::string frequency() {
		return "293.665";
	}
}

class ToneE(Tone) {
	std::string frequency() {
		return "329.628";
	}
}

class ToneF(Tone) {
	std::string frequency() {
		return "349.228";
	}
}

class ToneG(Tone) {
	std::string frequency() {
		return "391.995";
	}
}

class ToneA(Tone) {
	std::string frequency() {
		return "440";
	}
}

class ToneH(Tone) {
	std::string frequency() {
		return "493.883";
	}
}

class Caller {
	void call(Tone* obj) {
		print(obj.frequency());

int main(int argc, char* argv[])
{
	tones[] = { Tone(), ToneC(), ToneD(), ToneE(), ToneF(), ToneG(), ToneA(), ToneH() };
	caller = Caller();
	
	for (int i=0; i < 8; i++) {
		caller.call(&(tones[i]));
	}
}
