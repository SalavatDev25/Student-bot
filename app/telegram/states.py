from aiogram.fsm.state import State, StatesGroup


class FsmMain(StatesGroup):
    MAIN = State()


class FsmStatement(StatesGroup):
    SELECT_DEPARTAMENT = State()
    INPUT_FIO = State()
    INPUT_GROUP_NUMBER = State()
    INPUT_TITLE = State()
    INPUT_STATEMENT = State()
    SUCCESS = State()


class FsmSupportChat(StatesGroup):
    OPEN_DIALOG = State()
    SEND_MESSAGE = State()
    CLOSE_DIALOG = State()
