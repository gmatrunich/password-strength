import urwid

REQUIRED_PASSWORD_LENGTH = 12


def has_digit(password):
    return any(letter.isdigit() == True for letter in password)


def has_letters(password):
    return any(letter.isdigit() != True for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() == True for letter in password)


def has_lower_letters(password):
    return any(letter.islower() == True for letter in password)


def has_symbols(password):
    return any(letter.isdigit() != True and letter.isalpha() != True for letter in password)


def has_not_only_symbols(password):
    return not all(letter.isdigit() != True and letter.isalpha() != True for letter in password)


def is_very_long(password):
    return len(password) >= REQUIRED_PASSWORD_LENGTH


def checking(password, score=0):
    checkpoints = [has_digit,
                  has_letters,
                  has_upper_letters,
                  has_lower_letters,
                  is_very_long,
                  has_symbols,
                  has_not_only_symbols
    ]
    for checkpoint in checkpoints:
        if checkpoint(password) == True:
            score += 2
    return score


def on_ask_change(edit, password):
    reply.set_text("Рейтинг этого пароля: %s" % checking(password))


ask = urwid.Edit('Введите пароль: ')
reply = urwid.Text("")
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')
urwid.connect_signal(ask, 'change', on_ask_change)
urwid.MainLoop(menu).run()
