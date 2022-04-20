from extensions.settings.clearBrowsing import restart as restart


def clearb():
    with open('v3/extensions/settings/clearBrowsing/auto.txt', 'w') as f:
        f.write('')
        restart.restart_program()
