from axiom import attributes, item, upgrade

class Measurement(item.Item):
    typeName = "measurement"
    schemaVersion = 2

    temperature = attributes.point4decimal()
    pressure = attributes.point4decimal()


def _upgradeMeasurementTemperature(old):
    t = ((old.temperature - 32) * 5 / 9) + 273.15
    return Measurement(store=old.store, pressure=old.pressure, temperature=t)

upgrade.registerUpgrader(_upgradeMeasurementTemperature, "measurement", 1, 2)
