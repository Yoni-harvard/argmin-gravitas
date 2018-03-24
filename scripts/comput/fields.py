from enum import Enum


# TODO: Make binary options into Booleans


class Model(Enum):
	index = "index"
	name = "name"
	protagonists = "protagonists"
	date = "date"
	signals = "signals"
    universal = "universal"
 	programmables = "programmables"
	stored = "stored"
 	representation = "representation"
	base = "base"
    transmission = "transmission"
 	transistorised = "transistorised"
  	virtual = "virtual"
    instructions = "instructions"
 	gui = "gui"
 	notes = "notes"
 	link = "link"


class Signals(Enum):
	MECH = mechanical = "mechanical"
    ELECTROMECH = electromechanical = "electromechanical"
    ELECTRO = "fully-electronic"

class Universal(Enum):
	TURING = "general-purpose"
	SPECIAL = "special-purpose"

class Programmables(Enum):
	GRAMMABLE = "programmable"
	FIXIE = 'fixed-job'

class StoredProgram(Enum):
	STORED = "stored-program"
	STRUCTURAL = "structure-program"

class Representation(Enum):
	ANALOG = "analogue"
	DIGIT = "digital"

class Base(Enum):
	BINARY = 2
	TERNARY = 3
	DECIMAL = 10

class Transmission(Enum):
	SERIAL = serial = "serial"
	PARALLEL = parallel = "parallel"

class Transistorised(Enum):
	TRANSIST = 'transistorised'
	CIRCUITS = 'hard-wired'

class VirtualMemory(Enum):
	VIRTUAL = "virtual"
	PHYSICAL = "physical"

class Instructions(Enum):
	GATES = "Hard-wired"
	CISC = cisc = "cisc"
	RISC = risc = "risc"

class Gui(Enum):
	GUI = "gui-based"
	TERM = "terminal"
