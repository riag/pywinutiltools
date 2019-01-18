
YES_LIST = ('YES', 'Y')
NO_LIST = ('NO', 'N')


def ask_yes_or_no(msg):
    while True:
        answer = input('%s ' % msg)
        if not answer:
            continue

        answer = answer.upper()
        if answer in YES_LIST:
            return True

        return False
