import config

def display_settings():
    print "config.anneal = " + str(config.anneal)
    print "config.random_start = " + str(config.random_start)
    print "config.random_anneal = " + str(config.random_anneal)

def display_init_cost(cost):
            print "Best init cost " + str(cost)

def display_acceptance(ap, r, new_cost, status):
    if config.verbose == True:
        if status == "ACCEPT" : 
            sym = ">"
        else: 
            sym = "<"
        print ''
        print str(status) + ": " + str(ap) + " " + sym + " > RANDOM: " + str(r)
        print "new state's cost: " + str(new_cost)

def display_cost_change(bcost):
    if config.verbose==True:
        print "changed best cost to " + str(bcost)


def display_cost_after_iteration(i, cost):
    if config.verbose == True:
        print "Final best cost on iteration " + str(i) + ": " + str(cost)
