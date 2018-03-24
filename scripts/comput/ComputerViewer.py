# Had a neater solution using list comprehensions, 
# a data class and attrgetter, but Transcrypt doesn't like builtin modules
# or Jquery
# (or variables called 'var' but that one's obvs)


from data import *
from html_ids import *
from fields import *
from ComputerSelector import ComputerSelector


selecta = ComputerSelector(nullComputer)


# Entry point
def refresh(name) :
    criteria = get_criteria()
    criteria = infer_predicates(criteria, name)
    firstComputer = selecta.get_computer(computers, criteria)

    init_app()
    set_computer(firstComputer)


# The first comprehension just stores DOM queries, avoids querying twice.
def get_criteria() :
    checked = { f : get_radio_val(f) for f in fieldModel }
    return { f : checked[f] for f in fieldModel if checked[f] }


def get_radio_val( name ) :
    query = 'input[name="' + name + '"]:checked'
    dom = document.querySelector(query)

    return dom.value if dom else None



# First handle some special cases: e.g. analogs have no base.
# UX is terrible without this
def infer_predicates(data, name) :
    if name == Model.programmables :
        data = constrain_single_program(data)
    elif name == Model.universal :
        data = constrain_turing(data)
    elif name == Model.transistorised :
        data = constrain_transistor(data)
    elif name == Model.stored :
        data = constrain_stored(data)
    elif name == Model.gui :
        data = constrain_gui(data)
    elif name == Model.base :
        data = constrain_digital(data)
    elif name == Model.representation :
        data = constrain_analogue(data)

    return data


def constrain(id, isChecked=True) :
    document.getElementById(id).checked = isChecked


def constrain_analogue(data):
    elements = document.getElementsByName(BASE)

    if data[Model.representation] == Representation.ANALOG :
        for el in elements :
            el.checked = False
            el.disabled = True
    else :
        for el in elements :
            el.disabled = False

    return data


def constrain_digital(data) :
    if data[Model.base] is not "" :
        constrain(digId)
        data[Model.representation] = Representation.DIGITAL
    return data


def constrain_single_program(data) :
    if data[Model.programmables] == Programmables.FIXIE : 
        constrain(generalId, False)
        data[Model.universal] = Universal.SPECIAL
        constrain(specialId)
        data[Model.stored] = StoredProgram.STRUCTURAL
        constrain(notStoredId)

    return data


def constrain_turing(data) :
    if data[Model.universal] == Universal.TURING :
        constrain(programId)
        data[Model.programmables] = Programmables.GRAMMABLE
    return data


def constrain_transistor(data) :
    if data[Model.transistorised] == Transistorised.TRANSIST :
        constrain(electroId)
        data[Model.signals] = Signals.ELECTRO
    return data
    

def constrain_stored(data) :
    if data[Model.stored] == StoredProgram.STORED :
        constrain(programId)
        data[Model.programmables] = Programmables.GRAMMABLE
    return data


def constrain_gui(data) :
    if data[Model.gui] == Gui.GUI :
        constrain(electroId)
        data[Model.signals] = Signals.ELECTRO
    return data


#  Only once
def init_app() :
    global isAppInitialised

    if not isAppInitialised :
        document.getElementById(resultImg).style.display = ""
        hide_intro_text()
        set_image_size()
        isAppInitialised = True


def set_computer(computer) :
    name = "the " + computer[Model.name]
    set_html(resultName, name)
    who = "by " + computer[Model.protagonists]
    set_html(resultWho, who)
    when = "<br>fits the bill.<br><br>It was first operational " \
            + computer[Model.date] + "."
    set_html(resultDate, when)
    set_image(computer[Model.name])


def set_html(id, result) :
    document.getElementById(id).innerHTML = result


def set_image(name) :
    imgName = name.replace("#", "%23")
    imgDom = document.getElementById(resultImg)
    imgDom.src = "/img/spin.gif"

    # set_image_size(100,100)
    imgDom.src = "/img/comput/"+ imgName + ".jpg"
    set_image_size()


def hide_intro_text() :
    document.getElementById(intro).style.display = "none"


def set_image_size(x=400, y=300) :
    imgDom = document.getElementById(resultImg)
    imgDom.style.height = str(y) + "px"
    imgDom.style.width = str(x) + "px"


def reset() :
    for field in fieldModel:
        for dom in document.getElementsByName(field) :
            dom.checked = False
                
    set_computer(nullComputer)