

class Mop(object):

    # Global settings
    debug = True

    # MQTT Settings
    mqtt_server = "localhost"
    mqtt_port = 1833


    @staticmethod
    def printme(source, msg, debug=True):
        if debug == False:
            print("[INFO ] {}:\t{}".format(source, msg))

        elif Mop.debug & debug:
            print("[DEBUG] {}:\t{}".format(source, msg))



