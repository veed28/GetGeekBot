from pywinauto.application import Application
from time import sleep
app = Application(backend='uia').connect(best_match="Surfshark")


def albania():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("alb")
    sleep(1)
    app.Surfshark.child_window(title="Albania", auto_id="location_albania", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to albania')


def andorra():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("and")
    sleep(1)
    app.Surfshark.child_window(title="Andorra", auto_id="location_andorra", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to andorra')


def austria():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("austria")
    sleep(1)
    app.Surfshark.child_window(title="Austria", auto_id="location_austria", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to austria')


def australia_perth():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("austral")
    sleep(1)
    app.Surfshark.child_window(title="Australia Perth", auto_id="location_australia_perth", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to australia-perth')


def australia_adelaide():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("austral")
    sleep(1)
    app.Surfshark.child_window(title="Australia Adelaide", auto_id="location_australia_adelaide", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to australia-adelaide')


def australia_melbourne():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("austral")
    sleep(1)
    app.Surfshark.child_window(title="Australia Melbourne", auto_id="location_australia_melbourne", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to australia-melbourne')


def australia_brisbane():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("austral")
    sleep(1)
    app.Surfshark.child_window(title="Australia Brisbane", auto_id="location_australia_brisbane", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to australia-brisbane')


def australia_sydney():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("austral")
    sleep(1)
    app.Surfshark.child_window(title="Australia Sydney", auto_id="location_australia_sydney", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to australia-sydney')


def belgium_brussels():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("belgium")
    sleep(1)
    app.Surfshark.child_window(title="Belgium Brussels", auto_id="location_belgium_brussels", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to belgium-brussels')


def belgium_antwerp():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("belgium")
    sleep(1)
    app.Surfshark.child_window(title="Belgium Antwerp", auto_id="location_belgium_antwerp", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to belgium-antwerp')

def canada_montreal():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("canada")
    sleep(1)
    app.Surfshark.child_window(title="Canada Montreal", auto_id="location_canada_montreal", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to canada-montreal')


def canada_toronto():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("canada")
    sleep(1)
    app.Surfshark.child_window(title="Canada Toronto", auto_id="location_canada_toronto", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to canada-toronto')


def canada_vancouver():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("canada")
    sleep(1)
    app.Surfshark.child_window(title="Canada Vancouver", auto_id="location_canada_vancouver", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to canada-vancouver')


def france_marseille():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("france")
    sleep(1)
    app.Surfshark.child_window(title="France Marseille", auto_id="location_france_marseille", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to france-marseille')


def france_paris():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("france")
    sleep(1)
    app.Surfshark.child_window(title="France Paris", auto_id="location_france_paris", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to france-paris')


def france_bordeaux():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("france")
    sleep(1)
    app.Surfshark.child_window(title="France Bordeaux", auto_id="location_france_bordeaux", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to france-bordeaux')


def serbia():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("serbia")
    sleep(1)
    app.Surfshark.child_window(title="Serbia", auto_id="location_serbia", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to serbia')


def bulgaria():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("bulgaria")
    sleep(1)
    app.Surfshark.child_window(title="Bulgaria", auto_id="location_bulgaria", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to bulgaria')


def brazil():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("brazil")
    sleep(1)
    app.Surfshark.child_window(title="Brazil", auto_id="location_brazil", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to brazil')


def croatia():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("croa")
    sleep(1)
    app.Surfshark.child_window(title="Croatia", auto_id="location_croatia", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to croatia')


def cambodia():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("cambo")
    sleep(1)
    app.Surfshark.child_window(title="Cambodia", auto_id="location_cambodia", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to cambodia')


def colombia():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("colombia")
    sleep(1)
    app.Surfshark.child_window(title="Colombia", auto_id="location_colombia", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to colombia')


def cyprus():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("cypr")
    sleep(1)
    app.Surfshark.child_window(title="Cyprus", auto_id="location_cyprus", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to cyprus')


def czech():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("cze")
    sleep(1)
    app.Surfshark.child_window(title="Czech Republic", auto_id="location_czech_republic", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to czechia')


def denmark():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("denmark")
    sleep(1)
    app.Surfshark.child_window(title="Denmark", auto_id="location_denmark", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to denmark')


def estonia():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("esto")
    sleep(1)
    app.Surfshark.child_window(title="Estonia", auto_id="location_estonia", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to estonia')


def finland():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("finl")
    sleep(1)
    app.Surfshark.child_window(title="Finland", auto_id="location_finland", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to finland')


def greece():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("greece")
    sleep(1)
    app.Surfshark.child_window(title="Greece", auto_id="location_greece", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to greece')


def hungary():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("hung")
    sleep(1)
    app.Surfshark.child_window(title="Hungary", auto_id="location_hungary", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to hungary')


def iceland():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("iceland")
    sleep(1)
    app.Surfshark.child_window(title="Iceland", auto_id="location_iceland", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to iceland')


def indonesia():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("indo")
    sleep(1)
    app.Surfshark.child_window(title="Indonesia", auto_id="location_indonesia", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to indonesia')


def ireland():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("irel")
    sleep(1)
    app.Surfshark.child_window(title="Ireland", auto_id="location_ireland", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to ireland')


def israel():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("isra")
    sleep(1)
    app.Surfshark.child_window(title="Israel", auto_id="location_israel", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to israel')


def kazakhstan():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("kaza")
    sleep(1)
    app.Surfshark.child_window(title="Kazakhstan", auto_id="location_kazakhstan", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to kazakhstan')


def latvia():
    app.Surfshark.child_window(title="Disconnect", auto_id="connect_button", control_type="Button").click()
    app.Surfshark.child_window(title="Change", control_type="Button").click()
    app.Surfshark.child_window(auto_id="locations_search", control_type="Edit").type_keys("latv")
    sleep(1)
    app.Surfshark.child_window(title="Latvia", auto_id="location_latvia", control_type="Button").click()
    app.Surfshark.child_window(title="Connect", auto_id="connect_button", control_type="Button").click()
    print('swapped to latvia')


vpn_list = [albania, andorra, australia_perth, australia_melbourne, australia_adelaide,
            belgium_antwerp, belgium_brussels, canada_vancouver, canada_montreal, canada_toronto,
            france_bordeaux, france_paris, france_marseille, austria, serbia, bulgaria, croatia, cambodia,
            colombia, cyprus, czech, denmark, finland, greece, iceland, ireland, israel, kazakhstan, latvia]