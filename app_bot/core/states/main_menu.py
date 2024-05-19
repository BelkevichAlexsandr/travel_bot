from aiogram.fsm.state import State, StatesGroup


class MainMenuStateGroup(StatesGroup):
    menu = State()

    pick_info = State()
    info = State()
    socials = State()

    warehouse = State()
    warehouse_video = State()

    addresses = State()
    addresses_info = State()

    reviews = State()

    pick_requirements = State()
    requirements = State()

    pick_faq = State()
    faq = State()

    pick_case = State()
    case = State()

    currency = State()

    input_length = State()
    input_width = State()
    input_height = State()
    input_photo = State()

    managers_cards = State()
