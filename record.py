import options

def battue(niveau, temps):
    convertion = {5:1, 7:2, 8:3}
    record = int(options.get_score(convertion[niveau])[3:])
    if record > temps or record == 0:
        if temps < 10:
            options.set_record("00:0"+str(temps), convertion[niveau])
        else:
            options.set_record("00:" + str(temps), convertion[niveau])









